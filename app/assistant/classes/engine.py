from threading import Lock
from typing import Any

from .timeline import Timeline


class EngineMeta(type):
    _instances = {}
    _lock: Lock = Lock()

    def __call__(cls, *args: Any, **kwargs: Any) -> Any:
        with cls._lock:
            if cls not in cls._instances:
                instance = super().__call__(*args, **kwargs)
                cls._instances[cls] = instance
        return cls._instances[cls]


class Engine(metaclass=EngineMeta):
    def __init__(self) -> None:
        self.timelines = []

    def createTimeline(self):
        self.timelines.append(Timeline())

    def getTimeline(self, index) -> Timeline:
        if len(self.timelines) <= index:
            return None

        return self.timelines[index]


def get_engine() -> Engine:
    return Engine()
