def flip_case(phrase, to_swap):
    """Flip [to_swap] case each time it appears in phrase.

        >>> flip_case('Aaaahhh', 'a')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'A')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'h')
        'AaaaHHH'

    """
    lower = to_swap.lower()
    swap_case = ''
    for letter in phrase:
        if letter.lower() == lower:
            letter = letter.swapcase()
        swap_case+= letter
    print(swap_case) 