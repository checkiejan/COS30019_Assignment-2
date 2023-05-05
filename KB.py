from sentence import Sentence
class KB:
    def __init__(self,lst):
        self.sentences = []
        self.symbols = []
        for s in lst:
            self.addSentence(s)
    
    def addSentence(self, string):
        if string not in self.sentences:
            self.sentences.append(Sentence(string))
            