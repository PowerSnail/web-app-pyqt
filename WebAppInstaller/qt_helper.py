import functools
from typing import Any, Dict

import fire
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtWidgets import QAction, QApplication, QWidget

_qt_enum_types: Dict[Any, Any] = {}


def enum_type(const, namespace=Qt) -> str:
    # Lazy Init
    if namespace not in _qt_enum_types:
        _qt_enum_types[namespace] = True

        for obj in vars(namespace).values():
            if type(obj).__name__ == "enumtype":
                _qt_enum_types[obj] = {}
        for name, obj in vars(namespace).items():
            class_ = type(obj)
            if class_ in _qt_enum_types:
                _qt_enum_types[class_][obj] = name

    return _qt_enum_types[type(const)][const]


def print_children_widget(filename: str):
    from PyQt5 import uic

    app = QApplication([])
    ui = uic.loadUi(filename)
    for name, obj in vars(ui).items():
        if isinstance(obj, (QWidget, QAction)):
            print(f"{name}: {type(obj).__name__}")


def run_async(func, *args):
    QTimer.singleShot(0, functools.partial(func, *args))


def compile_uis(dir: str = None):
    import pathlib
    import subprocess as sp

    if dir is None:
        dir = pathlib.Path(__file__).parent

    ui_files = pathlib.Path(dir).rglob("*.ui")
    failed = []
    for ui_file in ui_files:
        out_filename = ui_file.with_name("ui_" + ui_file.name).with_suffix(".py")
        result = sp.run(["pyuic5", str(ui_file), "-o", str(out_filename)])
        if result.returncode != 0:
            failed.append(ui_file)

    if failed:
        print("The following files have failed.")
        print("\n".join(str(f) for f in failed))
    else:
        print("Success")


def compile_resource(resource_file=None, output_file=None):
    import pathlib
    import subprocess as sp

    if resource_file is None:
        resource_file = pathlib.Path(__file__).parent.parent / "res" / "res.qrc"
    if output_file is None:
        output_file = pathlib.Path(__file__).parent / "resource.py"

    result = sp.run(["pyrcc5", str(resource_file), "-o", str(output_file)])
    if result.returncode != 0:
        print("Failed")
    else:
        print("Success")


if __name__ == "__main__":
    fire.Fire(
        {"print-children-widget": print_children_widget, "compile_uis": compile_uis}
    )
