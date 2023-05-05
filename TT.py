class TT:
    def __init__(self) -> None:
        self.output = 0
        
    def getOutput(self):
        return self.output

    def TTEntail(self,kb,query):
        temp = query.symbols
        lst = kb.symbols.copy() 
        for x in temp:
            lst[x] = True
        symbols = lst.keys()
        self.TTCheckALL(kb,query,symbols,{})
        if self.output == 0:
            self.output = "NO"
        else:
            self.output = f"YES: {self.output}"
        
    def TTCheckAll(self,kb, query, symbols, model):
        if not symbols:
            if kb.PLTrue(model):
                query.setValue(model)
                if query.result:
                    self.output +=1
                else:
                    self.output = 0
                    return
        else:
            s = symbols.pop(0)
            model[s] = True
            self.TTCheckAll(kb, query, symbols, model)
            model[s] = False
            self.TTCheckAll(kb, query, symbols, model)