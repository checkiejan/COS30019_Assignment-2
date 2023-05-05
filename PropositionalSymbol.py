class PropositionalSymbol:
    def __init__(self,character):
        self.character = character
        self.value = False

    def getValue(self):
        return self.value
    
    def setValue(self, value):
        self.value = value
    
    def getCharacter(self):
        return self.character
        
    def __eq__(self, other):
        return self.character == other.character