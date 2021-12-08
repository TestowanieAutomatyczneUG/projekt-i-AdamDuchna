import re
import doctest


class Affine:
    def __init__(self):
        self.primes = [2, 3, 5, 7, 11, 13, 17, 19,
                       23, 29, 31, 37, 41, 43, 47,
                       53, 59, 61, 67, 71, 73, 79,
                       83, 89, 97]

    def encode(self, text, a, b):
        """
        Given a text and 2 values, return an affine encoded text or an error.

        :param text: str
        :param a: int
        :param b: int
        :return: str,ValueError,TypeError

        >>> t.encode("AFF ! 64",7,4)
        Traceback (most recent call last):
        ...
        ValueError: Contains non-letters
        >>> t.encode("1956 annO DOMINi",9,1)
        Traceback (most recent call last):
        ...
        ValueError: Contains non-letters
        >>> t.encode("desTT aeiou",11,1)
        'itrCC btlzn'
        >>> t.encode(["ks",1,4,True],3,6)
        Traceback (most recent call last):
        ...
        TypeError: ['ks', 1, 4, True]
        >>> t.encode("piesek",4,6)
        Traceback (most recent call last):
        ...
        ValueError: Parameter a should be a prime number no higher than 97


        """
        if str == type(text):
            if bool(re.search("[^a-zA-Z ]+", text)):
                raise ValueError("Contains non-letters")
            elif text == "":
                return text
            elif a not in self.primes:
                raise ValueError("Parameter a should be a prime number no higher than 97")
            else:
                answ = ""
                for letter in text:
                    if letter == " ":
                        answ += " "
                    elif 64 < ord(letter) < 91:
                        if (a * (ord(letter) - 64) + b) > 26:
                            answ += chr(65 + (a * (ord(letter) - 65) + b) % 26)
                        else:
                            answ += chr(65 + (a * (ord(letter) - 65) + b))
                    elif 96 < ord(letter) < 123:
                        if (a * (ord(letter) - 96) + b) > 26:
                            answ += chr(97 + (a * (ord(letter) - 97) + b) % 26)
                        else:
                            answ += chr(97 + (a * (ord(letter) - 97) + b))
                return answ
        else:
            raise TypeError(text)

    def decode(self, text, a, b):
        return chr(65 + ((ord(text) - 65 - b) // a))


if __name__ == '__main__':
    doctest.testmod(extraglobs={'t': Affine()})
