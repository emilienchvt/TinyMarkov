import markov

with open("nekfeu.txt") as f:
    text_nek = f.read()
with open("georges-brassens.txt") as f:
    text_georges = f.read()


model_nek = markov.Model()
model_nek.train(text_nek)

model_georges = markov.Model()
model_georges.train(text_georges)

model_mix = markov.Model()
model_mix.train(text_nek+"\n\n"+text_georges)


print("\n\nNekfeu:")
print(model_nek.generateSentence())
print("\n\nGeorges Brassens: ")
print(model_georges.generateSentence())
print("\n\nMélangés: ")
print(model_mix.generateSentence())
