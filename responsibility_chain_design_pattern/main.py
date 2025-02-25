"""
In Chain of Responsibility pattern, a request is sent to a chain of handlers.
Each handler decides either to process the request or to pass it to the next handler in the chain.
Applications:
1. ATM
2. Logging
3. Vending Machine

Source: https://gitlab.com/shrayansh8/interviewcodingpractise
"""

from log_processor import LogProcessor
from info_log_processor import InfoLogProcessor
from debug_log_processor import DebugLogProcessor
from error_log_processor import ErrorLogProcessor


if __name__ == '__main__':

    logger = InfoLogProcessor(DebugLogProcessor(ErrorLogProcessor()))

    # error_logger = ErrorLogProcessor()
    # debug_logger = DebugLogProcessor(error_logger)
    # info_logger = InfoLogProcessor(debug_logger)
    
    logger.log(LogProcessor.INFO, 'This is an information message')
    logger.log(LogProcessor.DEBUG, 'This is a debug message')
    logger.log(LogProcessor.ERROR, 'This is an error message')
