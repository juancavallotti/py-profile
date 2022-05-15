from prftools import timed
from pytest import fixture
from io import StringIO
import logging

@fixture
def logging_output():

    str_io = StringIO()
    print("Logger output", file=str_io)
    handler = logging.StreamHandler(str_io)
    logging.basicConfig(level=logging.DEBUG, handlers=[handler])
    logger = logging.getLogger()
    logger.addHandler(handler)
    logger.setLevel(logging.DEBUG)
    yield str_io


def test_basic_timed(logging_output: StringIO):
    
    @timed
    def tester_function():
        logging.info("Hello world")
        return "world"
    
    ret = tester_function()

    #chech the various aspects of timed.
    assert ret == "world" #check it returns the right value.
    logging_output.flush()
    logs = logging_output.getvalue()
    assert "tester_function" in logs #the timed decorator should have logged something.

