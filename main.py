#!./env/bin/python3

import sys
import random

from PySide6 import QtCore, QtWidgets, QtGui

import io
from PIL import Image, ImageCms
def convert_to_srgb(file_path):
        '''Convert PIL image to sRGB color space (if possible)'''
        print("convert_to_srgb(", file_path, ")")
        img = Image.open(file_path)
        icc = img.info.get('icc_profile', '')
        if icc:
            io_handle = io.BytesIO(icc)     # virtual file
            src_profile = ImageCms.ImageCmsProfile(io_handle)
            dst_profile = ImageCms.createProfile('sRGB')
            img_conv = ImageCms.profileToProfile(img, src_profile, dst_profile)
            icc_conv = img_conv.info.get('icc_profile','')
        if icc != icc_conv:
            # ICC profile was changed -> save converted file
            img_conv.save(file_path,
                        format = 'JPEG',
                        quality = 50,
                        icc_profile = icc_conv)
        print("--- end ---")

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

    @QtCore.Slot()
    def loadImage(self):
        convert_to_srgb("./image.jpg")
        self.image.load("./image.jpg")
        label = QtWidgets.QLabel(self)
        pixmap = QtGui.QPixmap('image.jpg')
        label.setPixmap(pixmap)
        label.resize(pixmap.width(),pixmap.height())
        label.show()


if __name__ == "__main__":
    app = QtWidgets.QApplication([])

    widget = MyWidget()
    widget.resize(800, 600)
    widget.show()

    sys.exit(app.exec())

