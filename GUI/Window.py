import sys
from PyQt5.QtWidgets import  *


class GeneScriptionGUI(QMainWindow):

    def __init__(self):
        super.__init__()
        self.setWindowTitle("GeneScription")
        self.setGeometry(600,600,800,800)

        btn1 = QPushButton("btn1",self)
        btn1.clicked.connect(self.btn1_click())


    def btn1_click(self):
        QMessageBox.about(self,"title","clicked")



app =QApplication(sys.argv)

geneScriptionGUI = GeneScriptionGUI()
geneScriptionGUI.show()

app.exec()
