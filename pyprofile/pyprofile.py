import time
import logging as logger


#%% decorator to log the time taken on various activitites.
def timed(func, desc=None, append_name=False, append_template = "{} - {}"):
    
    fn_name = desc if desc else func.__qualname__
    
    if append_name:
        fn_name = append_template.format(fn_name, func.__qualname__)

    def wrapper(*args, **kwargs):
        ret = None
        try:
            logger.info(f"Timing function {fn_name}")
            initTime = time.time()
            ret = func(*args, **kwargs)
            return ret
        except BaseException:
            logger.error("Something went really wrong")
            raise
        finally:
            endTime = time.time()
            totalTimeInMilis = round((endTime - initTime) * 1000)
            logger.info(f"Function call ({fn_name}) took {totalTimeInMilis} ms")
    
    return wrapper