from asyncio.log import logger
import time
import logging


#this allows turning profile messages on and off.
logger = logging.getLogger("py-profile")

#%% decorator to log the time taken on various activitites.
def timed(*parg ,desc=None, append_name=False, append_template = "{} - {}"):
    def timed_inner(func):
        
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

    if len(parg) == 1:
        return timed_inner(parg[0])
    else:
        return timed_inner