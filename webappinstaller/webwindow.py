import webbrowser

from PyQt6.QtCore import QUrl, pyqtSlot, pyqtSignal
from PyQt6.QtGui import QIcon
from PyQt6.QtWebEngineWidgets import QWebEngineView
from PyQt6.QtWebEngineCore import QWebEnginePage, QWebEngineProfile, QWebEngineSettings
from PyQt6.QtWidgets import QApplication, QMainWindow

from . import ui_webwindow


class NewPageHandler(QWebEnginePage):
    def __init__(self, parent=None) -> None:
        super().__init__(parent)

    def acceptNavigationRequest(self, url, *_):
        webbrowser.open(url.toString())
        self.setParent(None)
        return False


class MyWebPage(QWebEnginePage):
    def __init__(self, appname: str, ua: str, parent=None) -> None:
        profile = QWebEngineProfile(appname)
        profile.setHttpUserAgent(ua)
        super().__init__(profile, parent)
        profile.setParent(self)

    def createWindow(self, t: QWebEnginePage.WebWindowType):
        return NewPageHandler(self)


class WebWindow(QMainWindow, ui_webwindow.Ui_WebWindow):
    url_changed = pyqtSignal(QUrl)

    def __init__(self, url: str, home_url: str, icon: QIcon, ua: str):
        super().__init__()
        self.home_url = QUrl(home_url)
        self.web_view = QWebEngineView()
        self.page = MyWebPage(QApplication.instance().applicationName(), ua)

        self._setup_ui(icon)
        self._setup_events()
        self._setup_webview()
        self.page.setUrl(QUrl(url))
        self.web_view.show()

    def _setup_webview(self):
        setting = self.web_view.settings()
        setting.setAttribute(
            QWebEngineSettings.WebAttribute.JavascriptCanOpenWindows, True
        )

    def _setup_ui(self, icon: QIcon):
        self.setupUi(self)
        self.setWindowIcon(icon)
        self.centralWidget().layout().addWidget(self.web_view)
        self.web_view.setPage(self.page)

    def _setup_events(self):
        self.actionHome.triggered.connect(self.action_home_triggered)
        self.actionBack.triggered.connect(self.action_back_triggered)
        self.actionNext.triggered.connect(self.action_forward_triggered)
        self.web_view.titleChanged.connect(lambda title: self.setWindowTitle(title))
        self.web_view.urlChanged.connect(self.url_changed)

    @pyqtSlot()
    def action_home_triggered(self):
        self.page.setUrl(self.home_url)

    @pyqtSlot()
    def action_back_triggered(self):
        self.page.triggerAction(QWebEnginePage.WebAction.Back)

    @pyqtSlot()
    def action_forward_triggered(self):
        self.page.triggerAction(QWebEnginePage.WebAction.Forward)
