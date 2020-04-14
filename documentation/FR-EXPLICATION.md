## Contribution
Vous pouvez contribuer à l'amélioration de la documentation, en ajoutant, modifiant ou supprimant des éléments.

## Définition
[L'algorithme de Kruskal](https://fr.wikipedia.org/wiki/Algorithme_de_Kruskal) est un algorithme de recherche [d'arbre couvrant de poids minimal](https://fr.wikipedia.org/wiki/Arbre_couvrant_de_poids_minimal)

Cette algorithme fait partie de la [théorie des graphes](https://fr.wikipedia.org/wiki/Th%C3%A9orie_des_graphes)

l'algorithme de kruskal s'applique au graphe connexe, non-orienter et pondere

<ul>
    <li>Un graphe connexe est un graphe où aucun sommet n'est isolé.</li>
    <li>Un graphe non orienté est un graphe où les arêtes non pas de restriction de direction, ils peuvent être représentés avec 2 flèches.</li>
    <li>Un graphe pondéré est un graphe où les arêtes ont une valeur. (peut représenter une distance)</li>
</ul>
<p align="left">
    <img src="./assets/definition1.png" width="500" alt="">
</p>

## Pseudo-Code
<p align="left">
    <img src="./assets/pseudocode.png" width="600" alt="">
</p>

## Utilisation

Tous d'abord nous devons récupérer les arêtes et les trier par leurs poids.

Ex:

```
(r, t, 20)      (a, n, 4)
(j, h, 23)  =>  (r, t, 20)
(a, n, 4)   =>  (j, h, 23)
...             ...
```



<p align="left">
    <img src="./assets/utilisation1.gif" width="1000" alt="">
</p>

Voici les principales choses à faire :
* Mettre chaque nœuds dans un ensemble
* Récupérer les arêtes et les trier par ordre croissant
* Et pour chaque arêtes :
  * Trouver l'ensemble du premier nœuds de l'arête, l'ensemble du second nœuds et les comparer
  * Si les deux ensemble sont diffèrent alors 


## Plus d'information
Vous pouvez accéder au [slide de présentation](./assets/slide/index.html) (utiliser les flèches pour défiler)