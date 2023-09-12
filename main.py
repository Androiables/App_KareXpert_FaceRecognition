import sys
from PyQt5.QtWidgets import QApplication
from out_window import Ui_OutputDialog

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ui = Ui_OutputDialog()
    ui.show()
    ui.startVideo("0")
    sys.exit(app.exec_())
