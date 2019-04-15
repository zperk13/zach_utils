def drop_character(str, character):
    # Removes all of a certain character from string
    return str.replace(character, '')


def no_double_lines(string):
    while True:
        if '\n\n' in string:
            string = string.replace('\n\n', '\n')
            print(string.count('\n'))
        else:
            return string
