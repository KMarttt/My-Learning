from vanity_plates import is_valid

def main():
    pass


def test_is_valid__req_two_letter_start():
    assert is_valid("AB") == "Valid"
    assert is_valid("ABC123") == "Valid"
    assert is_valid("ABCDE") == "Valid"
    assert is_valid("KIER12") == "Valid"


def test_is_valid__req_max_char():
    assert is_valid("CHAR5") == "Valid"
    assert is_valid("MAXIS6") == "Valid"
    assert is_valid("ISREQ1") == "Valid"
    assert is_valid("ABCDE") == "Valid"


def test_is_valid__req_digit():
    assert is_valid("CHAR12") == "Valid"
    assert is_valid("MAXIS6") == "Valid"
    assert is_valid("ISREQ1") == "Valid"
    assert is_valid("ABCDEF") == "Valid"


def test_is_valid__req_no_punctuation():
    assert is_valid("CHAR12") == "Valid"
    assert is_valid("MAXIS6") == "Valid"
    assert is_valid("ISREQ1") == "Valid"
    assert is_valid("ABCDEF") == "Valid"


if __name__ == "__main__":
    main()