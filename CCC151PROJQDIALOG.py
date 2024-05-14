import sys
from PyQt5.QtWidgets import QApplication, QVBoxLayout, QPushButton, QLabel, QDialog, QWidget
from PyQt5.QtCore import Qt

# Mock functions to fetch data from MySQL for tenants and units (replace with actual implementation)
def fetch_tenant_data_from_mysql():
    # Mock tenant data for demonstration
    return [
        {'tenant_name': 'John Doe'},
        {'tenant_name': 'Jane Smith'}
    ]

def fetch_unit_data_from_mysql():
    # Mock unit data for demonstration
    return [
        {'unit_name': 'Unit A'},
        {'unit_name': 'Unit B'}
    ]

# Dialog for editing tenant information
class EditTenantDialog(QDialog):
    def __init__(self, tenant_name, parent=None):
        super(EditTenantDialog, self).__init__(parent)
        self.tenant_name = tenant_name
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        title_label = QLabel("Edit Tenant")
        layout.addWidget(title_label)

        self.tenant_info_label = QLabel("Tenant Name: " + self.tenant_name)
        layout.addWidget(self.tenant_info_label)

        edit_button = QPushButton("Edit")
        edit_button.clicked.connect(self.editTenant)
        layout.addWidget(edit_button)

        cancel_button = QPushButton("Cancel")
        cancel_button.clicked.connect(self.reject)
        layout.addWidget(cancel_button)

        self.setLayout(layout)
        self.setWindowTitle("Edit Tenant")

    def editTenant(self):
        print("Editing Tenant:", self.tenant_name)

# Dialog for editing unit information
class EditUnitDialog(QDialog):
    def __init__(self, unit_name, parent=None):
        super(EditUnitDialog, self).__init__(parent)
        self.unit_name = unit_name
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        title_label = QLabel("Edit Unit")
        layout.addWidget(title_label)

        self.unit_info_label = QLabel("Unit Name: " + self.unit_name)
        layout.addWidget(self.unit_info_label)

        edit_button = QPushButton("Edit")
        edit_button.clicked.connect(self.editUnit)
        layout.addWidget(edit_button)

        cancel_button = QPushButton("Cancel")
        cancel_button.clicked.connect(self.reject)
        layout.addWidget(cancel_button)

        self.setLayout(layout)
        self.setWindowTitle("Edit Unit")

    def editUnit(self):
        print("Editing Unit:", self.unit_name)

# Dialog for deleting tenant information
class DeleteTenantDialog(QDialog):
    def __init__(self, tenant_name, parent=None):
        super(DeleteTenantDialog, self).__init__(parent)
        self.tenant_name = tenant_name
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        title_label = QLabel("Delete Tenant")
        layout.addWidget(title_label)

        self.tenant_info_label = QLabel("Tenant Name: " + self.tenant_name)
        layout.addWidget(self.tenant_info_label)

        delete_button = QPushButton("Delete")
        delete_button.clicked.connect(self.deleteTenant)
        layout.addWidget(delete_button)

        cancel_button = QPushButton("Cancel")
        cancel_button.clicked.connect(self.reject)
        layout.addWidget(cancel_button)

        self.setLayout(layout)
        self.setWindowTitle("Delete Tenant")

    def deleteTenant(self):
        print("Deleting Tenant:", self.tenant_name)

# Dialog for deleting unit information
class DeleteUnitDialog(QDialog):
    def __init__(self, unit_name, parent=None):
        super(DeleteUnitDialog, self).__init__(parent)
        self.unit_name = unit_name
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        title_label = QLabel("Delete Unit")
        layout.addWidget(title_label)

        self.unit_info_label = QLabel("Unit Name: " + self.unit_name)
        layout.addWidget(self.unit_info_label)

        delete_button = QPushButton("Delete")
        delete_button.clicked.connect(self.deleteUnit)
        layout.addWidget(delete_button)

        cancel_button = QPushButton("Cancel")
        cancel_button.clicked.connect(self.reject)
        layout.addWidget(cancel_button)

        self.setLayout(layout)
        self.setWindowTitle("Delete Unit")

    def deleteUnit(self):
        print("Deleting Unit:", self.unit_name)

# Main window to display buttons for each tenant and unit
class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        # Fetch data for tenants and units separately
        tenant_data = fetch_tenant_data_from_mysql()
        unit_data = fetch_unit_data_from_mysql()

        # Create buttons for each tenant
        for tenant_row in tenant_data:
            tenant_name = tenant_row['tenant_name']
            edit_tenant_button = QPushButton("Edit Tenant: " + tenant_name)
            edit_tenant_button.clicked.connect(lambda _, tenant=tenant_name: self.showEditTenantDialog(tenant))
            layout.addWidget(edit_tenant_button)

            delete_tenant_button = QPushButton("Delete Tenant: " + tenant_name)
            delete_tenant_button.clicked.connect(lambda _, tenant=tenant_name: self.showDeleteTenantDialog(tenant))
            layout.addWidget(delete_tenant_button)

        # Create buttons for each unit
        for unit_row in unit_data:
            unit_name = unit_row['unit_name']
            edit_unit_button = QPushButton("Edit Unit: " + unit_name)
            edit_unit_button.clicked.connect(lambda _, unit=unit_name: self.showEditUnitDialog(unit))
            layout.addWidget(edit_unit_button)

            delete_unit_button = QPushButton("Delete Unit: " + unit_name)
            delete_unit_button.clicked.connect(lambda _, unit=unit_name: self.showDeleteUnitDialog(unit))
            layout.addWidget(delete_unit_button)

        self.setLayout(layout)
        self.setWindowTitle("Main Window")
        self.show()

    def showEditTenantDialog(self, tenant_name):
        dialog = EditTenantDialog(tenant_name, self)
        dialog.exec_()

    def showEditUnitDialog(self, unit_name):
        dialog = EditUnitDialog(unit_name, self)
        dialog.exec_()

    def showDeleteTenantDialog(self, tenant_name):
        dialog = DeleteTenantDialog(tenant_name, self)
        dialog.exec_()

    def showDeleteUnitDialog(self, unit_name):
        dialog = DeleteUnitDialog(unit_name, self)
        dialog.exec_()

# Run the application
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())
