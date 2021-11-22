import pytest

from homework4.task_3.task_3 import my_precious_logger


@pytest.mark.parametrize("text, expected_result",
                         [('error: file not found', 'error: file not found'),
                          ])
def test_my_precious_logger_stderr(capsys, text, expected_result):
    my_precious_logger(text)
    captured = capsys.readouterr()
    assert captured.err.strip() == expected_result


@pytest.mark.parametrize("text, expected_result",
                         [('OK', 'OK'),
                          ])
def test_my_precious_logger_stdout(capsys, text, expected_result):
    my_precious_logger(text)
    captured = capsys.readouterr()
    assert captured.out.strip() == expected_result
