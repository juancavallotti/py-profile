import time
import logging as logger


#%% decorator to log the time taken on various activitites.
def timed(func):
    def wrapper(*args, **kwargs):
        ret = None
        try:
            logger.info(f"Timing function {func.__qualname__}")
            initTime = time.time()
            ret = func(*args, **kwargs)
            return ret
        except BaseException:
            logger.error("Something went really wrong")
            raise
        finally:
            endTime = time.time()
            totalTimeInMilis = round((endTime - initTime) * 1000)
            logger.info(f"Function call ({func.__qualname__}) took {totalTimeInMilis} ms")
    
    return wrapper