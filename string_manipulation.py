def drop_character(str, character):
    # Removes all of a certain character from string
    list_var = str.split(character)
    str_var = ''
    for item in list_var:
        str_var += item
    return str_var