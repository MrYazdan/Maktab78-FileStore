from core.utils import clear
from importlib import import_module


class Config:
    parent = None


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
        # ...
        self.children = None
        if not callback: self.children = children

    def run(self):
        # ...

        clear()
        print(self.name)
        print(self.description or "\n")

        if children := self.children:

            Config.parent = self

            for child in children:
                child: Route
                print(f"{children.index(child) + 1}. {child.name}")

            index = int(input("\n>> ")) - 1
            # ...

            children[index]: Route
            children[index].run()

        else:
            # ...
            self.callback: CallBack
            self.callback.call()

        if Config.parent:
            input("Press enter to back menu")
            Config.parent.run()


class Router:
    """
        ...
    """

    def __init__(self, name: str, route: Route) -> None:
        self.name = name
        self.route = route

    def generate(self) -> None:
        clear()
        Config.parent = self.route
        self.route.run()
        # ...
