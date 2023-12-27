import io
import os
import pytest
from unittest.mock import patch, call
from project import single_print, fake_norad, access_denied
import re


def test_single_print():
    # Redirect stdout for testing
    with patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
        printed_string = single_print("hello", 0.1, output_stream=mock_stdout)

    # Check the printed content
    captured = mock_stdout.getvalue()

    # Create a pattern to match the expected output, including bell characters
    expected_pattern = re.compile(
        r'h(\x07|\\a)?e(\x07|\\a)?l(\x07|\\a)?l(\x07|\\a)?o(\x07|\\a)?')

    # Assert that the pattern is found within the captured content
    assert expected_pattern.search(captured)

    # Check the returned value
    assert printed_string == "hello"


def test_fake_norad():
    with patch('sys.stdout', new_callable=io.StringIO):
        with patch('os.system') as mock_system:
            with patch('project.single_print') as mock_single_print:
                fake_norad()

    # Check the system clear calls
    mock_system.assert_has_calls([call('clear')] * 3)

    # Check the calls to single_print
    expected_calls = [
        call('jmnsZJrExk6f8xSaRCbuQl9vcT85K5YQs2rCYIRN0194KtIO1hXEMqcWtPwpSbPq', 0.02),
        call('wSRq1wztrXkoslH03h7Y139KVib4VRMHRmoEywKbi23JqOUmR5cXRz5n28HoAvdIIGtWxbs4BaBy4cWwWKUxCjtdKACxg11lZlP8iYe4QxKIgl18fzUz6jiVlNJLDvIgZCA2EG8rUqcWdpi82', 0.01),
        call('▒▒▒▒9vcT85▒▒▒  ▒03h7Y1▒▒▒ ▒▒▒▒▒▒▒ ▒▒▒▒▒▒KtIO1h▒▒▒ 867-5309 ▒▒▒▒▒ ▒▒▒▒▒▒aBy4c▒▒▒▒ ▒▒▒▒▒▒▒▒', 0.02),
    ]
    mock_single_print.assert_has_calls(expected_calls)


def test_access_denied():
    with patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
        with patch('os.system') as mock_system:
            with patch('time.sleep') as mock_sleep:
                access_denied()

    # Check the printed content
    captured = mock_stdout.getvalue()

    # Check the system calls
    mock_system.assert_called_once_with('clear')

    # Check the calls to time.sleep
    mock_sleep.assert_called_once_with(2)

    # Define the expected output
    expected_output = (
        '\n'*5 +
        '           ** IDENTIFICATION NOT RECOGNIZED **\n' +
        '                   ** ACCESS DENIED **\n'
    )

    # Update the assertion based on the actual output
    assert expected_output in captured
