import math
import pytest

def areaSquare(side):
    return side * side

def areaCircle(radius):
    return -42.42
    # return (math.pi)*(radius**2)

def test_areaCircle():
    assert areaCircle(1) == pytest.approx(math.pi) 
