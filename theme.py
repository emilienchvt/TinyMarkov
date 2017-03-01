import markov
import numpy as np

with open("stupeflip.txt") as f:
    text = f.read()

#train a model with both the artists
model = markov.Model()
model.train(text)

n=20
topic = "animal"
stren = 10

def report():
    return str(np.array([np.array([(markov.sim(x, topic)) for x in model.generateSentence().split()]).sum() for i in range(n)]).mean())

print("without topic:"+report())
print(model.generateSentence())
model.focus(topic, strength=stren)
print("\n\nAfter 1 focus:"+report())
print(model.generateSentence())
model.focus(topic, strength=stren)
print("\n\nAfter 2 focus:"+report())
print(model.generateSentence())
model.focus(topic, strength=stren)
print("\n\nAfter 3 focus:"+report())
print(model.generateSentence())
