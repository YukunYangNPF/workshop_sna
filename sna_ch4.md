Summarizing a network
======
![word-net](http://2.bp.blogspot.com/-loCreSlUoec/TlsL5W4L_zI/AAAAAAAAAnY/gCbivQf7BMc/s1600/data%2Bviz.jpg)


## Basics from Graph Theory
```{panels}
:column: col-12
*Walk* is a sequence of nodes and a sequence of edges that joins two nodes. A walk from $i_j$ to $i_k$ is a sequene of nodes ($i_j$, $i_j+1$, ...,$i_k$), and a sequence of edges ($i_j$$i_{j+1}$, $i_{j+1}$$i_{j+2}$, ..., $i_{k-1}$$i_{k}$). Usually, we can just use a list of nodes to describe the sequence.

*Path* is a walk that each node is distinct. It just basically means that you can not cycle back.

*Cycle* is a walk where the first node is the last node. We end up with the starting node.

*Geodesic* is the *shortest path* between nodes. It means that you calculate how many links are in all possible paths between two nodes and pick the one with the fewest number of links (for an unweighted graph). 
```

```{figure} images/ch4/path_waks.jpeg
---
height: 150px
name:  path
---
Walk, Path, Cycle, & Shortest Path
```


## Diameter & Average Path Length
> The diameter of a graph is the length of the *longest geodesic* (i.e., the longest shortest path) between any pairs of nodes. 

It describes how close nodes are to each other. 
- How long will it take to get from one node to another in some sense
- How fast will information spread? 
- How quickly can we get from one part of the graph to another

> Average Path Length is the average geodesic in the network (less prone to outliers). 

Looking at social networks in the real world is that they tend to have short average path lengths and short diameters:
- Milgram (1967) letter experiments
    – median 5 for the 25% that made it
- Co‐Authorship studies
    – Grossman (2002) Math mean 7.6, max 27,
    – Newman (2001) Physics mean 5.9, max 20
    – Goyal et al (2004) Economics mean 9.5, max 29
- WWW
    – Adamic, Pitkow (1999) – mean 3.1 (85.4% possible of 50M pages)
- Facebook
    – Backstrom et al (2012) – mean 4.74 (721 million users)

``` {note}
Global network properties on resilience: the largest connected component, the average shortage path length (APL), diameter (D), clustering coefficient (CC), BC, etc. Lower APL and higher CC are typically considered indicators of the small-world-ness property and are sometimes associated with higher resilience.
```



## Density
> The density  of a graph is a measure of how many ties between nodes exist compared to how many edges between nodes are possible, given the graph size (number of nodes) and the graph order (number of links)
$d={2m \over (n)(n-1)}$

Denser networks are less vulnerable to disruption due to the removal of key nodes.

## Connected Network & Components
A network is connected if there is a path between every two nodes.

Component is a maximum connected subgraph. Assume $G= (N, E)$ is a network, then the component of G must satisfy the following rules:
- ($N', E' $) must be a subset of $(N, E)$
- ($N', E' $) must be connected
- $i$ in $N'$ and $ij$ in E must imply $j$ in $N'$ and $ij$ in $E'$

```{figure} images/ch4/component.png
---
height: 350px
name:  com
---
How many components are there in this graph?
```

### Connectivity
Connectivity minimum number of nodes that need to be removed to separate the remaining nodes into two or more components. How hard it is to disconnect a graph by removing vertices or edges. 

By Menger’s theorem, this is equal to the number of node independent paths (paths that share no nodes other than source and target

## Homophily 
>“Birds of a feather flock together”
- age, race, gender, religion, profession…
- opportunity – contact theory
- benefits/costs
- social pressure
- social competition...

### Strength of Weak Ties
```{figure} images/ch4/homo.png
---
height: 150px
name:  homo
---
“strong friendships” - cross-group links less than half as frequent
```

### Assortativity
```{figure} images/ch4/assort.png
---
height: 150px
name:  path
---
Assortatitivy
```

Is there a tendency of nodes with the same magnitude of the degree to connect to each other, or are large-degree nodes primarily connected to low-degree nodes? 

> Assortativity measures the similarity of connections in the graph with respect to the node degree.


## Local Structures
### Clustering
Basic idea: how dense is a network at a local level?

e.g. What fraction of the people who I'm friends with, are friends with each other?

Clustering looks at if we have a given node $i$, and we look at two of $i$'s friends j and k, what's the chance that those two are related to each other?


Local clustering coefficient:
For a node $i$ in graph $g$, we have the local clustering coefficient $Ci(g)$ calculated as:  
$\#\{$ $kj$ in $g$ | $k, j$ in $N_i(g)\}$}    
divided by  
$\#\{$ $kj$ | $k, j$ in $N_i(g)\}$  


Average clustering coefficient:
$C^{avg}(g) ={∑_i C_i(g) \over n}$


### Triads
A triangle is a set of three nodes where each node has a relationship to the other two.
> In the context of social networks, three individuals $x, y, z$ such $x$ and $z$ are both friends of $y$ are called a triad centered at $y$. 


#### Triadic Closure
> The triad is said to be open if the link from $x$ to $z$ is missing. A closed triad centered at $y$ is a particular triad centered at $y$ with the additional link from $x$ to $z$. The process of closing an open triad is called 
triadic closure.

![TC](https://mw2016.museumsandtheweb.com/wp-content/uploads/2016/01/espinos-figure1.png)


#### Transitivity
Transitivity is the overall probability for the network to have adjacent nodes interconnected, thus revealing the existence of tightly connected communities (or clusters, subgroups, cliques). It is calculated by the ratio between the observed number of closed triplets and the maximum possible number of closed triplets in the graph. 

$T={\# of Triads \over \# of connected Triads}$

```{figure} images/ch4/trans.png
---
height: 350px
name:  trans
---
```

### Cliques
> Cliques are identified by their size k, which is the number of nodes that are present in the clique.

A triangle is what we would consider to be a k-clique where k=3.

#### Maximal Cliques
> A maximal clique is a clique that cannot be extended by including one more adjacent vertex, meaning it is not a subset of a larger clique. A maximum clique (i.e., clique of the largest size in a given graph) is therefore always maximal, but the converse does not hold.


### Motifs

> Motifs patterns of interconnections occurring in complex networks at numbers that are significantly higher than those in randomized networks

```{figure} images/ch4/motif.jpg
---
height: 350px
name:  motif
---
Motifs
```


#### Triad Motifs

```{figure} images/ch4/triads.png
---
height: 250px
name:  triad
---
Triad Census
```

The triads are numbered 1-16, and have a code associated with them. The code reads like this:

- The first number is the number of bidirectional edges.
- The second number is the number of single edges.
- The third number is the number of “non-existent” edges.

>A letter code to distinguish directed variations of the same triad—U for “up,” D for “down,” C for “circle,” and T for “transitive” (i.e., having 2 paths that lead to the same endpoint).

Triads 1-3 in the figure are unconnected, triads 4-8 and 11 represent variations on structural holes, and triads 9,10 and 12-16 are variations on closed triads.


Important triads:
- structural-hole triads (code 201)
- closed triads (code 300).

The ratio between the structural holes and closed triads is also important—a hierarchy is largely composed of structural holes, while more egalitarian structures would have a higher ratio of closed triads.