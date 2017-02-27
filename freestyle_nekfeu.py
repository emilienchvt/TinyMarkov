import markov

with open("nekfeu.txt") as f:
    text = f.read()

model = markov.createModel(text)
print(markov.generateSentence(model))
