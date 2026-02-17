import pytest
from src.logger import log_message
import logging

def test_logger(mocker):
    mocker.patch("src.logger.logging.info")
    mock_log = mocker.patch("src.logger.logging.info")
    log_message("hello")
    mock_log.assert_called_once_with("hello")
