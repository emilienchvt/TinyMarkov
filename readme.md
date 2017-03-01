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
 2 heures du rap, elle en s'en aille, garder cette fille au foyer, des choses essentielles que t'étais seul aux filles parce qu'on pense à toi et des autres, on s'connaît pas ma princesse ne viendras plus qu'un mirage, les cuites<br>


### Georges Brassens:

 Et n'entra plus qu'une blonde<br>
 Il en chur,<br>
 Bien récompensée...<br>
 Le grand mouchoir en meute<br>
 La plus d'argent<br>
 Et je t'ai connue,<br>
 D'interrompre l'échauffouré'.<br>
 Je bande<br>
 Du fin que dans ma foi,<br>
 Le sable fin,<br>
 Une niche idéale.<br>
 Mais c'étaient mes bras lancaient des neiges d'antan?<br>
 Un champ d'honneur.<br>

Je suis dit, bonnes gens,<br>
Pour reconnaître<br>
Que l'on a<br>
De beaux assassinats.<br>
Il avait paru<br>
<br>

### Mélangés:

 [Alpha Waan]<br>
 Bellek à coup j'ai pas juger ceux d'mon charbonnier<br>
 Qui est mécontente<br>
 Parce que nul doute du 19, on a balayé le temps sont pas d'boss, pas conduire à Montfaucon,<br>
 Mais dans les veines<br>
 Qu'il est pris dans la sniffer<br>
 C’monde n’est qu’un pharmacien<br>
 Hu, dia, hop là!<br>
 Qu'elle est un humain sur la réalité, j'aimerais l'aider<br>

## Output theme - nekfeu - thème: la famille

### Pour Nekfeu:
#### 0 itérations, fit_topic: -0.00279357266227
Quand j'suis peut-être te grugent<br>
Trop de Air Max blanches et ses pensées s’accumulent et index en apparence<br>
J'ai pas s’mentir, on vivra<br>
Je m'en tape pour tes rêves ?<br>
Mes loups rôdent dans le moteur ronronnera<br>
<br>
J'compte pas d’pilon, Quand j'galère le trou noir je pense à coup dur de l'emploi<br>
#### 1 itération, fit_topic: 2.11359486562

J'irai, j'irai jusqu'au bout de vivre<br>
Lève-toi la chaussée<br>
J'te comprends pas dans son âge<br>
Qui ne vais repasser<br>
Si j’ai tous faux j'en ai deux-trois<br>
I'll be Calling you moving mad bro<br>
J’aime tes belles maisons, vous ils m'parlent de chez l'épicier ouvert les passants qui veulent surtout pas d’taff fuir le son sauveur, ma vie te manquent de sable<br>

#### 2 itérations, fit_topic: 6.28422371344
Dans cette femme et ses vieux son héritage au sein de ses fils de fric<br>
On se téléphoner<br>
Quand viennent de vie et j’suis un père til-gen, j’voulais l’divan<br>
J'ai beau être pauvre qu'avoir de sable<br>
J'relève la vie<br>
Tu crois être heureux avoir la vie et elle à ses vieux dans cette fille à son et sa mère<br>

#### 3 itérations, fit_topic: 10.6326274274
Avec mes gens se ferme la mère de son père de frère à son et ses fils de sa mère à vie et elle se greffer<br>
Tout seul moyen d'se rattraper<br>
Vu ma vie et elle avait envie de ses fils de vivre dans cette vie et ses fils de vivre dans ses fils de frère à cette fille de vivre dans cette vie de vivre dans son âge et elle peut être pauvre à son père de naître et elle se téléphoner<br>
