from PyQt5 import QtWidgets
from PyQt5.QtCore import QMimeData


class Clipboard:
    def __init__(self) -> None:
        app = QtWidgets.QApplication([])
        self._qt5_clipboard = app.clipboard()

    def read_clipboard_text(self) -> str | None:
        data = self._qt5_clipboard.mimeData()

        if data is None:
            return None

        return data.data("text/plain").data().decode()

    def write_clipboard_txt(self, text: str) -> None:
        data = QMimeData()
        data.setText(text)
        self._qt5_clipboard.setMimeData(data)

