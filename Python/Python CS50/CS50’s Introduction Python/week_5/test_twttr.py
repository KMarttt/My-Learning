from twttr import shorten

def main():
    test_shorten_lower_vowel()
    test_shorten_upper_vowel()


def test_shorten_lower_vowel():
    assert shorten("Marti") == "Mrt"
    assert shorten("Kier") == "Kr"
    assert shorten("Vicente") == "Vcnt"
    assert shorten("Trance") == "Trnc"


def test_shorten_upper_vowel():
    assert shorten("Angelo") == "ngl"
    assert shorten("Emily") == "mly"
    assert shorten("Obito") == "bt"
    assert shorten("Umika") == "mk"


if __name__ == "__main__":
    main()