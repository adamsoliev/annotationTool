#!./env/bin/python3

# system imports
import argparse
import sys

# 3rd party imports
from PySide6 import QtWidgets

# Project imports
from src.MainWindow import MainWindow

if __name__ == "__main__":
    options = argparse.ArgumentParser()
    options.add_argument("-f", "--file", type=str, required=False)
    args = options.parse_args()
    # data = read_data(args.file)
    # some arguments

    app = QtWidgets.QApplication(sys.argv)

    widget = MainWindow()
    widget.show()

    sys.exit(app.exec())