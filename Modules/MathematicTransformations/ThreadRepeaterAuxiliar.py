from threading import Thread

class ThreadRepeater(Thread):
    def __init__(self, event):
        Thread.__init__(self)
        self.stopped = event

    def run(self):
        while not self.finished.wait(self.interval):
            self.function(*self.args, **self.kwargs)
