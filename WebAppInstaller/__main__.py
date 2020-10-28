import fire
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication

from . import main_window, webwindow
import json
import pathlib
import appdirs


def config():
    app = QApplication(["WebAppInstaller"])
    w = main_window.MainWindow()
    w.show()
    return app.exec()


def _get_cache(appname):
    cache_dir = pathlib.Path(appdirs.user_cache_dir(appname))
    cache_path = cache_dir / "cache.json"
    if not cache_path.exists():
        return {}
    else:
        with open(cache_path) as file:
            return json.load(file)


def _save_cache(appname, **kwargs):
    cache_dir = pathlib.Path(appdirs.user_cache_dir(appname))
    cache_dir.mkdir(parents=True, exist_ok=True)
    
    cache_path = cache_dir / "cache.json"
    with open(cache_path, "w") as file:
        json.dump(kwargs, file)


def app(name, url, open_last_url=False, icon_name=None, desktop_file=None):
    app = QApplication([name])
    cache = _get_cache(name)

    icon = QIcon.fromTheme(icon_name)
    if not icon:
        icon = QIcon.fromTheme("internet-web-browser")
    app.setWindowIcon(icon)
    app.setDesktopFileName(name)
    
    w = webwindow.WebWindow(url=cache.get("last_url", url), home_url=url, icon=icon)
    w.show()
    result = app.exec()

    _save_cache(name, last_url=w.page.url().toString())


fire.Fire()
