from loguru import logger
from sys import stderr
from functools import wraps
import time

logger.remove()
# logger.add('This is if i want to create a file to save my logs')
# logger.add('filename.log')
# EXAMPLE
#logger.add('log_messages.log')

# log file for filtering

# logger.add('critical_logs.log', level='CRITICAL') # EXAMPLE for critical logs filtering

# Examples the log configuration

logger.add(
           sink=stderr,
           format="{time} <r>{level}</r> <g>{message}</g> {file}",
           level='INFO'
           )

logger.add('error_logs.log',
           format="{time} {level} {message} {file}",
           level='INFO'
           )

# # Logs
# logger.debug('When you want to leave something to the dev in the future.')
# logger.info('Important information')
# logger.warning('A message that something might stop working in the future.')
# logger.error('Something happened.')
# logger.critical('Something stopped the application.')


def log_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        logger.info(f'Calling definition "{func.__name__}" with args {args} and kwargs {kwargs}')
        try:
            result = func(*args, **kwargs)
            logger.info(f'Definition "{func.__name__}" returned {result}')
            return result
        except Exception as ex:
            logger.exception(f'Exception caught on "{func.__name__}": {ex}')
            raise # This relaunch the function to not alter the def behavior
    return wrapper

def time_measure_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        logger.info(f'Definition "{func.__name__}" executed in {end_time - start_time} ')
        return result
    return wrapper
        
    