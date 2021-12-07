import re


class Ceasar:
    def encode(self, text):
        if str == type(text):
            if bool(re.search("[^a-zA-Z ]+", text)):
                raise ValueError("Contains non-letters")
            elif text == "":
                return text
            else:
                answ = ""
                for letter in text:
                    if letter == " ":
                        answ += " "
                    elif ord(letter)>64 and ord(letter)<91:
                        if ord(letter) + 3 > 90:
                            answ += chr(64 + ((ord(letter) + 3) % 90))
                        else:
                            answ += chr(ord(letter) + 3)
                    elif ord(letter)>96 and ord(letter)<123:
                        if ord(letter) + 3 > 122:
                            answ += chr(96 + ((ord(letter) + 3) % 122))
                        else:
                            answ += chr(ord(letter) + 3)
                return answ
        else:
            raise TypeError(text)

    def decode(self, text):
        if str == type(text):
            if bool(re.search("[^a-zA-Z ]+", text)):
                raise ValueError("Contains non-letters")
            elif text == "":
                return text
            else:
                answ = ""
                for letter in text:
                    if letter == " ":
                        answ += " "
                    elif ord(letter)>64 and ord(letter)<91:
                        if ord(letter) - 3 < 65:
                            answ += chr(91 + (ord(letter) - 65) - 3)
                        else:
                            answ += chr(ord(letter) - 3)
                    elif ord(letter)>96 and ord(letter)<123:
                        if ord(letter) - 3 < 97:
                            answ += chr(122 + (ord(letter) - 96) - 3)
                        else:
                            answ += chr(ord(letter) - 3)
                return answ
        else:
            raise TypeError(text)
