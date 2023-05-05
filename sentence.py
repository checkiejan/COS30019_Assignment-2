import PropositionalSymbol
class Sentence:
    def __init__(self, string):
        self.symbols = []
        self.operators = ["~","&", "||", "=>","<=>"]
        self.sentence = []
        
        
    def createSentence(self,string):
        string= string.strip(" ")
        temp =0 
        flag = True
        for operator in self.operators:
            if operator not in  string:
                flag = False
        if flag:
            self.symbols.append(PropositionalSymbol(string))
            self.sentence.append(temp)
            return
        
        lst = 
        
    def containSymbol(self,symbol):
        s = PropositionalSymbol(symbol)
        for x in self.symbols:
            if x == s:
                return True
        return False
        
        
        
        
        
        
        
        
        
                