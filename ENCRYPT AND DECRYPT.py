import sys
from PyQt5.QtWidgets import QApplication,QFormLayout,QMessageBox,QPushButton,QTextEdit,QWidget

def showondisplay():
    freshlyentered = entertext.toPlainText()
    displaytext.setText(freshlyentered)



if __name__=="__main__":
    app=QApplication(sys.argv)
    w=QWidget()
    w.resize(900,900)
    w.setWindowTitle('bojuAI')

    displaytext = QTextEdit(w)
    displaytext.resize(800,300)
    displaytext.move(50,50)
    displaytext.setReadOnly(True)
    displaytext.setStyleSheet("background-color: black; color: white")
    #displaytext.setPlaceholderText("Do not type here")

    entertext = QTextEdit(w)
    entertext.resize(800,300)
    entertext.move(50,550)
    entertext.setReadOnly(False)
    entertext.setStyleSheet("background-color: white; color: black")
    entertext.setPlaceholderText("Enter text here")
    entertext.textChanged.connect(showondisplay)
    ##call a function named showondisplay which simply pulls the content 
    #from entertext and  makes it the content on displaytext

    w.show()
    sys.exit(app.exec())
    
    

