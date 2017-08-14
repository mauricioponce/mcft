from functools import wraps
import logging

def log_ts(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        logging.debug('doing %s %s', f.__name__, args)
        res = f(*args, **kwargs)
        logging.debug('leaving %s with %s', f.__name__, res)
        return res
    return decorated_function
