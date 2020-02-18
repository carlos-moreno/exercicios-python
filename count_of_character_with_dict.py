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

    character_sorted = sorted(s)
    previous_character = character_sorted[0]
    count = 1

    result = {}

    for character in character_sorted[1:]:
        if character == previous_character:
            count += 1
        else:
            result[previous_character] = count
            count = 1
            previous_character = character

    result[previous_character] = count

    return result


if __name__ == "__main__":
    print(count_character("car"))
    print()
    print(count_character("passport"))
