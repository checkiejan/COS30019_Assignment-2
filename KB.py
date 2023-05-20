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
            sentence = Sentence(string)
            lst = re.findall("[a-zA-Z0-9]+", string)
            self.sentences.append(sentence)
            sentence.setCount()
            
            if len(lst) == 1:
                self.symbols[lst[0]] = True
            else:
                for x in lst:
                    self.symbols[x] = False
            

    def setValue(self,dict):
        for k,v in dict.items():
            if k in self.symbols.keys():
                self.symbols[k] = v

    def PLTrue(self,model):
        for s in self.sentences:
            s.setValue(model)
            if s.result() == False:
                return False
        return True
    
    

