from PyQt5.QtGui import QGuiApplication
from PyQt5 import QtWidgets

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    clipboard = QGuiApplication.clipboard()
    mimeData = clipboard.mimeData()
    print(clipboard)
    for format in mimeData.formats():
        print(f'{format}: {mimeData.data(format)}')

