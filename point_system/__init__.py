# doesnt work when using controller

from aqt import mw
from aqt.qt import *
from aqt.reviewer import Reviewer
from anki.hooks import wrap
from PyQt6.QtGui import QFont

 
points = 0
new_points = 0
points_label = None
label_created = False

def update_Points(self, ease):
    global points
    global new_points
    global points_label
    global label_created
    
    if label_created == False:
        setup_points_label()
        label_created = True 
    
    if ease in [2, 3, 4]:
        new_points += 10
        if points_label:
            points_label.setText(f"[ {points:02} ] + {new_points} !")
        
    elif ease in [1]:
        if points_label:
            points += new_points
            new_points = 0
            points_label.setText(f"[ {points} ]")
            
            
def setup_points_label():
    global points_label
    points_label = QLabel(f"[ {points:02} ]", mw)
    points_label.move(30, 80)

    font = QFont()
    font.setPointSize(13)
    font.setBold(True)

    points_label.setFont(font)
    points_label.show()

# test


Reviewer._answerCard = wrap(Reviewer._answerCard, update_Points)