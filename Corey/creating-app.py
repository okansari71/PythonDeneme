from PyQt5 import QtWidgets
import sys

app = QtWidgets.QApplication(sys.argv)
window = QtWidgets.QWidget()
window.setWindowTitle("PyQt5 Test Penceresi")
window.resize(300, 200)
window.show()
sys.exit(app.exec_())