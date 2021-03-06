import requests
import string
import random


def get_names():
    url = 'https://uinames.com/api/'
    response = requests.get(url).json()

    name = response['name']
    surname = response['surname']

    for char in (name+surname):
        if char not in string.ascii_letters:
            name, surname = get_names()
            return name, surname

    return name, surname


def create_username():

    first_name, last_name = get_names()

    op = random.choice(range(4))

    if op == 0:
        return number_last(first_name, last_name)
    if op == 1:
        return number_mid(first_name, last_name)
    if op == 2:
        return first_name_number(first_name)
    if op == 3:
        return last_name_number(last_name)


def last_name_number(last_name):

    username = ''
    n = random.choice(range(1, 4))
    username += last_name
    username += ''.join(random.choice(string.digits) for _ in range(n))

    return username.replace(' ', '')


def first_name_number(first_name):

    username = ''
    n = random.choice(range(1, 4))
    username += first_name
    username += ''.join(random.choice(string.digits) for _ in range(n))

    return username.replace(' ', '')


def number_last(first_name, last_name):

    username = ''
    n = random.choice(range(1, 4))
    username += first_name[0].lower()
    username += last_name
    username += ''.join(random.choice(string.digits) for _ in range(n))

    return username.replace(' ', '')


def number_mid(first_name, last_name):

    username = ''
    n = random.choice(range(1, 4))
    username += first_name
    username += ''.join(random.choice(string.digits) for _ in range(n))
    username += last_name

    return username.replace(' ', '')
