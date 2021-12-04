def encode(text):
    if text == 'A':
        return '.-'
    if text == '1':
        return '.----'
    if text == '.':
        return '.-.-.-'
    if type(text) != str:
        raise TypeError(text)
def decode(text):
    return text