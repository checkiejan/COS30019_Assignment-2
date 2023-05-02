class Symbol:
    def __init__(self,character):
        self.character = character

class KB:
    def __init__(self):
        self.sentences = []
        self.symbols = []
    
    def addSentence(self, string):
        if string not in self.sentences:
            self.sentences.append(string)
            