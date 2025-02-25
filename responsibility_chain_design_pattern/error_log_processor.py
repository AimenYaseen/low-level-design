from log_processor import LogProcessor


class ErrorLogProcessor(LogProcessor):
    def __init__(self, next_processor=None):
        super().__init__(next_processor)

    def log(self, type, message):
        if type == self.ERROR:
            print(f'ERROR: {message}')
        elif self.next_processor:
            self.next_processor.log(type, message)
