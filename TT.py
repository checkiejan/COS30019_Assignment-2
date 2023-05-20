import sys
sys.setrecursionlimit(100000)
class TT:
    def __init__(self) -> None:
        self.output = ""
        self.count = 0
        self.check = 0

    def getOutput(self):
        return self.output

    def infer(self,kb,query):
        temp = []
        for x in query.symbols:
            temp.append(x.getCharacter())
        lst = kb.symbols.copy() 
        for x in temp:
            lst[x] = False
        symbols = list(lst.keys())
        self.TTCheckAll(kb,query,symbols,{})
        if self.check == "NO":
            self.output = "NO"
        else:
            self.output = f"YES: {self.count}"
        
    def TTCheckAll(self,kb, query, symbols, model):
        if self.output == "NO":
            return
        if len(symbols) == 0:
            if kb.PLTrue(model):
                query.setValue(model)
                if query.result():
                    self.count +=1
                else:
                    self.check = "NO" 
        else:
            s = symbols.pop(0)
            s1 = symbols.copy()
            s2 = symbols.copy()
            t1 = model.copy()
            t2 = model.copy()
            t1[s] = True
            a = self.TTCheckAll(kb, query, s1, t1)
            t2[s] = False
            b= self.TTCheckAll(kb, query, s2, t2)
