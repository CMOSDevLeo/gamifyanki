from PyQt6.QtWidgets import QApplication, QDialog, QLabel, QVBoxLayout
from PyQt6.QtCore import QTimer, QSize, Qt
from PyQt6.QtGui import QFont
from aqt.reviewer import Reviewer
from anki.hooks import wrap

# Global variable to hold the reference to the dialog
global_dialog = None

def show_message(reviewer, ease):
    global global_dialog
    if ease == 3 or ease == 4:  # Ease 3 is "Good" in Anki's rating system
        app = QApplication.instance()
        
        global_dialog = QDialog()
        global_dialog.setWindowTitle("Message")
        global_dialog.setStyleSheet("background-color: #92E000;")
        global_dialog.setMinimumSize(QSize(300, 200))


        label = QLabel("Very Nice! :D ", global_dialog)
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)  # Center the text
        label.setStyleSheet("color: white;")
        
        font = QFont()
        font.setPointSize(20)  # Set a larger font size
        font.setBold(True)
        
        label.setFont(font)
        

        layout = QVBoxLayout()
        layout.addWidget(label)
        layout.setContentsMargins(0,0,0,25)
        
        global_dialog.setLayout(layout)
        global_dialog.show()

        QTimer.singleShot(2000, global_dialog.close)

Reviewer._answerCard = wrap(Reviewer._answerCard, show_message)
