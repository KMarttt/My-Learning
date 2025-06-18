from bank import value

def main():
    pass

def test_value_startswith_hello():
    assert value("Hello there") == 0
    assert value("Hello man, don't be cold") == 0
    assert value("Hello, I was wondering") == 0
    assert value("Hello!!!!") == 0

def test_value_startswith_h():
    assert value("Hey, I was amazed") == 20
    assert value("Happy day!") == 20
    assert value("Hip-hip hello") == 20
    assert value("Hiyyyaaa") == 20

def test_value_notstarting_h_or_hello():
    assert value("Please die") == 100
    assert value("stappp") == 100
    assert value("shut up") == 100
    assert value("Go to H#%&") == 100




if __name__ == "__main__":
    main()
