def print_upper_words(list, letters):
    for item in list:
        for letter in letters:
            if item.startswith(letter):
                if list.index(item) < len(list) - 1:
                    print(f'{item.upper()}')
                elif len(list) < 2:
                    print(f'{item.upper()}')
                else:
                    print(f'{item.upper()}')
def must_start_with(letters):
    word_match = []
    for letter in letters:
        word_match.append(letter.lower())
    return word_match
    
print_upper_words(['hello','hi','bye'],must_start_with(input('enter letters with no space: ')))
