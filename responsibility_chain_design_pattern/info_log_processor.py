from log_processor import LogProcessor


class InfoLogProcessor(LogProcessor):
    def __init__(self, next_processor=None):
        super().__init__(next_processor)

    def log(self, type, message):
        if type == self.INFO:
            print(f'INFO: {message}')
        elif self.next_processor:
            self.next_processor.log(type, message)
