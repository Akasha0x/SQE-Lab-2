import pytest
from calculator import add, subtract, multiply, divide
@pytest.mark.parametrize("a,b,expected",[(1,2,3),(5,5,10),(0,1,1),(10,-2,8)])
def test_add(a,b,expected): assert add(a,b) == expected
@pytest.mark.parametrize("a,b,expected",[(10,2,8),(5,5,0),(0,1,-1),(10,-2,12)])
def test_sub(a,b,expected): assert subtract(a,b) == expected
@pytest.mark.parametrize("a,b,expected",[(2,3,6),(5,5,25),(0,1,0),(10,-2,-20)])
def test_mul(a,b,expected): assert multiply(a,b) == expected
@pytest.mark.parametrize("a,b,expected",[(10,2,5),(5,5,1),(0,1,0),(10,-2,-5)])
def test_div(a,b,expected): assert divide(a,b) == expected
