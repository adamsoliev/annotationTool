from PySide6.QtWidgets import QMainWindow, QWidget, QLabel
from PySide6.QtGui import QAction, QKeySequence, QPixmap

from src.AT_utils import convert_to_srgb


class MainWindow(QMainWindow):
    def __init__(self, width=800, height=600):
        QMainWindow.__init__(self)
        self.setWindowTitle("Annotation Tool")

        # Menu
        self.menu = self.menuBar()
        self.file_menu = self.menu.addMenu("File")

        # Upload Action
        upload_action = QAction("Upload", self)
        upload_action.triggered.connect(self.load_image())

        # Exit QAction
        exit_action = QAction("Exit", self)
        exit_action.setShortcut(QKeySequence.Quit)
        exit_action.triggered.connect(self.close)

        self.file_menu.addAction(exit_action)

        # Status bar
        """
        self.status = self.statusBar()
        self.status.showMessage("Data loaded and plotted")
        """

        # Window dimensions
        self.setFixedSize(width, height)
        """
        geometry = self.screen().availableGeometry()
        """

    def load_image(self):
        convert_to_srgb('image.jpg')
        label = QLabel(self)
        pixmap = QPixmap('image.jpg')
        label.setPixmap(pixmap)
        label.resize(pixmap.width(), pixmap.height())
        label.show()


"""
class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.hello = ["Hallo Welt", "Hei maailma", "Hola Mundo", "Привет мир"]

        self.button = QtWidgets.QPushButton("Click me!")
        self.imageButton = QtWidgets.QPushButton("Load an image")
        self.text = QtWidgets.QLabel("Hello World",
                                     alignment=QtCore.Qt.AlignCenter)
        self.image = QtGui.QImage()

        self.layout = QtWidgets.QVBoxLayout(self)
        self.layout.addWidget(self.text)
        self.layout.addWidget(self.button)
        self.layout.addWidget(self.imageButton)

        self.button.clicked.connect(self.magic)
        self.imageButton.clicked.connect(self.loadImage)

    @QtCore.Slot()
    def magic(self):
        self.text.setText(random.choice(self.hello))

    def loadImage(self):
        convert_to_srgb("image.jpg")
        self.image.load("./image.jpg")
        label = QtWidgets.QLabel(self)
        pixmap = QtGui.QPixmap('image.jpg')
        label.setPixmap(pixmap)
        label.resize(pixmap.width(), pixmap.height())
        label.show()
"""
