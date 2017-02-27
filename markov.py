import nltk
import random
import math
import numpy as np
from nltk.tokenize import SpaceTokenizer

def tokenize(s):
    out = []
    tokens = SpaceTokenizer().tokenize(s)
    for w in tokens:
        if w[:1]=="\n":
            out.append("\n")
            out.append(w[1:])
        else:
            out.append(w)
    return out

class Model:
    def __init__(self):
        self.dic = {}

    def train(self, text):
        tokens = tokenize(text)

        #Add all the words in the model:
        for i in range(len(tokens)):
           self.dic[tokens[i]]={}

        #Add the links between words
        for i in range(len(tokens)-1):
            try:
                self.dic[tokens[i]][tokens[i+1]] = self.dic[tokens[i]][tokens[i+1]] + 1
            except KeyError:
                self.dic[tokens[i]][tokens[i+1]] = 1

    def predictNext(self, previous):
        subModel = self.dic[previous]
        counts = np.array([subModel[word] for word in subModel.keys()])
        probas = (counts/sum(counts)).cumsum()
        seed = random.random()
        i=0
        while probas[i]<=seed:
            i+=1
        return list(subModel.keys())[i]

    def generateSentence(self):
        out = ""
        currword = '\n'
        while(len(out)<300):
            out += currword
            out += " "
            currword = self.predictNext(currword)
        while(currword!="\n"):
            out += currword
            out += " "
            currword = self.predictNext(currword)
        return out
