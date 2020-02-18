def count_character(s: str):
    """
    Function for character count in the string
    :param s:

    Ex:
    >>> count_character('car')
    {'a': 1, 'c': 1, 'r': 1}
    >>> count_character('passport')
    {'a': 1, 'o': 1, 'p': 2, 'r': 1, 's': 2, 't': 1}
    """

    result = {}

    for character in s:
        result[character] = result.get(character, 0) + 1

    return result


if __name__ == "__main__":
    print(count_character("car"))
    print()
    print(count_character("passport"))
