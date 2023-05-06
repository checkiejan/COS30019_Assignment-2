from sentence import Sentence
import re
class KB:
    def __init__(self,lst):
        self.sentences = []
        self.symbols = {}
        for s in lst:
            self.addSentence(s)
    
    def addSentence(self, string):
        if string not in self.sentences:
            lst = re.findall("[a-zA-Z0-9]+", string)
            self.sentences.append(Sentence(string))
            for x in lst:
                self.symbols[x] = True
                
    def PLTrue(self,model):
        for s in self.sentences:
            s.setValue(model)
            if s.result() == False:
                return False
        return True
    
    