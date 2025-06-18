import pytest
from calculator import square


def main():
    test_square_positive()
    test_square_negative()
    test_square_zero()
def test_square_positive():
    assert square(2) == 4
    assert square(3) == 9

def test_square_negative():
    assert square(-2) == 4
    assert square(-3) == 9

def test_square_zero():
    assert square(0) == 0

def test_str():
	with pytest.raises(TypeError):
            square("cat")

if __name__ == "__main__":
    main()