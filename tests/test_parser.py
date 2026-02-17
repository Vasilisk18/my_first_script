import pytest
from src.parser import get_status_code_from_response

def test_parser(mocker):
    mock_response = mocker.Mock()
    mock_response.status_code = 200
    get_status_code_from_response(mock_response)
    assert get_status_code_from_response(mock_response) == 200