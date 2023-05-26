import random
import re

class WSAT:
    def __init__(self):
        self.output = "NO"

    # This is the main function that performs the WalkSAT algorithm
    def infer(self, kb, query,test=False):
        maxIteration =400
        if test: #when using for unit test
            maxIteration = 600
        else:
            maxIteration = int(input("Enter the max iteration"))
        
        relevanceCount = self.relevanceCount(kb.sentences)

        # Create a random model using the symbols in the knowledge base
        randomModel = self.randomModel(kb.symbols)
        
        flipChance = 0.5

        for i in range(maxIteration):
            # If the random model satisfies all sentences in the knowledge base
            if (kb.PLTrue(randomModel)):
                    query.setValue(randomModel)
                    if query.result():
                        self.output = "YES "+ str(i)
                        return
                    else:
                        self.output = "NO"
                        return


            # Get a sentence from the knowledge base that is not satisfied by the random model
            randomSentence = self.getRandomFalseSentence(randomModel, kb.sentences)
            if randomSentence != None:
                # Flip a symbol in the random model with a chance of flipChance
                if (random.random() > flipChance):
                    self.flipRandomSymbol(randomSentence, randomModel)
                # Or flip the most relevant symbol
                else:
                    self.flipSymbolByRelevance(randomSentence, randomModel, relevanceCount)
            else:
                # If all sentences are satisfied, generate a new random model
                randomModel = self.randomModel(randomModel)

                 

    def randomModel(self, kbSymbols):
        symbolList = {}

        # Go through each symbol and flip the symbol 
        for symbol in kbSymbols.keys():
            symbolList[symbol] = random.choice([True, False])
        return symbolList

    def relevanceCount(self, sentenceList):
        relevanceCount = {}
        for sentence in sentenceList:
            # Find sentence that are not known facts
            if (len(sentence.lst) > 1):
                for symbol in range(len(sentence.lst)):
                    currentSymbol = sentence.lst[symbol]
                    if re.search("[a-zA-Z0-9]+", currentSymbol) != None:
                        # set the relance count for the symbol
                        if currentSymbol in relevanceCount:
                            relevanceCount[currentSymbol]+=1
                        else:
                            relevanceCount[currentSymbol] = 1
        return relevanceCount

    
    def getRandomFalseSentence(self, randomModel, sentenceList):
        hasFalseClause = False
        # Check if Knowledge base contain false clauses
        for sentence in sentenceList:
            sentence.setValue(randomModel)
            if sentence.result() == False:
                hasFalseClause = True
                break
        # Return none if there is no false clause in the knowledge base
        if hasFalseClause == False:
            return None

        # Get a random false clause from the knowledge base
        while True:
            randomIndex =random.randint(0, len(sentenceList)-1)
            sentenceList[randomIndex].setValue(randomModel)
            if sentenceList[randomIndex].result() == False:
                return sentenceList[randomIndex]

    def flipRandomSymbol(self, sentence, randomModel):
        while True:
            # Get a random index
            randomIndex = random.randint(0,len(sentence.lst)-1)
            if re.search("[a-zA-Z0-9]+", sentence.lst[randomIndex]) != None:
                # Flip the symbol in that index
                randomModel[sentence.lst[randomIndex]] = not randomModel[sentence.lst[randomIndex]]
                break

    def flipSymbolByRelevance(self, sentence, randomModel, relevanceCount):
        symbolToFlip = None

        for symbol in sentence.lst:
            if re.search("[a-zA-Z0-9]+", symbol) != None:
                # if the symbol to flip is none or the relance of teh symbol is higher than the current symbol to flip
                if symbolToFlip == None or relevanceCount[symbol] > relevanceCount[symbolToFlip]:
                    symbolToFlip = symbol 

        if symbolToFlip != None:
            randomModel[symbolToFlip] = not randomModel[symbolToFlip]



    
 

    