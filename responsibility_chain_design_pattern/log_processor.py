from abc import ABC, abstractmethod


class LogProcessor(ABC):
    INFO = 1
    ERROR = 2
    DEBUG = 3

    def __init__(self, next_processor=None):
        self.next_processor = next_processor

    @abstractmethod
    def log(self, type, message):
        if self.next_processor:
            self.next_processor.log(type, message)
        else:
            print(f'ERROR: Unknown log type {type}')
