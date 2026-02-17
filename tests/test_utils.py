import random
import pytest
from src.utils import get_random_number
def test_random_number(mocker):
    mocker.patch("src.utils.random.randint", return_value=42)
    assert get_random_number() == 42
