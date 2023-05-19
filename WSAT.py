import random
import re

class WSAT:
    def __init__(self):
        self.output = "NO"


    def infer(self, kb, query):
        maxIteration = int(input("Enter the max iteration"))
        relevanceCount = self.relevanceCount(kb.sentences)
        randomModel = self.randomModel(kb.symbols)
        
        flipChance = 0.5

        for i in range(maxIteration):
            if (kb.PLTrue(randomModel)):
                if (self.sentenceEvaluator(query, randomModel)):
                    self.output = "YES "+ str(i)

            
            randomSentence = self.getRandomFalseSentence(randomModel, kb.sentences)
            if randomSentence != None:
                if (random.random() > flipChance):
                    self.flipRandomSymbol(randomSentence, randomModel)
                else:
                    self.flipSymbolByRelevance(randomSentence, randomModel, relevanceCount)
            else:
                randomModel = self.randomModel(randomModel)

                 

    def randomModel(self, kbSymbols):
        symbolList = {}

        for symbol in kbSymbols.keys():
            symbolList[symbol] = random.choice([True, False])
        return symbolList

    def relevanceCount(self, sentenceList):
        relevanceCount = {}
        for sentence in sentenceList:
            if (len(sentence.lst) > 1):
                for symbol in range(len(sentence.lst)):
                    currentSymbol = sentence.lst[symbol]
                    if re.search("[a-zA-Z0-9]+", currentSymbol) != None:
                        if currentSymbol in relevanceCount:
                            relevanceCount[currentSymbol]+=1
                        else:
                            relevanceCount[currentSymbol] = 1
        return relevanceCount

    
    def getRandomFalseSentence(self, randomModel, sentenceList):
        hasFalseClause = False
        for sentence in sentenceList:
            if self.sentenceEvaluator(sentence, randomModel) == False:
                hasFalseClause = True
                break
        if hasFalseClause == False:
            return None

        while True:
            randomIndex =random.randint(0, len(sentenceList)-1)
            if self.sentenceEvaluator(sentenceList[randomIndex], randomModel) == False:
                return sentenceList[randomIndex]

    def flipRandomSymbol(self, sentence, randomModel):
        while True:
            randomIndex = random.randint(0,len(sentence.lst)-1)
            if re.search("[a-zA-Z0-9]+", sentence.lst[randomIndex]) != None:
                randomModel[sentence.lst[randomIndex]] = not randomModel[sentence.lst[randomIndex]]
                break

    def flipSymbolByRelevance(self, sentence, randomModel, relevanceCount):
        symbolToFlip = None

        for symbol in sentence.lst:
            if re.search("[a-zA-Z0-9]+", symbol) != None:
                if symbolToFlip == None or relevanceCount[symbol] > relevanceCount[symbolToFlip]:
                    symbolToFlip = symbol 

        if symbolToFlip != None:
            randomModel[symbolToFlip] = not randomModel[symbolToFlip]


    def sentenceEvaluator(self, sentence, symbolList):
        result = []
        LHS = None
        RHS = None
        for symbol in sentence.lst:
            if re.search("[a-zA-Z0-9]+", symbol) != None: 
                result.append(symbolList[symbol])
            else:
                if symbol == "&":
                    LHS = result.pop(0)
                    RHS = result.pop(0)
                    result.append(LHS and RHS)
                elif symbol == "=>":
                    LHS = result.pop(0)
                    RHS = result.pop(0)
                    result.append(not LHS or RHS)
                elif symbol == "~":
                    result.append(not result.pop(0))
                elif symbol == "<=>":
                    LHS = result.pop(0)
                    RHS = result.pop(0)
                    result.append(LHS == RHS)
                elif symbol == "||":
                    LHS = result.pop(0)
                    RHS = result.pop(0)
                    result.append(LHS or RHS)
        return result.pop(0)

    
 

    