import pytest
from src.Hello import printHello
def test_hello():
    assert printHello()=="hello Ayala"