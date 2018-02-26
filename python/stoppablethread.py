from time import sleep
from threading import Thread
from threading import Event

class StoppableThread(Thread):
    def __init__(self, func, waitingTime, isLoop):
        super(StoppableThread, self).__init__()
        self._stop_event = Event()
        self.func = func
        self.waitingTime = waitingTime
        self.isLoop = isLoop

    def stop(self):
        self._stop_event.set()

    def stopped(self):
        return self._stop_event.is_set()

    def run(self):
        while not self.stopped():
            self.func()
            if not self.isLoop:
                self.stop
                break
            sleep(self.waitingTime)

