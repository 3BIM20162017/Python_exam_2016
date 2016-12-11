# Python_exam_2016

[Lien vers le sujet](https://sergiopeignier.github.io/teaching/python/DS.pdf)

##Infos sur la partie 1
J'ai récupéré les séquences sur le NCBI. La séquence "unknow.fasta" est le génome d'une souche de grippe, elle
sert juste à faire le log-likelihood.

Pour visualiser les fichiers HTML, téléchargez les et ouvrez avec votre navigateur. Github arrive pas à les montrer
en *nesting* dans une page à cause de leur taille.

##Installation de plotly

La première partie (markov.py) contient plein de commentaires "Décommentez si vous avez plotly"
Je vous montre ici comment l'installer. (**sur vos ordis persos, avec un accès administrateur**)

Plotly est une librairie qui génère des graphiques stylés assez facilement (en plus, en html ^^) et je m'en sert dans la partie 
chaînes de markov pour les heatmaps.

Si vous avez pip installé (vérifiez en faisant `pip --version` en terminal), tapez juste  
```
$ sudo pip install plotly
```
Entrez motre mdp et c'est parti !
Sinon, installez pip, puis plotly avec : 
```
$ sudo apt-get install python-pip python-dev build-essential 
$ sudo pip install --upgrade pip 
$ sudo pip install plotly
```
*Note : `apt-get` marchera avec les distribs debian (ubuntu, xubuntu, debian et dérivés) si apt-get marche pas chez vous, essayez ` sudo yum`
à la place.*

Pour utiliser plotly, je laisse [un lien vers la doc ici](https://plot.ly/python/)

