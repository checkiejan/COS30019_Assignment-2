class PropositionalSymbol:
    def __init__(self,character):
        self.character = character
        self.value = True

    def getValue(self):
        return self.value
    
    def setValue(self, value):
        self.value = value
    
    def getCharacter(self):
        return self.character
        
    def __eq__(self, other):
        if type(other)  is not PropositionalSymbol:
            return False
        return self.character == other.character
    
    def __str__(self) -> str:
        return f"character:{self.character}, value:{self.value}"