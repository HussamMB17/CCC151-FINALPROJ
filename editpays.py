import sys
from PyQt5.QtWidgets import (QApplication, QDialog, QVBoxLayout, QLineEdit, 
                             QPushButton, QLabel, QHBoxLayout, QGridLayout, 
                             QDateEdit, QComboBox, QSizePolicy, QSpacerItem)
from PyQt5.QtCore import QDate

class PaysDialog(QDialog):
    def __init__(self):
        super().__init__()

        # Set the window title and size
        self.setWindowTitle("Payment Information")
        self.setFixedSize(400, 500)

        # Set the overall stylesheet for the dialog
        self.setStyleSheet("""
        QDialog {
            background-color: #f8f8f8;
            font-family: Arial, sans-serif;
        }
        QLabel {
            color: #000000;
            font-size: 14px;
        }
        QLineEdit, QDateEdit, QComboBox {
            border: 1px solid #cccccc;
            border-radius: 5px;
            padding: 10px;
            font-size: 14px;
            background-color: #ffffff;
            color: #333333;
        }
        QPushButton {
            background-color: #000000;
            color: #ffffff;
            border: none;
            border-radius: 5px;
            padding: 10px;
            font-size: 14px;
        }
        QPushButton:hover {
            background-color: #333333;
        }
        QPushButton:pressed {
            background-color: #555555;
        }
        """)

        # Create layout with margins and spacing
        layout = QVBoxLayout()
        layout.setContentsMargins(20, 20, 20, 20)
        layout.setSpacing(15)

        # Create a grid layout for input fields and labels
        grid_layout = QGridLayout()
        grid_layout.setVerticalSpacing(10)
        grid_layout.setHorizontalSpacing(10)

        # Create QLineEdits, QDateEdit and QComboBoxes for each attribute
        self.tenant_id_edit = QLineEdit(self)
        self.unit_id_edit = QLineEdit(self)
        self.payment_date_edit = QDateEdit(self)
        self.payment_date_edit.setCalendarPopup(True)
        self.payment_date_edit.setDate(QDate.currentDate())
        self.payment_type_combo = QComboBox(self)
        self.payment_type_combo.addItems(["Credit Card", "Debit Card", "Cash", "Bank Transfer"])
        self.payment_status_combo = QComboBox(self)
        self.payment_status_combo.addItems(["Pending", "Completed", "Failed"])

        # Add labels and QLineEdits to grid layout
        grid_layout.addWidget(QLabel("Tenant ID:"), 0, 0)
        grid_layout.addWidget(self.tenant_id_edit, 1, 0, 1, 2)
        grid_layout.addWidget(QLabel("Unit ID:"), 2, 0)
        grid_layout.addWidget(self.unit_id_edit, 3, 0, 1, 2)
        grid_layout.addWidget(QLabel("Payment Date:"), 4, 0)
        grid_layout.addWidget(self.payment_date_edit, 5, 0, 1, 2)
        grid_layout.addWidget(QLabel("Payment Type:"), 6, 0)
        grid_layout.addWidget(self.payment_type_combo, 7, 0, 1, 2)
        grid_layout.addWidget(QLabel("Payment Status:"), 8, 0)
        grid_layout.addWidget(self.payment_status_combo, 9, 0, 1, 2)

        # Add grid layout to the main layout
        layout.addLayout(grid_layout)

        # Create and add submit and cancel buttons to the main layout
        button_layout = QHBoxLayout()
        button_layout.addSpacerItem(QSpacerItem(20, 0, QSizePolicy.Expanding, QSizePolicy.Minimum))
        self.cancel_button = QPushButton("Cancel", self)
        self.submit_button = QPushButton("Submit", self)
        button_layout.addWidget(self.cancel_button)
        button_layout.addWidget(self.submit_button)
        button_layout.addSpacerItem(QSpacerItem(20, 0, QSizePolicy.Expanding, QSizePolicy.Minimum))

        # Add button layout to the main layout
        layout.addLayout(button_layout)

        # Set the main layout for the dialog
        self.setLayout(layout)

        # Connect the buttons to their respective slots
        self.submit_button.clicked.connect(self.submit)
        self.cancel_button.clicked.connect(self.cancel)

    def submit(self):
        tenant_id = self.tenant_id_edit.text().strip()
        unit_id = self.unit_id_edit.text().strip()
        payment_date = self.payment_date_edit.date().toString("yyyy-MM-dd")
        payment_type = self.payment_type_combo.currentText()
        payment_status = self.payment_status_combo.currentText()

        # Validate the inputs
        if not tenant_id or not unit_id or not payment_date or not payment_type or not payment_status:
            error_dialog = QDialog(self)
            error_dialog.setWindowTitle("Input Error")
            error_dialog.setFixedSize(300, 100)
            error_dialog.setStyleSheet("""
            QDialog {
                background-color: #f8f8f8;
                font-family: Arial, sans-serif;
            }
            QLabel {
                color: #333333;
                font-size: 14px;
            }
            QPushButton {
                background-color: #000000;
                color: #ffffff;
                border: none;
                border-radius: 5px;
                padding: 5px 10px;
                font-size: 14px;
            }
            QPushButton:hover {
                background-color: #333333;
            }
            QPushButton:pressed {
                background-color: #555555;
            }
            """)
            error_layout = QVBoxLayout()
            error_layout.setContentsMargins(20, 20, 20, 20)
            error_message = QLabel("All fields must be filled out.")
            error_layout.addWidget(error_message)
            ok_button = QPushButton("OK")
            ok_button.clicked.connect(error_dialog.accept)
            button_layout = QHBoxLayout()
            button_layout.addSpacerItem(QSpacerItem(20, 0, QSizePolicy.Expanding, QSizePolicy.Minimum))
            button_layout.addWidget(ok_button)
            button_layout.addSpacerItem(QSpacerItem(20, 0, QSizePolicy.Expanding, QSizePolicy.Minimum))
            error_layout.addLayout(button_layout)
            error_dialog.setLayout(error_layout)
            error_dialog.exec_()
            return

        # Print the values (replace this with actual handling code)
        print(f"Tenant ID: {tenant_id}")
        print(f"Unit ID: {unit_id}")
        print(f"Payment Date: {payment_date}")
        print(f"Payment Type: {payment_type}")
        print(f"Payment Status: {payment_status}")

        # Close the dialog
        self.accept()

    def cancel(self):
        # Add any actions you want to perform when cancel button is clicked
        self.reject()  # Close the dialog without accepting input

if __name__ == "__main__":
    app = QApplication(sys.argv)
    dialog = PaysDialog()  # Instantiate your custom dialog
    dialog.exec_()  # Call exec_() on the instance
    sys.exit(app.exec_())
