import nltk
import random
import math
import numpy as np

def createModel(text):
    tokens = nltk.word_tokenize(text)
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
    indexFirstWord = int(random.random()*len(model))
    currword = list(model.keys())[indexFirstWord]
    while(len(out)<300):
        out += currword
        out += " "
        currword = nextWord(model, currword)
    return out


####### Example
with open("nekfeu.txt") as f:
    text = f.read()

model = createModel(text)
print(generateSentence(model))
