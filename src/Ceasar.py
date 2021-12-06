import re


class Ceasar:
    def encode(self, text):
        if str == type(text):
            if bool(re.match("[A-Za-z]+", text)):
                answ = ""
                for letter in text:
                    if letter == " ":
                        answ+= " "
                    elif letter.isupper():
                        if ord(letter) + 3 > 90:
                            answ += chr(64 + ((ord(letter) + 3) % 90))
                        else:
                            answ += chr(ord(letter) + 3)
                    elif letter.islower():
                        if ord(letter) + 3 > 122:
                            answ += chr(96 + ((ord(letter) + 3) % 122))
                        else:
                            answ += chr(ord(letter) + 3)
                return answ
            elif text == "":
                return text
            else:
                raise ValueError("Contains non-letters")
        else:
            raise TypeError(text)

    def decode(self, text):
        return text