import pytest
from src.main import main
def test_main():
    assert main()==9*7+"hello World"