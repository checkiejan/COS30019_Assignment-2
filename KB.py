from sentence import Sentence
import re
class KB:
    def __init__(self,lst):
        self.sentences = [] #list of propositional sentences
        self.strings = [] #list to keep track of duplicate sentences
        self.symbols = {} #all symbols available in a knowledge base
        if not (len(lst) == 1 and lst[0] ==""): #if the knowledge base is not empty
            for s in lst:
                self.addSentence(s)
    
    def addSentence(self, string):
        if string not in self.strings: #check for duplicate sentence
            self.strings.append(string)
            sentence = Sentence(string)
            lst = re.findall("[a-zA-Z0-9]+", string) # find all symbols in the sentence
            self.sentences.append(sentence)
            sentence.setCount() #this one is for horn clause to count the number of symbols before the imply operator
            if len(lst) == 1: #if the sentence is a fact
                self.symbols[lst[0]] = True #assign that symbol with true value
            else: #otherwise, every value is false
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
    
    

