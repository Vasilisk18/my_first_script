import pytest
from src.conftest import first_try
from src.conftest import divide
def test_first():
    assert first_try(-10) == "zero or negative"
    assert first_try(1) == "positive"
def test_divide():
    assert divide(20,2) == 10