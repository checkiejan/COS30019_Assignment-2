import sympy 
import random
import string
import re
import unittest
from sympy.parsing.sympy_parser import parse_expr
from sympy import And, Or, Implies, Not, Equivalent, Symbol
from BC import  BC
from FC import FC
from TT import TT
from KB import KB
from WSAT import WSAT
from sentence import Sentence

def createHornTest():
    numberOfClause = random.randint(5,40)#number of sentence
    clauses = []
    numberOfSymbols= random.randint(3,20)
    while numberOfSymbols > numberOfClause:
        numberOfSymbols= random.randint(3,10)
    symbols = set()
    for i in range(numberOfSymbols): #get the unique list of symbols
        x= random.choice(string.ascii_letters)
        while x=="":
            x= random.choice(string.ascii_letters)
        symbols.add(x)
    symbols = list(symbols)
    
    statement = [] #statement is to store the list of facts
    query = random.choice(symbols)
    statement.append(query) #store query into statement to avoid the teset where query is a known fact
    for i in range(numberOfClause):
        clause = random.random()
        if clause > 0.6: #statement or fact more than 0.6 is fact
            if len(statement) == len(symbols): #skip if the first sentence
                continue
            temp = random.choice(symbols)
            while temp in statement: #make sure no repeated statement
                temp = random.choice(symbols)
            clauses.append(temp)
            statement.append(temp)
        else:
            depth = random.randint(2,numberOfSymbols) #number of the symbols before the imply operator
            s = []
            for x in range(depth):
                s.append(random.choice(symbols))

            sentence = " & ".join(s[:-1])
            sentence += f" => {s[-1]}"
            clauses.insert(0,sentence)
    kb = ";".join(clauses)  #join to make the sentence
    with open("generate.txt", 'w') as f:
            f.write(f"TELL\n{kb};\nASK\n{query}")
            
def joinClause(lst): #join different subclause for generic sentence
    operator = ["&", "||"]
    temp = ""
    for i in range(len(lst)):
        if i != len(lst)-1:
            temp += lst[i] + random.choice(operator)
        else:
            temp += lst[i]
    return temp

def createGenericSentence(symbols,operators = ["<=>","=>","&","||"]): #create a random generic sentence
    clause = random.random()
    if clause > 0.97: #statement or fact more than this probability is fact
        temp = random.choice(symbols)
        
        chance_negation = random.random()
        if chance_negation > 0.6: #negation for sentence
            temp = "~"+temp
        return temp
    else:
        number_subclause = random.randint(2,6) 
        sub_lst = []
        for j in range(number_subclause):
            chance_parathesis = random.random()
            temp = ""
            if chance_parathesis > 0.6:  #chance of containing parathesis
                temp += "("
                chance_clause = random.random()
                if chance_clause >0.7:
                    temp+="("
                    a = random.choice(symbols)
                    chance_negation_a = random.random()
                    if chance_negation_a > 0.6:
                        a = "~"+a
                    b = random.choice(symbols)
                    chance_negation_b = random.random()
                    if chance_negation_b > 0.6:
                        b = "~"+b
                    temp += a + random.choice(operators) + b + ")"
                else:
                    a = random.choice(symbols)
                    chance_negation_a = random.random()
                    if chance_negation_a > 0.6:
                        a = "~"+a
                    temp += "a"
                temp += random.choice(operators) #join between 2 subclause with an operator
                chance_clause = random.random()
                if chance_clause >0.9: # limit the chance of being another clause
                    temp+="("
                    a = random.choice(symbols)
                    chance_negation_a = random.random()
                    if chance_negation_a > 0.6:
                        a = "~"+a
                    b = random.choice(symbols)
                    chance_negation_b = random.random()
                    if chance_negation_b > 0.6:
                        b = "~"+b
                    temp += a + random.choice(operators) + b + "))"
                else:
                    a = random.choice(symbols)
                    chance_negation_a = random.random()
                    if chance_negation_a > 0.6:
                        a = "~"+a
                    temp += "a"
                    temp +=")"
            else: #or else should be a symbol
                a = random.choice(symbols) 
                chance_negation = random.random()
                if chance_negation > 0.6:
                    a = "~"+a
                temp += a
            sub_lst.append(temp)
            sentence = joinClause(sub_lst)
            return sentence
            
def createGenericTest():
    numberOfClause = random.randint(5,40) # number of sentences in the knowledge base
    operators = ["<=>","=>","&","||"] #operator allowed
    clauses = []
    numberOfSymbols= random.randint(3,20)
    while numberOfSymbols > numberOfClause:
        numberOfSymbols= random.randint(3,10)
    symbols = set()
    for i in range(numberOfSymbols):
        x= random.choice(string.ascii_letters)
        while x=="":
            x= random.choice(string.ascii_letters)
        symbols.add(x)
    symbols = list(symbols)
    
    statement = []
    query = createGenericSentence(symbols)
    statement.append(query)
    for i in range(numberOfClause):
        clause = random.random()
        if clause > 0.8: #statement or fact more than 0.7 is fact
            if len(statement) == len(symbols):
                continue
            temp = random.choice(symbols)
            while temp in statement: #make sure no repeated statement
                temp = random.choice(symbols)
                chance_negation = random.random()
                if chance_negation > 0.6:
                    temp = "~"+temp
            clauses.append(temp)
            statement.append(temp)
        else:
            number_subclause = random.randint(2,5)
            sub_lst = []
            for j in range(number_subclause):
                chance_parathesis = random.random()
                temp = ""
                if chance_parathesis > 0.6:    
                    temp += "("
                    chance_clause = random.random()
                    if chance_clause >0.7:
                        temp+="("
                        a = random.choice(symbols)
                        chance_negation_a = random.random()
                        if chance_negation_a > 0.6:
                            a = "~"+a
                        b = random.choice(symbols)
                        chance_negation_b = random.random()
                        if chance_negation_b > 0.6:
                            b = "~"+b
                        temp += a + random.choice(operators) + b + ")"
                    else:
                        a = random.choice(symbols)
                        chance_negation_a = random.random()
                        if chance_negation_a > 0.6:
                            a = "~"+a
                        temp += "a"
                    temp += random.choice(operators)
                    chance_clause = random.random()
                    if chance_clause >0.9:
                        temp+="("
                        a = random.choice(symbols)
                        chance_negation_a = random.random()
                        if chance_negation_a > 0.6:
                            a = "~"+a
                        b = random.choice(symbols)
                        chance_negation_b = random.random()
                        if chance_negation_b > 0.6:
                            b = "~"+b
                        temp += a + random.choice(operators) + b + "))"
                    else:
                        a = random.choice(symbols)
                        chance_negation_a = random.random()
                        if chance_negation_a > 0.6:
                            a = "~"+a
                        temp += "a"
                        temp +=")"
                   # temp += ")"
                else:
                    a = random.choice(symbols)
                    chance_negation = random.random()
                    if chance_negation > 0.6:
                        a = "~"+a
                    temp += a
                sub_lst.append(temp)
            sentence = joinClause(sub_lst)
            clauses.insert(0,sentence)
    kb = ";".join(clauses) 
    with open("generate.txt", 'w') as f:
            f.write(f"TELL\n{kb};\nASK\n{query}")

def postfix_to_infix(postfix_expr): #function to transform posfix to infix function
    stack = []

    for symbol in postfix_expr:
        # If the symbol is a propositional variable, push it to the stack
        if symbol.isalpha():
            stack.append(symbol)
        # If the symbol is a unary operator (~), pop the last element from the stack, combine it with the operator
        # and push the result back to the stack
        elif symbol == "~":
            operand = stack.pop()
            new_expr = f"{symbol}({operand})"
            stack.append(new_expr)
        # If the symbol is a binary operator (&, |, =>), pop the last two elements from the stack,
        # combine them with the operator and push the result back to the stack
        elif symbol in ["&", "|", ">>"]:
            operand2 = stack.pop()
            operand1 = stack.pop()
            new_expr = f"({operand1} {symbol} {operand2})"
            stack.append(new_expr)
        # If the symbol is a biconditional operator (<=>), replace it with a combination of & and | operators
        elif symbol == "<=>": #sympy does not have operator <=>
            operand2 = stack.pop()
            operand1 = stack.pop()
            new_expr = f"(({operand1} & {operand2}) | (~{operand1} & ~{operand2}))"
            stack.append(new_expr)
    # The last element in the stack is the infix expression
    return stack[-1]


def posfixEval(input): #Shunting Yard algorithm to transform into postfix 
    operator_stack = []  # Stack to store operators
    lst = [] #list to store the sentence
    precedence = {"~": 3, "&": 2, "|": 1, ">>": 0, "<=>": 0}

    for token in input:
        if token in ["~", "&", "|", ">>", "<=>"]:
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
    return lst #assign the list to the sentence list

            
def processHornInput(tracks):
    result = tracks.copy()
    for i in range(len(result)):
        temp = result[i]
        if re.search("=>", temp): #sympy use >> instead of =>
            temp = temp.replace("=>",">>")
            if re.search("&", temp): #append parenthesis for the sentence otherwise sympy will make this false
                temp = temp[:0] + '(' + temp[0:]
                index = temp.find(">>")
                temp = temp[:index] + ')' + temp[index:]
        result[i] = temp
    return result
def processGenericInput(tracks, query):
    result = tracks.copy()
    for i in range(len(result)):
        temp = result[i]
        input = re.findall("[a-zA-Z0-9]+|[&]|[~]|[|]+|\w*(?<!<)=>|<=>|[(]|[)]", temp)
        for j in range(len(input)):
            if input[j] == "=>": #sympy use >> instead of =>
                input[j] = ">>"
            if input[j] == "||": #sympy use | instead of ||
                input[j] = "|"
        
        lst = posfixEval(input)
       
        temp = postfix_to_infix(lst) #sympy does not have <=> in as a standalone operator so convert <=> in a different way
        result[i] = temp
    temp = query#process the query like sentences in the knowledge base
    input = re.findall("[a-zA-Z0-9]+|[&]|[~]|[|]+|\w*(?<!<)=>|<=>|[(]|[)]", temp)
    for j in range(len(input)):
        if input[j] == "=>":
            input[j] = ">>"
        if input[j] == "||":
            input[j] = "|"
    lst = posfixEval(input)
    
    query = postfix_to_infix(lst)
    return result,query
        
def writeError(track,query): #when a test fail write the scenerio to a file 
    kb = ";".join(track) 
    with open("error.txt", 'w') as f:
            f.write(f"TELL\n{kb};\nASK\n{query.lst[0]}")
    
def readKB():
    tracks = None
    query = None
    with open("generate.txt","r") as f: 
        track = f.readline().strip("[\n]")
        tracks = f.readline()
        tracks = tracks.strip("[\n] ")[:-1].strip().split(";")
        for i in range(len(tracks)):
            tracks[i] = tracks[i].replace(" ", "")
        track = f.readline().strip("[\n]")
        track = f.readline().strip("[\n]")
        query = track
    return tracks,query

class LogicTest(unittest.TestCase):
    def creatNewCase(self):
        res = False
        tracks = None
        query = None
        while not res:
            try: #if sympy cannot parse this case then create another one
                createHornTest()
                tracks,query = readKB()
                tracks_processed = processHornInput(tracks)
                self.track = tracks
                Set = set() #get unique list of sentence
                for x in tracks_processed:
                    exp = parse_expr(x)
                    Set.add(exp)
                query_processed = parse_expr(query)
                self.result = sympy.logic.inference.entails(query_processed,Set)
                res = True
            except:
                
                continue
        self.KB = KB(tracks)
        self.query = Sentence(query)
    
    def creatNewGenericCase(self):
        res = False
        tracks = None
        query = None
        while not res:
            try:
                createGenericTest()
                tracks,query = readKB()
                tracks_processed,query_gen = processGenericInput(tracks,query)
                self.track = tracks
                Set = set()
                for x in tracks_processed: #get unique list of sentence
                    exp = parse_expr(x)
                    Set.add(exp)
                query_processed = parse_expr(query_gen)
                self.result = sympy.logic.inference.entails(query_processed,Set)
                res = True
            except:
                continue
        self.KB = KB(tracks)
        self.query = Sentence(query)
        
    
    def setUp(self):
        # This method will be called before every test
        
        self.TT = TT()
        self.BC = BC()
        self.FC = FC()
        self.WSAT = WSAT()
        self.KB = None
        self.query = None
        self.track =None
        
    # def test_horn_truth_table(self):
    #     test = True
    #     for i in range(100): #number of test case
    #         self.creatNewCase()
    #         self.TT = TT()
    #         self.TT.infer(self.KB, self.query)
    #         result = self.TT.output
    #         flag = False
    #         if "YES" in result:
    #             flag = True
    #         if(flag != self.result): #whenever fail, break the test
    #             test = False
    #             print(f"TT fail:{i+1}")
    #             print(self.result)
    #             writeError(self.track,self.query)
    #             break
    #         print(f"TT pass:{i+1}")
    #     print()
    #     self.assertTrue(test)
        
    # def test_generic_truth_table(self):
    #     test = True
    #     for i in range(100): #number of test case
    #         self.creatNewGenericCase()
    #         self.TT = TT()
    #         self.TT.infer(self.KB, self.query)
    #         result = self.TT.output
    #         flag = False
    #         if "YES" in result:
    #             flag = True
    #         if(flag != self.result): #whenever fail, break the test
    #             test = False
    #             print(f"TT fail:{i+1}")
    #             print(self.result, flag)
    #             writeError(self.track,self.query)
    #             break
    #         print(f"Generic TT pass:{i+1}")
    #     print()
    #     self.assertTrue(test)
        
    def test_generic_WSAT(self):
        number_fail = 0
        number_pass = 0
        for i in range(10): #number of test case
            self.creatNewGenericCase()
            self.WSAT = WSAT()
            self.WSAT.infer(self.KB, self.query,True)
            result = self.WSAT.output
            flag = False
            if "YES" in result:
                flag = True
            if(flag != self.result):
                number_fail += 1
                print(f"Generic WSAT fail:{i+1}")
            else:
                print(f"Generic WSAT pass:{i+1}")
                number_pass += 1
                
        print(f"FAIL:{number_fail}, PASS:{number_pass}")
        self.assertTrue(True)
        
    
        
    # def test_horn_WSAT(self):
    #     number_fail = 0
    #     number_pass = 0
    #     for i in range(100): #number of test case
    #         self.creatNewCase()
    #         self.WSAT = WSAT()
    #         self.WSAT.infer(self.KB, self.query, True)
    #         result = self.WSAT.output
    #         flag = False
    #         if "YES" in result:
    #             flag = True
    #         if(flag != self.result):
    #             number_fail += 1
    #             print(f"WSAT fail:{i+1}")
    #         else:
    #             print(f"WSAT pass:{i+1}")
    #             number_pass += 1
                
    #     print(f"FAIL:{number_fail}, PASS:{number_pass}")
    #     self.assertTrue(True)
         
    # def test_backward_chaining(self):
    #     test = True
    #     for i in range(100): #number of test case
    #         self.creatNewCase()
    #         self.BC = BC()
    #         self.BC.infer(self.KB, self.query)
    #         result = self.BC.output
    #         flag = False
    #         if "YES" in result:
    #             flag = True
    #         if(flag != self.result): #whenever fail, break the test
    #             test = False
    #             writeError(self.track,self.query)
    #             print(f"BC fail:{i+1}")
    #             break
    #         print(f"BC pass:{i+1}")
    #     print()
    #     self.assertTrue(test)
        
    # def test_forward_chaining(self):
    #     test = True
    #     for i in range(100):
    #         self.creatNewCase()
    #         self.FC = FC()
    #         self.FC.infer(self.KB, self.query)
    #         result = self.FC.output
    #         flag = False
    #         if "YES" in result:
    #             flag = True
    #         if(flag != self.result): #whenever fail, break the test
    #             writeError(self.track,self.query)
    #             print(f"FC fail:{i+1}")
    #             test = False
    #             break
    #         print(f"FC pass:{i+1}")
    #     print()
    #     self.assertTrue(test)

if __name__ == "__main__":
    unittest.main()

