##  Contribution
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


Un [arbre](https://fr.wikipedia.org/wiki/Arbre_(th%C3%A9orie_des_graphes)) est un graphe sans cycle et l'une des principales  fonctionnalités de cet algorithme est de trouver les cycles entre nœuds  déjà traiter.


<p align="left">
    <img src="./assets/definition1.png" width="500" alt="">
</p>

## Pseudo-Code

<p align="left">
    <img src="./assets/pseudocode.fr.png" width="600" alt="">
</p>



En anglais `v` == `vertices` == `sommets`

En anglais `e` == `edges` == `arêtes`

En anglais `u` == `undirected` == `non orienté`



`(u, v)` veut dire `A => B` et `A <= B`

## Utilisation

Cet exemple se fera avec le graphe ci-dessous : (un exemple graphique du graphe, se trouve dans la partie `Définition`)

```
A <=[5]=> B
A <=[4]=> C
A <=[11]=> D
B <=[7]=> C
B <=[20]=> F
C <=[9]=> D
C <=[12]=> E
C <=[8]=> F
D <=[5]=> E
E <=[9]=> F
```



La variable `Resultat` sera le résultat avec l'arbre couvrant minimal.

```
Resultat = []
```



1. Tous d'abord, on met tous les nœuds dans des `set`, les  `set`  peuvent être des listes, des nœuds d'un graphe ou un tableau. (`MAKE-SET`)

   

   Dans ce premier exemple, nous allons prendre des listes.

   ```
   [A] [B] [C] [D] [E] [F]
   ```



2. Ensuite nous devons récupérer les arêtes et les trier par leurs poids.

   

   Quand plusieurs arêtes sont égales, on choisie aléatoirement.

   ```
   A <=[4]=> C
   A <=[5]=> B  or  D <=[5]=> E
   D <=[5]=> E  or  A <=[5]=> B
   B <=[7]=> C
   C <=[8]=> F
   C <=[9]=> D  or  E <=[9]=> F
   E <=[9]=> F  or  C <=[9]=> D
   A <=[11]=> D
   C <=[12]=> E
   B <=[20]=> F
   ```



3. On boucle pour chaque arête trier.

   1. La première chose à faire dans la boucle est de vérifier dans quel liste sont les arêtes. (`FIND-SET`)

      ```
      A <=[4]=> C
      
      État du moment:
      [A] [B] [C] [D] [E] [F]
      
      [A] et [C] sont dans des ensembles différents
      ```


      1. Si les 2 ensembles sont différents, c'est qu'il n'y a pas de cycle alors on les fusionne. (`UNION`)

         ```
         État avant:
         [A] [B] [C] [D] [E] [F]
         
         État après:
         [A, C] [B] [D] [E] [F]
         ```

         

      2. Après avoir fusionné les ensembles, on stocke l'arête dans la variable `Resultat`:

         ```
         Resultat = [
           ...
           A <=[4]=> C
         ]
         ```

   

   1. Bis. 

      ```
      A <=[11]=> D
      
      État du moment:
      [A, C, B, D] [E] [F]
      
      [A, C, B, D] sont dans le même ensemble alors on ne fusionne pas pour éviter un cycle
      ```

      

4. À la fin, on retourne la variable `Resultat` qui contient tous les arêtes de l'arbre couvrant minimal

   ```
   return Resultat
   ```

<p align="left">
    <img src="./assets/utilisation1.gif" width="1200" alt="">
</p>

### Exemple avec arbre

Nous avons vu en gros comment fonctionne `Kruskal`.

L'exemple était avec une liste, on va voir un exemple avec un arbre.



Le fonctionnement est le même, pour le `FIND-SET` on retourne le parent du graphe.

```
  |A|
|B| |C|  => A
    |D|
    
  |E|    => E
```

Dans le premier cas le parent de `D` est `A`
Dans le second cas le parent de `E` est `E`

Dans `parent`, on retourne le parent du graphe



Le fonctionnement pour l' `UNION` .

```
   |A|            |A|                |E|
|B|   |C|  =>  |B|   |C| |E|  or  |G|   |A|
      |D|            |D| |G|          |B| |C|
                                          |D|
  |E|      =>
  |G|
```

On fusionne les graphes aléatoirement, un amélioration est de fusionner le plus petit arbre au plus grand. (À voir plus loin)

<p align="left">
    <img src="./assets/exampleTree.gif" width="1000" alt="">
</p>

### Exemple avec tableau

Le fonctionnement avec le tableau est un des moins gourmands en ressource.

L'initialisation du tableau se fait par des `-1` et le taille du tableau est le nombre de nœuds. (`MAKE-SET`)

```
[-1, -1, -1, -1, -1, -1]
```



Un simple tableau suffit, mais pour mon exemple j'ai ajouté un  dictionnaire pour relier le nom des nœuds et les indexes du tableau.

```
{
  A: 0
  B: 1
  C: 2
  D: 3
  E: 4
  F: 5
}

[-1, -1, -1, -1, -1, -1]
 A   B   C   D   E   F 
```



La spécificité du tableau est que les `nombres négatifs` désigne qu'il n'y a pas de parent et les `nombres positifs` sont des indexes vers les parents.

```
arr = [-3, 0, -1, 1, -1, -1]
       A   B  C   D  E   F
 
Si on cherche le parent de "D".
arr[D] = 1

1 est positif, alors c'est un index.
arr[1] = 0

0 est positif, alors c'est un index.
arr[0] = -3

-3 est négatif, alors c'est qu'il n’y a pas de parent.

Il est lui-même le parent, donc on récupère son index qui est 0.

Le parent de "D" est 0.
```



Pour le `FIND-SET`, on retourne l'index:

``` 
arr = [-3, 0, -1, 1, -1, -1]
        A  B   C  D   E   F
       
Le parent de "D", c'est 0
Le parent de "B", c'est 0  =>  NON-UNION

Le parent de "A", c'est 0
Le parent de "E", c'est 4  =>  UNION
```



Pour l'`UNION`, cette méthode implémente déjà une amélioration qui est le `rang`.

Le `rang` permet de fusionner le plus petit au plus grand. (À voir plus loin)

```
arr = [-3, 0, -1, 1, -1, -1]
        A  B   C  D   E   F
        
arr[D] = arr[B] = arr[A] = -3
arr[E] = -1

Le parent de "D", c'est 0
Le parent de "E", c'est 4  =>  UNION
```

On fusionne `E` dans `A`, parce que le rang de `A = -3` et plus grand que le rang de `E = -1`

Pour chaque fusion, on addition les rangs.

```
A = -3 devient A = -4
E = -1 devient E = 0 (index de A)

arr = [-4, 0, -1, 1, 0, -1]
        A  B   C  D  E   F
        
Si E = -2, alors:
A = -3 devient A = -5
E = -2 devient E = 0 (index de A)
```

<p align="left">
    <img src="./assets/exampleArray.gif" width="1000" alt="">
</p>



## Optimisation

 #### La compression des chemins

La compression des chemins ce fait lors du `FIND-SET` est non lors de l'`UNION`, et elle ne se fait pas en une fois.



Voici un exemple avec les 2 même `FIND-SET`:

``` =
arr = [-3, 0, -1, 1, -1, -1]
        A  B   C  D   E   F
        
find(D) = 0
arr[D] = arr[B] = arr[A]
```

L'algorithme à remonter jusqu'à l'index `0`.



On vérifie si le parent de D est `positif`. (S’il est négatif, il n'a pas de parent, c'est lui-même le parent)
Et on vérifie si le parent de D est `différent de l'index du parent du graphe` soit `0`. 

Alors `arr[D] = 0`



Si on refait une recherche

```
arr = [-3, 0, -1, 0, -1, -1]
        A  B   C  D   E   F

find(D) = 0
arr[D] = arr[A]
```

Un coup de moins.

<p align="left"> 
    <img src="./assets/pathCompression.png" width="1000" alt="">
</p>



<p align="left">
    <img src="./assets/pathCompression.gif" width="1000" alt="">
</p>



#### Le rang

Comme on la vu plus haut, le `rang` permet d'optimiser les fusions.

En fusionnant le plus petit vers le plus grand, on donne moins de boulot au `compression des chemins` et plus de chemin sont à `1 coup` du parent du graphe.

La méthode du tableau l'implémente par défaut.



Dans l'algorithme, un simple

```
A.rang > G.rang:
  G.parent = A
sinon
  A.parent = G
```

<p align="left">
    <img src="./assets/rank.png" width="1000" alt="">
</p>



Cet exemple montre la méthode optimiser et la méthode non-optimiser.

<p align="left">
    <img src="./assets/rank2.png" width="1000" alt="">
</p>