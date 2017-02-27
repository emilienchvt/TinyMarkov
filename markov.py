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

def createModel(text):
    tokens = tokenize(text)
    model = {}

    #Add all the words in the model:
    for i in range(len(tokens)):
        model[tokens[i]]={}

    #Add the following words
    for i in range(len(tokens)-1):
        try:
            model[tokens[i]][tokens[i+1]] = model[tokens[i]][tokens[i+1]] + 1
        except KeyError:
            model[tokens[i]][tokens[i+1]] = 1

    return model

def nextWord(model, previous):
    subModel = model[previous]
    counts = np.array([subModel[word] for word in subModel.keys()])
    probas = (counts/sum(counts)).cumsum()
    seed = random.random()
    i=0
    while probas[i]<=seed:
        i+=1

    return list(subModel.keys())[i]

def generateSentence(model):
    out = ""
    currword = '\n'
    while(len(out)<1000):
        out += currword
        out += " "
        currword = nextWord(model, currword)
    return out
