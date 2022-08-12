import threading
from typing import Callable, Dict, List


class Timer:

    def __init__(self, time: float, function: Callable = None, args: List = [], kwargs: Dict = {}):
        self._time = time
        self._function = function
        self._args = args
        self._kwargs = kwargs
        self.__set()
        self._running = False

    def __set(self):
        self._timer = threading.Timer(
            self._time,
            self._function,
            self._args,
            self._kwargs)

    def start(self):
        self._running = True
        self._timer.start()

    def cancel(self):
        self._running = False
        self._timer.cancel()

    def reset(self, start=False):
        if self._running:
            self._timer.cancel()

        self._set()

        if self._running or start:
            self.start()

    def running(self) -> bool:
        return self._running;
