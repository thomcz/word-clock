import time
import threading

class StoppableThread(threading.Thread):
        def __init__(self, func, waitingTime):
                super(StoppableThread, self).__init__()
                self._stop_event = threading.Event()
                self.func = func
                self.waitingTime = waitingTime

        def stop(self):
                self._stop_event.set()

        def stopped(self):
                return self._stop_event.is_set()

        def run(self):
                while not self.stopped():
                        self.func()
                        time.sleep(self.waitingTime)

