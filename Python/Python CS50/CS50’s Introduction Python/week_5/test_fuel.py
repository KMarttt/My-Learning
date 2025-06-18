import pytest
from fuel import convert, gauge

def main():
    pass

# note, when there are many value to return, you should put then in a parenthesis () separated by (,)

def test_convert_num():
    assert convert("1/4") == (25, 1, 4)
    assert convert("2/4") == (50, 2, 4)
    assert convert("3/4") == (75, 3, 4)
    assert convert("4/4") == (100, 4, 4)

# the code below are used when you exit a program using sys.exit
# instead of raising an error, you raise the SystemExit
# then name that (ex. wrong)
# then you can assert the ending message of the SystemExit using the var name
# -- var name should be in a str if the ending message is a str ... ex: str(wrong.value)
# which should be "Wrong value"


def test_convert_str():
    with pytest.raises(SystemExit) as wrong:
        convert("cat")
    with pytest.raises(SystemExit) as wrong:
        convert("dog")
    with pytest.raises(SystemExit) as wrong:
        convert("rat")
    with pytest.raises(SystemExit) as wrong:
        convert("bird")
    assert str(wrong.value) == "Wrong Value"


def test_gauge():
    assert gauge(1, 1, 100) == "E"
    assert gauge(25, 1, 4) =="25%"
    assert gauge(50, 2, 4) == "50%"
    assert gauge(75, 3, 4) == "75%"
    assert gauge(100, 4, 4) == "F"
    with pytest.raises(SystemExit) as wrong:
        gauge(25, 4, 1)
    assert str(wrong.value) == "Wrong Value"

if __name__ == "__main__":
    main()