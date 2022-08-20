from core.utils import clear
from importlib import import_module


class CallBack:
    """
        ...
    """
    def __init__(self, package, function, *args, **kwargs):
        self.function = getattr(import_module(package), function)
        self.args = args
        self.kwargs = kwargs

    def call(self):
        self.function(*self.args, **self.kwargs)


class Route:
    """
        ...
    """
    def __init__(self, name, description=None, callback: CallBack = None, children=()) -> None:
        self.name = name
        self.description = description
        self.callback = callback
        ...
        if not callback: self.children = children


class Router:
    """
        ...
    """
    def __init__(self, name, route):
        self.name = name
        self.route = route

    def generate(self) -> None:
        clear()
        ...
