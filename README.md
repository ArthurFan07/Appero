# Optimisation hivernale

## Instructions d'installations

Afin de faciliter l'utilisation et la visualisation des résultats plusieurs packages supplémentaires sont nécessaires.
Il vous faudra tout d'abord python et les différends packages avec ```pip install ``` ou ```pip3 install```

```
pip3 install numpy
```
```
pip3 install osmnx
```
```
pip3 install networkx
```
```
pip3 install matplotlib
```

## Fonctionnement des algorithmes

Nos algorithmes sont divisés en 2 parties: 
* Une partie théorique avec une utilisation des bibliotèques standards de python
* Une partie pratique avec l'utilisation de *networkx*

La partie théorique est éxecuté avec le ```drone.py```. Cela représente le parcours du drone. Pour lancer ce script, il faut lacer la commande suivante :
```
python drone.py
```
Une fois le script lancé, on vous demandera de mettre un pays, une ville ainsi qu'un quartier. Si vous ne voulez pas rentrer de quartier, appuyez simplement sur ```enter``` lorsque le programme vous demandera un quartier.
Si jamais le localisation que vous avez entré n'est pas valid, le programme s'arretera et il faudra le relancer si vous voulez réessayer avec une ville.
En sortie du programme, vous aurez un graphe qui représentera la ville que vous avez indiqué ainsi les la liste des sommets à parcourir dans l'ordre afin d'avoir un cycle eulérien.

La partie pratique est éxecuté avec le script ```deneiger.py```, Cela représente le parcours de la déneigeuse. Pour lancer ce script, il faut lacer la commande suivante :
```
python deneiger.py
```
Tout comme la partie théorique, le prgramme vous demandera de rentrer un pays, une ville et un quartier.
Vous aurez également un graphe qui représentera la ville que vous avez indiqué ainsi les la liste des sommets à parcourir dans l'ordre afin d'avoir un cycle eulérien.