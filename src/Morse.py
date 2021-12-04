def encode(text):
    if text == 'A':
        return '.-'
    if text == '1':
        return '.----'
    if text == '.':
        return '.-.-.-'
def decode(text):
    return text