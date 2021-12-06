class Ceasar:
    def encode(self,text):
        return chr(ord(text)+3)
    def decode(self,text):
        return text