def encode(text):
    if type(text) != str:
        raise TypeError(text)
    else:
        text= text.upper()
        morse_dict_encode = {'A': '.-', 'B': '-...',
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
                             '0': '-----', ', ': '--..--', '.': '.-.-.-',
                             '?': '..--..', '/': '-..-.', '-': '-....-',
                             '(': '-.--.', ')': '-.--.-'}
        encoded_msg= ''
        for letter in text:
            if letter != ' ':
                encoded_msg+=morse_dict_encode[letter] + ' '
            else:
                encoded_msg+= ' '
        return encoded_msg[:-1]

def decode(text):
    return text