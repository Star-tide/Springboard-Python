def single_letter_count(word, letter):
    """How many times does letter appear in word (case-insensitively)?
    
        >>> single_letter_count('Hello World', 'h')
        1
        
        >>> single_letter_count('Hello World', 'z')
        0
        
        >>> single_letter_count("Hello World", 'l')
        3
    """
    lower_word = word.lower()
    lower_letter = letter.lower()
    letter_count = 0
    for letters in lower_word:
        if lower_letter == letters:
            letter_count += 1
    print(letter_count)
