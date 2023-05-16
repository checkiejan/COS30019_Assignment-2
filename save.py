from PropositionalSymbol import PropositionalSymbol
import re

def Or(a,b):
    return a or b
def And(a,b):
    return a and b
def Imply(a,b):
    if a and not b:
        return False
    return True
def Not(a):
    return not a

def Bicondition(a,b):
    if a == b:
        return True
    return False

class Sentence:
    def __init__(self, string):
        self.lst = None
        self.symbols = []
        self.operators = {"&": And, "=>": Imply ,"<=>": Bicondition,"~": Not,"||": Or}
        self.sentence = []
        self.create(string)
        self.count = 0

        
    def containSymbol(self,symbol):
        s = PropositionalSymbol(symbol)
        for x in self.symbols:
            if x == s:
                return True
        return False
    
    def getSymbol(self,symbol):
        s = PropositionalSymbol(symbol)
        for x in self.symbols:
            if x == s:
                return x
        return None
        
    def create(self,string):
        lst = re.findall("[a-zA-Z0-9]+|[&]|[~]|[|]+|=>", string)
        self.lst = lst
        i = 0
        while  i < len(lst):
            if lst[i] in self.operators:
                temp1 = lst[i]
                lst[i] = lst[i+1]       
                lst[i+1] = temp1
                i +=1 
            i += 1
        for x in lst:
            if(x in self.operators.keys()):   
                self.sentence.append(x)
            else:
                temp = PropositionalSymbol(x)
                if not self.containSymbol(x):   
                    self.symbols.append(temp)
                    self.sentence.append(temp)
                else:
                    self.sentence.append(self.getSymbol(x))
                    
    def createGeneric(self,string):
        lst = re.findall("[a-zA-Z0-9]+|[&]|[~]|[|]+|\w*(?<!<)=>|<=>", string)
        self.lst = lst
        i = 0
        while i < len(lst):
            if lst[i] in self.operators:
                temp1 = lst[i]
                lst[i] = lst[i+1]       
                lst[i+1] = temp1
                i +=1 
            i += 1

    def setValue(self,model):
        for k,v in model.items():
            temp = self.getSymbol(k)
            if temp is not None:
                temp.setValue(v)

    def setCount(self):
         for symbol in range(len(self.lst)-2):
                if re.search("[a-zA-Z0-9]+", self.lst[symbol]) != None:
                    self.count += 1
    
    def getValue(self):
        return self.result()
    
    def result(self):
        if len(self.sentence) == 1:
            return  self.symbols[0].getValue()
        else:
            back = self.sentence[0].getValue()
            index = 0
            result = True
            while index < len(self.sentence):
                result = self.sentence[index].getValue()
            
                if  index + 1 < len(self.sentence) and self.sentence[index+1] not in self.symbols:
                    func =  self.operators[self.sentence[index+1]]
                    result = func(back, result)
                    back = result
                    index +=1
                index +=1
            return back
        
        
        
    def posfixEval(self):
        output_queue = []  # Output queue for the Reverse Polish Notation (RPN)
        operator_stack = []  # Stack to store operators
        lst = []
        precedence = {"~": 3, "&": 2, "||": 1, "=>": 0, "<=>": 0}

        for token in self.lst:
            if token in ["~", "&", "||", "=>", "<=>"]:
                while operator_stack and operator_stack[-1] != "(" and precedence[token] <= precedence[operator_stack[-1]]:
                    temp = operator_stack.pop()
                    lst.append(temp)
                    output_queue.append(temp)
                operator_stack.append(token)
            elif token == "(":
                operator_stack.append(token)
            elif token == ")":
                while operator_stack and operator_stack[-1] != "(":
                    lst.append(token)
                    output_queue.append(operator_stack.pop())
                operator_stack.pop()  # Remove "(" from stack
            else:
                lst.append(token)
                output_queue.append(self.getSymbolValue(token))

        while operator_stack:
            temp = operator_stack.pop()
            lst.append(temp)
            output_queue.append(temp)
        self.lst = lst
        print(lst)
        