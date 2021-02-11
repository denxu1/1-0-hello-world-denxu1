import pytest
import exercise

def test_case(capsys):
  
    input_values = []
    result = 'Hello, world!\n'

    exercise.input = lambda prompt: input_values.pop(0)
  
    exercise.main()

    out, err = capsys.readouterr()

    assert out == result, f'for input(s) of {input_values}, the output should be {result} instead of your {out}'
    assert err == ''
