import re


class Morse:

    def __init__(self):
        self.morse_dict = {'A': '.-', 'B': '-...',
                           'C': '-.-.', 'D': '-..', 'E': '.',
                           'F': '..-.', 'G': '--.', 'H': '....',
                           'I': '..', 'J': '.---', 'K': '-.-',
                           'L': '.-..', 'M': '--', 'N': '-.',
                           'O': '---', 'P': '.--.', 'Q': '--.-',
                           'R': '.-.', 'S': '...', 'T': '-',
                           'U': '..-', 'V': '...-', 'W': '.--',
                           'X': '-..-', 'Y': '-.--', 'Z': '--..',
                           '1': '.----', '2': '..---', '3': '...--',
                           '4': '....-', '5': '.....', '6': '-....',
                           '7': '--...', '8': '---..', '9': '----.',
                           '0': '-----', ',': '--..--', '.': '.-.-.-',
                           '?': '..--..', '/': '-..-.', '-': '-....-',
                           '(': '-.--.', ')': '-.--.-', '"': '.-..-.',
                           '!': '-.-.--', ':': '---...'}

    def encode(self, text):
        if type(text) != str:
            raise TypeError(text)
        else:
            text = text.upper()
            if bool(re.search("\w", text)):
                encoded_msg = ''
                for letter in text:
                    if letter != ' ':
                        encoded_msg += self.morse_dict[letter] + ' '
                    else:
                        encoded_msg += ' '
                return encoded_msg[:-1]
            else:
                raise ValueError("This is already encoded")

    def decode(self, text):
        if type(text) != str:
            raise TypeError(text)
        else:
            if bool(re.match("[ .-]*", text)):
                text += ' '
                decoded_msg = ''
                storage = ''
                i = 0
                for letter in text:
                    if letter != ' ':
                        i = 0
                        storage += letter
                    else:
                        i += 1
                        if i == 2:
                            decoded_msg += ' '
                        else:
                            decoded_msg += list(self.morse_dict.keys())[list(self.morse_dict
                                                                             .values()).index(storage)]
                            storage = ''

                return decoded_msg
            else:
                raise ValueError("This is already decoded")
