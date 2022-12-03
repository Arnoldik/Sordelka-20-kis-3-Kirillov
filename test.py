import pytest
def reverse(s):
    if type(s) != str:
        raise TypeError('вот блин'.format(type(s)))

    return s [::-1]
