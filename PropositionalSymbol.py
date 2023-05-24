class PropositionalSymbol:
    def __init__(self,character):
        self.character = character #store the character
        self.value = False #value for the character

    def getValue(self): #value of the symbol
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