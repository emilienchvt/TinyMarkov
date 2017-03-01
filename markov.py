import nltk
import random
import math
import numpy as np
from nltk.tokenize import SpaceTokenizer
import word2vec
w2v = word2vec.load('fr_small.bin')


#Cosine similarity between 2 words
def sim(w1, w2):
    try:
        vec1, vec2 = np.array(w2v[w1]), np.array(w2v[w2])
        norm1=np.linalg.norm(vec1)
        norm2=np.linalg.norm(vec2)
        return (vec1*vec2).sum()/(norm1*norm2)
    except KeyError:
        return 0

#This funtion is applied to the distance to the topic in order to change the graph's coefficient.
def filtre(s, strength):
    return 1/(1+np.exp(-strength*(s-0.5)))
        #To be improved

#tokenizer. Specific handling of \n
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

#Markov Model class
class Model:
    def __init__(self):
        self.dic = {}

    #softmax function, to be applied to a model
    def softmaxModel(self):
        for prev in self.dic.keys():
            oldvec = np.array(list(self.dic[prev].values()))
            sm = oldvec.sum()
            #Applying softmax
            newvec = [oldvec[i]/sm for i in range(len(oldvec))]
            #replacing values in dic
            i=0
            for foll in self.dic[prev].keys():
                self.dic[prev][foll]=newvec[i]
                i+=1


    #to train a model on a corpus
    def train(self, text, factor=1, applySoft=True):
        tokens = tokenize(text)

        #Add all the words in the model:
        for i in range(len(tokens)):
            try:
                self.dic[tokens[i]]
            except:
                self.dic[tokens[i]]={}

        #Add the links between words
        for i in range(len(tokens)-1):
            try:
                self.dic[tokens[i]][tokens[i+1]] += factor
            except KeyError:
                self.dic[tokens[i]][tokens[i+1]] = factor

        if applySoft==True:
            self.softmaxModel()

    #for multiple documents: texts and coeffs are arrays of the same size.
    #Higher Coeff[i] means that text[i] will be more represented in the model
    def trainMultiple(self, texts, coeffs=None):
        if coeffs==None:
            coeffs=np.ones(len(texts))
        for i in range(len(texts)):
            a = coeffs[i]
            b = 1/len(texts[i])
            self.train(texts[i], factor=a*b, applySoft=False)
        self.softmaxModel()

    #met tous les mots à 1.
    def flat(self):
        for prev in self.dic.keys():
            for foll in self.dic[prev].keys():
                self.dic[prev][foll]=1
        self.softmaxModel()


    #to have it focus on a topic (1 word)
    def focus(self, topic, strength=4):
        #loop over the integers:
        for prev in self.dic.keys():
            for foll in self.dic[prev].keys():
                sim(foll, topic)
                self.dic[prev][foll]*= filtre(sim(foll, topic), strength)
        self.softmaxModel()

    #next word, generated randomly according to the model
    def predictNext(self, previous):
        subModel = self.dic[previous]
        counts = np.array([subModel[word] for word in subModel.keys()])
        probas = (counts/sum(counts)).cumsum()
        threshold = random.random()
        i=0
        while probas[i]<=threshold:
            i+=1
        return list(subModel.keys())[i]

    #generate a sentence of 300+ characters. (the second loop finishes the sentence)
    def generateSentence(self):
        out = ""
        currword = '\n'
        while(len(out)<600):
            out += currword
            out += " "
            currword = self.predictNext(currword)
        while(currword!="\n"):
            out += currword
            currword = self.predictNext(currword)
            out += " "
        return out
