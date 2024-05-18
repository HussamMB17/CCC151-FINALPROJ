import sys
from PyQt5.QtWidgets import QApplication, QDialog, QVBoxLayout, QPushButton, QLabel, QHBoxLayout, QSizePolicy, QSpacerItem

class DeleteConfirmationDialog(QDialog):
    def __init__(self):
        super().__init__()

        # Set the window title and size
        self.setWindowTitle("Delete Confirmation")
        self.setFixedSize(300, 150)

        # Set the overall stylesheet for the dialog
        self.setStyleSheet("""
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

        # Create the main layout
        layout = QVBoxLayout()
        layout.setContentsMargins(20, 20, 20, 20)
        layout.setSpacing(15)

        # Create a label with the confirmation message
        confirmation_label = QLabel("Are you sure you want to delete this item?")
        layout.addWidget(confirmation_label)

        # Create a horizontal layout for the buttons
        button_layout = QHBoxLayout()

        # Add spacer to push buttons to the right
        button_layout.addSpacerItem(QSpacerItem(20, 0, QSizePolicy.Expanding, QSizePolicy.Minimum))

        # Create and add Yes and No buttons
        self.no_button = QPushButton("No", self)
        self.yes_button = QPushButton("Yes", self)
        button_layout.addWidget(self.no_button)
        button_layout.addWidget(self.yes_button)

        # Add the button layout to the main layout
        layout.addLayout(button_layout)

        # Set the main layout for the dialog
        self.setLayout(layout)

        # Connect the buttons to their respective slots
        self.yes_button.clicked.connect(self.accept)
        self.no_button.clicked.connect(self.reject)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    dialog = DeleteConfirmationDialog()
    result = dialog.exec_()
    if result == QDialog.Accepted:
        print("Item will be deleted.")
    else:
        print("Deletion cancelled.")
    sys.exit(app.exec_())
