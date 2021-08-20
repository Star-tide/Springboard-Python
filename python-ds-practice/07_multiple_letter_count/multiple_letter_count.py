def multiple_letter_count(phrase):
    """Return dict of {ltr: frequency} from phrase.

        >>> multiple_letter_count('yay')
        {'y': 2, 'a': 1}

        >>> multiple_letter_count('Yay')
        {'Y': 1, 'a': 1, 'y': 1}
    """
    my_dict = {}
    for letter in phrase:
        if letter in my_dict:
            my_dict[letter] += 1
        else:
            my_dict[letter] = 1
    print(my_dict)
