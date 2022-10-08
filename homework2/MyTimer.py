
import string
import time

class MyTimer:
    def __init__(self, units: string):
        self.units = units
        self.start_time = None
        self.spend_time = None

    def start(self):
        self.start_time = time.perf_counter()
        return self

    def stop(self):
        self.spend_time = time.perf_counter() - self.start_time
        self.start_time = None

    def __enter__(self):
        self.start()
        return self

    def __exit__(self, *exc_info):
        self.stop()

    def elapsed_time(self):
        if self.units == "m":
            self.spend_time = self.spend_time / 60
        elif self.units == "h":
            self.spend_time = self.spend_time / 3600
        return self.spend_time

