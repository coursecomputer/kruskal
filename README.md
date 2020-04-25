[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

# Kruskal
<strong>[EN]</strong>  
Implementation of Kruskal's algorithm

Kruskal is an algorithm that looks for the minimum weight coverage tree in a graph.

<strong>[FR]</strong>  
Implémentation de l'algorithme de Kruskal

Kruskal est un algorithme qui recherche l'arbre couvrant de poids minimum dans un graphe.

## Explanation
* [English](./documentation/explanation.en.md)
* [Français](./documentation/explanation.fr.md)

## Pre-requisites
Before starting, please make sure you have installed:
- python [v3](https://www.python.org/)

## Installation
```bash
# Download the repository
git clone https://github.com/coursecomputer/kruskal.git
```

## Usage
CLI:
```bash
python3 -m unittest discover
```

CODE:
```python
from source.graph import Graph

graph = Graph({
  "A": { "B": 3, "C": 6 },
  "B": { "A": 3, "C": 8 },
  "C": { "A": 6, "B": 8 },
})

graph.kruskal()
# [
#   ("A", "B", 3),
#   ("A", "C", 6),
# ]
```

## Links
* https://en.wikipedia.org/wiki/Kruskal%27s_algorithm
* https://en.wikipedia.org/wiki/Disjoint-set_data_structure
* https://www.youtube.com/watch?v=wU6udHRIkcc&feature=youtu.be (Abdul Bari - 1.12 Disjoint Sets Data Structure - Weighted Union and Collapsing Find)
