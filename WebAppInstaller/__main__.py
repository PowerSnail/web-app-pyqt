import fire
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication

from . import main_window, webwindow


def config():
    app = QApplication(["WebAppInstaller"])
    w = main_window.MainWindow()
    w.show()
    return app.exec()


def app(name, url, icon_name=None, desktop_file=None):
    app = QApplication([name])
    icon = QIcon.fromTheme(icon_name)
    if not icon:
        icon = QIcon.fromTheme("internet-web-browser")
    app.setWindowIcon(icon)
    app.setDesktopFileName(name)

    w = webwindow.WebWindow(url, icon)
    w.show()
    return app.exec()


fire.Fire()
