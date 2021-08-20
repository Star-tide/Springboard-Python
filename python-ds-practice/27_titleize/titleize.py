def titleize(phrase):
    """Return phrase in title case (each word capitalized).

        >>> titleize('this is awesome')
        'This Is Awesome'

        >>> titleize('oNLy cAPITALIZe fIRSt')
        'Only Capitalize First'
    """
    _phrase = ''
    split = phrase.split(' ')
    for word in split:
        _phrase += word.capitalize() + ' '
    print(_phrase)