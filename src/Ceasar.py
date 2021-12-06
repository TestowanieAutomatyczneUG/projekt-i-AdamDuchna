import re
class Ceasar:
    def encode(self,text):
        if str == type(text):
            if bool(re.match("[A-Za-z]+",text)):
                answ=""
                for letter in text:
                    answ += chr(ord(letter) + 3)
                return answ
            elif text == "":
                return text
            else:
                raise ValueError("Contains non-letters")
        else:
            raise TypeError(text)
    def decode(self,text):
        return text