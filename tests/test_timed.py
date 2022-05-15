from prftools import timed
from pytest import fixture
from io import StringIO
import logging

@fixture
def logging_output():

    str_io = StringIO()
    logging.basicConfig(stream=str_io, level=logging.INFO)
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

