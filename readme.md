## Description

### markov.py
implementation of a markov model class. features:
- training a model on a class
- generating sentences based on the model
- focus the model on a specific topic (given by a word) by applying a similarity factor to the model

### example1: freestyle:

generating lyrics from Nekfeu and Georges Brasses, and mixing their models to generate text from the union.

### example2: theme:

displaying topic_fit and text generated after several updates of the model to focus on the tocim "famille"

## Output freestyle:

### Nekfeu:

 Y'a certains de toutes sortes de ur' jnounés <br>
 Avant tu t'es solo quand elle est une obligation<br>
 I'm doing<br>
 Elle danse comme Sankara<br>
 On est grand jour est la jungle<br>


### Georges Brassens:

 Je bande<br>
 Mais c'étaient mes bras lancaient des neiges d'antan?<br>
 Un champ d'honneur.<br>

 Je suis dit, bonnes gens,<br>
 Pour reconnaître<br>
 Que l'on a<br>
 De beaux assassinats.<br>
 Il avait paru<br>
<br>

### Mélangés(Stupeflip, PNL, Nekfeu, Brassens):

Je l'ai laissée faire ce siècle, entre elles n’auront jamais la la faire des joko sur mon avenue <br>
Quand mes potos boivent trop vilaine, il s’met en casseurs <br>
J'arrive en bas<br>
Tout contre laquelle j'mets c'panier du miroir élabore un parfait avenir <br>
Sauf le péché véniel <br>
Les gars sont chorégraphiés <br>

## Output theme - nekfeu - thème: la famille

### Pour Nekfeu:
#### 0 itérations, fit_topic: -0.00279357266227
Quand j'suis peut-être te grugent<br>
Trop de Air Max blanches et ses pensées s’accumulent et index en apparence<br>
J'ai pas s’mentir, on vivra<br>
J'compte pas d’pilon, Quand j'galère le trou noir je pense à coup dur de l'emploi<br>
#### 1 itération, fit_topic: 2.11359486562

J'irai, j'irai jusqu'au bout de vivre<br>
Lève-toi la chaussée<br>
J'te comprends pas dans son âge<br>
Qui ne vais repasser<br>

#### 2 itérations, fit_topic: 6.28422371344
Dans cette femme et ses vieux son héritage au sein de ses fils de fric<br>
On se téléphoner<br>
Quand viennent de vie et j’suis un père til-gen, j’voulais l’divan<br>
Tu crois être heureux avoir la vie et elle à ses vieux dans cette fille à son et sa mère<br>

#### 3 itérations, fit_topic: 10.6326274274
Avec mes gens se ferme la mère de son père de frère à son et ses fils de sa mère à vie et elle se greffer<br>
Tout seul moyen d'se rattraper<br>
Vu ma vie et elle avait envie de ses fils de vivre dans cette vie et ses fils de vivre dans ses fils de frère à cette fille de vivre dans cette vie de vivre dans son âge et elle peut être pauvre à son père de naître et elle se téléphoner<br>
