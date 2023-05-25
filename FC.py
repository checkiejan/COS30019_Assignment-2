import sys
import re

sys.setrecursionlimit(100000)
class FC:
    def __init__(self) -> None:
        self.output = ""

    def getOutput(self):
        return self.output

    def infer(self, kb, query):
        sentenceCount = {}
        inferredSymbol = []
        symbolList = {}
        
        # Add the symbols that are true in in the list and make the inferred list
        for symbol in kb.symbols.keys():
            symbolList[symbol] = False
            if kb.symbols[symbol]:
                inferredSymbol.append(symbol)
        # Initiallize the count for each sentence 
        for sentence in kb.sentences:
            sentenceCount[sentence] = sentence.count
           
            #print(sentence.lst, sentenceCount[sentence])
            
        if query.lst[0] in inferredSymbol:
            self.output = "YES: " + query.lst[0]
            return

        
        
        while len(inferredSymbol) > 0:
            # Get the next symbol in the list of true symbols
            
            currentSymbol = inferredSymbol.pop(0)
            if currentSymbol == query.lst[0]:
                self.output = "YES: " + self.output + currentSymbol
                return
            if (symbolList[currentSymbol] == False):
                symbolList[currentSymbol] = True
                self.output += currentSymbol + ", "

                # Loop through the sentence in KB to find the symbol
                for sentence in kb.sentences:
                    # Loop through each symbol on the left hand side to find the symbol
                    for i in range(len(sentence.lst)-2):
                        if sentence.lst[i] == currentSymbol:
                            if (sentenceCount[sentence] > 0):
                                # decrease the point when a match is found
                                sentenceCount[sentence] -= 1
                                # append the symbol when the count reaches 0
                                #print(sentence.lst)
                                if sentenceCount[sentence]  <= 0:
                                    if sentence.lst[len(sentence.lst) - 2] == query.lst[0]:
                                        self.output = "YES: " + self.output + sentence.lst[len(sentence.lst) - 2]
                                        return
                                    inferredSymbol.append(sentence.lst[len(sentence.lst) - 2])


                
        self.output = "NO"

            

