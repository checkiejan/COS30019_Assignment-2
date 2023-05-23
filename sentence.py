from PropositionalSymbol import PropositionalSymbol
import re


class Sentence:
    def __init__(self, string):
        self.lst = None
        self.symbols = []
        self.sentence = []  
        self.createSentence(string)
        self.count = 0
        
        
    def containSymbol(self,symbol): #check if the sentence contains a symbol
        s = PropositionalSymbol(symbol)
        for x in self.symbols:
            if x == s:
                return True
        return False
    
    def getSymbol(self,symbol): #get the symbol from the sentence
        s = PropositionalSymbol(symbol)
        for x in self.symbols:
            if x == s:
                return x
        return None
        
                    
    def createSentence(self,string):
        lst = re.findall("[a-zA-Z0-9]+|[&]|[~]|[|]+|\w*(?<!<)=>|<=>|[(]|[)]", string) #separate the sentence into a list of symbols and operator
        self.lst = lst
        self.posfixEval() #transform sentence into a postfix form
        symbols = re.findall("[a-zA-Z0-9]+", string)
        set1 = set(symbols)
        for x in set1: #create a set of symbols for the sentence
            temp = PropositionalSymbol(x)
            self.symbols.append(temp)
        
        

    def setValue(self,model): #set value for symbols in the sentence
        for k,v in model.items(): 
            temp = self.getSymbol(k)
            if temp is not None:
                temp.setValue(v)

    def setCount(self): #count for horn clause the number of symbols before the imply operator
         for symbol in range(len(self.lst)-2):
                if re.search("[a-zA-Z0-9]+", self.lst[symbol]) != None:
                    self.count += 1
               
    def result(self): # return the result of the sentence
        return self.evaluate_sentence()
    
    def getSymbolValue(self,symbol): #get value of the symbol in the sentence
        result = self.getSymbol(symbol)
        if result is not None:
            return result.getValue()
        
    def evaluate_sentence(self): #evaluate the sentence with the stored value of each symbols
        output_queue = [] 
        for token in self.lst:
            if token not in ["~", "&", "||", "=>", "<=>"]: #if token is a symbol then get its value
                output_queue.append(self.getSymbolValue(token))
            else:
                output_queue.append(token)
        return self.evaluate_exp(output_queue)

    def posfixEval(self): #Shunting Yard algorithm to transform into postfix 
        operator_stack = []  # Stack to store operators
        lst = [] #list to store the sentence
        precedence = {"~": 3, "&": 2, "||": 1, "=>": 0, "<=>": 0}

        for token in self.lst:
            if token in ["~", "&", "||", "=>", "<=>"]:
                while operator_stack and operator_stack[-1] != "(" and precedence[token] <= precedence[operator_stack[-1]]:
                    temp = operator_stack.pop()
                    lst.append(temp)
                operator_stack.append(token)
            elif token == "(":
                operator_stack.append(token)
            elif token == ")":
                while operator_stack and operator_stack[-1] != "(":
                    temp = operator_stack.pop()
                    lst.append(temp)
                operator_stack.pop()  # Remove "(" from stack
            else:
                lst.append(token)

        while operator_stack:
            temp = operator_stack.pop()
            lst.append(temp)
        self.lst = lst #assign the list to the sentence list
            
    def evaluate_exp(self,expression): #evaluate the sentence based on already processed expression
        stack = []
        for token in expression:
            if token in ["~", "&", "||", "=>", "<=>"]:
                right_operand = stack.pop()
                if token != "~":
                    left_operand = stack.pop()
               
                if token == "~":
                    result = not right_operand
                elif token == "&":
                    result = left_operand and right_operand
                elif token == "||":
                    result = left_operand or right_operand
                elif token == "=>":
                    result = (not left_operand) or right_operand
                elif token == "<=>":
                    result = left_operand == right_operand

                stack.append(result)
            else:
                stack.append(token)

        return stack[0]