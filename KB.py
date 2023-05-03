class Symbol:
    def __init__(self,character, logic):
        self.character = character
        self.logic = logic
    
    def logic(self):
        return self.logic
    
    def character(self):
        return self.character
    
    def setCharacter(self, character):
        self.character = character
    
    def setLogic(self, logic):
        self.logic = logic
    

class KB:
    def __init__(self):
        self.sentences = []
        self.symbols = []
    
    def addSentence(self, string):
        if string not in self.sentences:
            self.sentences.append(string)
            