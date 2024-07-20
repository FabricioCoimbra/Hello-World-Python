import pytest
import hello

def test_hello():
    hello.say_hello()
    assert True == True