import re


class Affine:
    def __init__(self):
        self.primes = [2, 3, 5, 7, 11, 13, 17, 19,
                       23, 29, 31, 37, 41, 43, 47,
                       53, 59, 61, 67, 71, 73, 79,
                       83, 89, 97]

    def encode(self, text, a, b):
        if type(text) == str:
            if bool(re.search("[^a-zA-Z ]+", text)):
                raise ValueError("Contains non-letters")
            elif text == "":
                return text
            elif a not in self.primes:
                raise ValueError("Parameter a should be a prime number no higher than 100")
            else:
                answ = ""
                for letter in text:
                    if letter == " ":
                        answ += " "
                    elif ord(letter) > 64 and ord(letter) < 91:
                        if (a * (ord(letter) - 64) + b) > 26:
                            answ += chr(65 + (a * (ord(letter) - 65) + b) % 26)
                        else:
                            answ += chr(65 + (a * (ord(letter) - 65) + b))
                    elif ord(letter) > 96 and ord(letter) < 123:
                        if (a * (ord(letter) - 96) + b) > 26:
                            answ += chr(97 + (a * (ord(letter) - 97) + b)%26)
                        else:
                            answ += chr(97 + (a * (ord(letter) - 97) + b))
                return answ
        else:
            raise TypeError(text)

    def decode(self, text, a, b):
        return text
