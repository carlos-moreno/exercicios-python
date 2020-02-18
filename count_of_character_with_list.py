def count_character(s: str):
    """
    Function for character count in the string
    :param s:

    Ex:
    >>> count_character('car')
    a: 1
    c: 1
    r: 1
    >>> count_character('passport')
    a: 1
    o: 1
    p: 2
    r: 1
    s: 2
    t: 1
    """

    character_sorted = sorted(s)
    previous_character = character_sorted[0]
    count = 1

    for character in character_sorted[1:]:
        if character == previous_character:
            count += 1
        else:
            print(f"{previous_character}: {count}")
            count = 1
            previous_character = character

    print(f"{previous_character}: {count}")


if __name__ == "__main__":
    count_character("car")
    print()
    count_character("passport")
