import webbrowser

from PyQt5.QtCore import QUrl
from PyQt5.QtGui import QIcon
from PyQt5.QtWebEngineWidgets import QWebEnginePage, QWebEngineProfile, QWebEngineSettings, QWebEngineView
from PyQt5.QtWidgets import QApplication, QMainWindow

from . import ui_webwindow


class NewPageHandler(QWebEnginePage):
    def __init__(self, parent=None) -> None:
        super().__init__(parent)

    def acceptNavigationRequest(self, url, *_):
        webbrowser.open(url.toString())
        self.setParent(None)
        return False


class MyWebPage(QWebEnginePage):

    def __init__(self, profile, parent=None) -> None:
        super().__init__(profile, parent)

    def createWindow(self, t: QWebEnginePage.WebWindowType):
        return NewPageHandler(self)


class WebWindow(QMainWindow, ui_webwindow.Ui_WebWindow):
    def __init__(self, url: str, home_url: str, icon: QIcon, ua: str):
        super().__init__()
        self.setupUi(self)
        self.setWindowIcon(icon)
        self.web_view = QWebEngineView()
        self.centralWidget().layout().addWidget(self.web_view)
        self.web_view.titleChanged.connect(lambda title: self.setWindowTitle(title))

        self.profile = QWebEngineProfile(QApplication.instance().applicationName(), parent=self)
        self.profile.setHttpUserAgent(ua)
        self.page = MyWebPage(self.profile)
        self.page.setUrl(QUrl(url))
        self.web_view.setPage(self.page)
        setting = self.web_view.settings()
        setting.setAttribute(QWebEngineSettings.JavascriptCanOpenWindows, True)
        self.web_view.show()

        self._home_url = QUrl(home_url)
        self.actionHome.triggered.connect(lambda: self.page.setUrl(self._home_url))
        self.actionBack.triggered.connect(lambda: self.page.triggerAction(self.page.Back))
        self.actionNext.triggered.connect(lambda: self.page.triggerAction(self.page.Forward))
