from contextlib import contextmanager
import json
import pathlib

import appdirs
import typer
import typing as t
from PyQt6.QtGui import QIcon
from PyQt6.QtCore import QUrl
from PyQt6.QtWidgets import QApplication
from PyQt6.QtCore import QMargins

from webappinstaller import useragents, webwindow


@contextmanager
def session_cache(appname):
    cache = {}
    cache_dir = pathlib.Path(appdirs.user_cache_dir(appname))
    cache_path = cache_dir / "cache.json"

    if cache_path.exists():
        with open(cache_path) as file:
            cache |= json.load(file)

    yield cache

    with open(cache_path, "w") as file:
        json.dump(cache, file)


def setup_app(name: str, desktop_file: t.Optional[str], icon_name: t.Optional[str]):
    app = QApplication([name])
    app.setDesktopFileName(desktop_file)
    icon = QIcon.fromTheme(icon_name) or QIcon.fromTheme("internet-web-browser")
    app.setWindowIcon(icon)
    app.setDesktopFileName(name)
    return app


def centered_rectangle(screen):
    screen_size = screen.availableGeometry()
    x_margin = screen_size.width() // 6
    y_margin = screen_size.height() // 6
    return screen_size.marginsRemoved(QMargins(x_margin, y_margin, x_margin, y_margin))


def main(
    name,
    url,
    open_last_url: bool = False,
    icon_name: t.Optional[str] = None,
    desktop_file: t.Optional[str] = None,
    ua: str = "chrome",
    maximized: bool = False,
):
    app = setup_app(name, desktop_file, icon_name)

    with session_cache(name) as cache:
        home_url = url
        current_url = url

        if open_last_url and (last_url := cache.get("last_url")):
            current_url = last_url

        typer.echo(current_url)
        w = webwindow.WebWindow(
            url=current_url,
            home_url=home_url,
            icon=app.windowIcon(),
            ua=useragents.UA_STRINGS[ua],
        )

        def set_url(url: QUrl):
            cache["last_url"] = url.url()

        w.url_changed.connect(set_url)

        w.setGeometry(centered_rectangle(w.screen()))

        if maximized:
            w.showMaximized()
        else:
            w.show()

        return app.exec()


if __name__ == "__main__":
    typer.run(main)
