from string import ascii_letters


def encrypt(inp_string, key):
    result = ""
    lower = ascii_letters.lower()[:26]
    upper = ascii_letters.upper()[:26]
    for char in inp_string:
        if char not in ascii_letters:
            result += char
        elif char in ascii_letters.lower():
            new_char = (lower.index(char) + key) % len(lower)
            result += lower[new_char]
        else:
            new_char = (upper.index(char) + key) % len(upper)
            result += upper[new_char]

    return result


def decrypt(inp_string, key):
    key *= -1
    return encrypt(inp_string, key)


def brute_force(inp_string):
    result = ""
    brute_force_data = {}
    key = -26

    while key <= 26:
        result = decrypt(inp_string, key)
        brute_force_data[key] = result
        key += 1

    return brute_force_data

