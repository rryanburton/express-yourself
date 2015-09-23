import re


def binary(num):
    return re.match(r'[01+]', num)


def binary_even(num):
    return re.match(r'[01+]*0$', num)


def hex(string):
    return re.match(r'[0-9ABCDEF][^G-Z]', string)


def word(string):
    return re.match(r'^[\w-]*[a-z-]+$', string)


def words(string, count=None):
    if count:
        pass
    else:
        return word(string)


def phone_number(string):
    return re.match(r'[\(\d{3}\)\s\d{3}\-\d{4}]', string)


def money():
    pass


def zipcode(num):
    return re.match(r'[\d{5}\-*\d{4}]', num)


def date(num):
    return re.match(r'(\d+[/-]\d+[/-]\d+)', num)
