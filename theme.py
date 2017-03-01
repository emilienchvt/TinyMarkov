import markov
import numpy as np

with open("nekfeu.txt") as f:
    text = f.read()

#train a model with both the artists
model = markov.Model()
model.train(text)

n=100
topic = "famille"
print("without topic:")
print(model.generateSentence())
print("After 1 focus: \nSimilitude from "+str(np.array([np.array([(markov.sim(x, topic)) for x in model.generateSentence().split()]).sum() for i in range(n)]).mean()))
report = model.focus(topic, strength=30)
print("to "+str(np.array([np.array([(markov.sim(x, topic)) for x in model.generateSentence().split()]).sum() for i in range(n)]).mean()))
print(model.generateSentence())
print("After 2 focus:")
report = model.focus(topic, strength=30)
print("similitude to "+str(np.array([np.array([(markov.sim(x, topic)) for x in model.generateSentence().split()]).sum() for i in range(n)]).mean()))
print(model.generateSentence())
print("After 3 focus:")
report = model.focus(topic, strength=30)
print("similitude to "+str(np.array([np.array([(markov.sim(x, topic)) for x in model.generateSentence().split()]).sum() for i in range(n)]).mean()))
print(model.generateSentence())
