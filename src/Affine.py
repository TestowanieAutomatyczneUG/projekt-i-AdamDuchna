import re

class Affine:
    def encode(self,text,a,b):
        if type(text) == str:
            if bool(re.search("[^a-zA-Z ]+", text)):
                raise ValueError("Contains non-letters")
            if ord(text) > 64 and ord(text) < 91:
                return chr(a*(ord(text)-65)+b+65)
            if ord(text) > 96 and ord(text) < 123:
                return chr(a * (ord(text) - 97) + b + 97)
        else:
            raise TypeError(text)
    def decode(self,text,a,b):
        return text