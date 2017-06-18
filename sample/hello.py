"""Place holder until I make a repository worth maintaining"""


def letter_print(string):
    """prints each letter of a string on a different line
    Parameters string: string input to the function
    Use: letter_print([any string])
    Return nothing"""

    if isinstance(string, str):
        print('This is not a string, GTFO')
        return False

    for letter in string:
        print(letter)

    return True
