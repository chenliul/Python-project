import math_func
import pytest
import base64

def test_add():
    assert math_func.add(7,3) == 10
    assert math_func.add(7) == 9
    assert math_func.add(5) == 7

def test_product():
    assert math_func.product(5,5) == 25
    assert math_func.product(5) == 10
    assert math_func.product(7) == 14

#@pytest.mark.skip(reason="do not run strings")
def test_add_strings():
    result = math_func.add('hello', ' world')
    assert result == 'hello world'
    assert type(result) is str
    assert 'hello' in result
