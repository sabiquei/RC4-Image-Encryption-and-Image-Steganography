def initial_perm(s, u):
    """ Initial permutation of array S using array U. """
    j = 0
    for i in range(256):
        j = (j + s[i] + u[i]) % 256
        s[i], s[j] = s[j], s[i]
    return s


def prga(s):
    """
    Pseudo Random Generation Algorithm

    :param s: Permuted S Array
    :return: random int value ranging from 0 - 255
    """
    i = 0
    j = 0
    while True:
        i = (i + 1) % 256
        j = (j + s[i]) % 256
        s[i], s[j] = s[j], s[i]
        t = s[(s[i] + s[j]) % 256]
        yield t


def rc4(s, u):
    s = initial_perm(s, u)
    return prga(s)