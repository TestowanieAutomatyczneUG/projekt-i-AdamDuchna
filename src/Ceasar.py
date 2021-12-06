import re
class Ceasar:
    def encode(self,text):
        if str == type(text):
            if bool(re.match("[A-Za-z]+",text)):
                return chr(ord(text) + 3)
            elif text == "":
                return text
            else:
                raise ValueError("Contains non-letters")
        else:
            raise TypeError(text)
    def decode(self,text):
        return text