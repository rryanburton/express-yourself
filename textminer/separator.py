import re

def words(string, count):
    return re.split(r'\s+', string)
    '''
    takes a single or multi word string and
    splits it into a list of single words:
    ['hello', 'world']
    '''
    pass

def phone_number(input):
    '''
    takes a 10 digit number and breaks it down to:
     {"area_code": "919", "number": "555-1212"}

    '''

    return re.match(r'{^\(?\d{3}\)?[. -]?\d{3}[-.]?\d{4}$}', input)
