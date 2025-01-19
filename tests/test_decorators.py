import os

from src.decorators import log


def test_log_console(capsys):
    @log()
    def square(x):
        return x * x

    square(3)
    result_ok = capsys.readouterr()
    assert result_ok.out == 'square ok\n'
    square('3')
    result_not_ok = capsys.readouterr()
    assert result_not_ok.out == "square error: can't multiply sequence by non-int of type 'str'. Inputs: (('3',), {})\n"


def test_log_file():
    @log('test_log.txt')
    def square(x):
        return x * x

    square(3)
    with open('test_log.txt', 'r', encoding='utf-8') as f:
        result_ok = f.read()
        assert result_ok == 'square ok'
    square('3')
    with open('test_log.txt', 'r', encoding='utf-8') as f:
        result_not_ok = f.read()
        assert result_not_ok == "square error: can't multiply sequence by non-int of type 'str'. Inputs: (('3',), {})"
    os.remove('test_log.txt')
