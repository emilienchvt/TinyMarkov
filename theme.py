import markov
import numpy as np

with open("nekfeu.txt") as f:
    text_nek = f.read()
with open("georges-brassens.txt") as f:
    text_georges = f.read()

modeleGeorges = markov.Model()
modeleGeorges.train(text_georges)

modeleNek = markov.Model()
modeleNek.train(text_nek)

n=100
topic = 'mort'
print("Essayons d'orienter les paroles ver le thème de la mort:")

def report(model):
    print("Indice de similitude avec la mort, avant focus:")
    print(np.array([np.array([(markov.sim(x, topic)) for x in model.generateSentence().split()]).sum() for i in range(n)]).mean())

    report = model.focus(topic, strength=30)

    print("Indice de similitude avec la mort, après focus:")
    print(np.array([np.array([(markov.sim(x, topic)) for x in model.generateSentence().split()]).sum() for i in range(n)]).mean())

    print("Une petite chanson sur la mort:")
    print(model.generateSentence())

print("Pour Nekfeu: ")
report(modeleNek)
print("Pour Georges Brassens: ")
report(modeleGeorges)
