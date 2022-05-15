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
    logs = logging_output.getvalue()
    assert "tester_function" in logs #the timed decorator should have logged something.


def test_description_timed(logging_output: StringIO):
    
    description = "Some Function"
    @timed(desc=description)
    def tester_function():
        logging.info("Hello world")
        return "world"
    
    ret = tester_function()

    #chech the various aspects of timed.
    assert ret == "world" #check it returns the right value.
    logs = logging_output.getvalue()
    assert description in logs #the timed decorator should have logged something.
    assert not "tester_function" in logs

def test_formatted_timed(logging_output: StringIO):
    
    description = "Some Function"
    @timed(desc=description, append_name=True)
    def tester_function():
        logging.info("Hello world")
        return "world"
    
    ret = tester_function()

    #chech the various aspects of timed.
    assert ret == "world" #check it returns the right value.
    logs = logging_output.getvalue()
    assert description in logs #the timed decorator should have logged something.
    assert "tester_function" in logs
