import markov
import numpy as np

with open("stupeflip.txt") as f:
    text = f.read()

#train a model with both the artists
model = markov.Model()
model.train(text)

n=100
topic = "amour"

def report():
    str(model.generateSentence()+str(np.array([np.array([(markov.sim(x, topic)) for x in model.generateSentence().split()]).sum() for i in range(n)]).mean()))

print("without topic:"+report())
model.focus(topic, strength=30)
print("After 1 focus:"+report())
model.focus(topic, strength=30)
print("After 2 focus:"+report())
model.focus(topic, strength=30)
print("After 2 focus:"+report())
model.focus(topic, strength=30)
