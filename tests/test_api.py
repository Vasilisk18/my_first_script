import pytest
import requests
from src.api import get_data

def test_get_data(mocker):
    mocker.patch("src.api.requests.get",
                    side_effect = requests.exceptions.ConnectionError)
    with pytest.raises(requests.exceptions.RequestException):
        get_data()