How to define a network?
============
![image](https://media.springernature.com/lw685/springer-static/image/art%3A10.1007%2Fs11192-020-03527-0/MediaObjects/11192_2020_3527_Fig1_HTML.png)
### A *formal* definition of a network

```{epigraph}
Networks are just **Graphs** in [Graph Theory](https://en.wikipedia.org/wiki/Graph_theory). 

```


Graphs are comprised of two sets of objects:

1. **A node set**: the "entities" in a graph.
2. **An edge set**: the "connections" between the entities in the graph.


Usually, we denote a graph as:  

$$
  G=<V,E>
$$

$V$ is the set of vertices and $E$ is the set of edges. Each edge $e$ in $E$ can be represented as $e_{ij}=(v_i, v_j)$, where $v_i$ and $v_j$ *must* be included in $V$. 


### Type of edges and graphs
- Edges might have intensity:
A tweet can be retweeted 10 times or 10000 times. If we want to distinguish this difference, we have to assign **weights** to the edges.
Graphs with weighted edges are **weighted graphs**.      
<br>
- Edges might have directions:
A person might have 10 friends but 10000 followers. Friends mean the person actively follows the other 10 accounts while his/her 10000 followers actively follow him/her. If we want to distinguish the difference, we have to separate the edges directing differently. 
Graphs with directed edges are **directed graphs**.


```{figure} images/ch2/typesofgraphs.png
---
height: 500px
name: four-types
---
Four Types of Graphs (based on Edge Types)
```

## Types of nodes and graphs
- Nodes can be of different kinds  
Nodes can be grouped into different types and the interactions occur between the groups of nodes. Networks with multiple kinds of nodes are called **multi-modal networks**. The most common one is the bimodal networks, a.k.a., **bipartite**.
```{figure} images/ch2/bimodal.jpeg
---
height: 500px
name: bi
---
[HBO shows and the actors bipartite](http://social-dynamics.org/projecting-bipartite-network-gephi/)
```

### Application of networks
This formal definition tells you the basics of every network. When you apply any network analysis techniques to your project, the first thing is to define what's in your network:
1. What does a vertex/node mean in your network?
    - humans, tweets, posts, airports, cells, etc.
2. What does a connection/edge mean in your network?
    - befriending, reposting, replying, citing, flying, interacting, etc.

For me, constructing a network is like making up an English sentence where nodes are *subjects* or *objects* and edges are the *predicates*. 

Next, you should consider what node/edge attributes are in your defined network, and should these attributes matter to your research?

3. Should I use weighted edges — if so, how?
   - What metrics should be used to represent weights?
   - What are the implications of using the metrics?
4. Should I use directed edges — if so, how?
5. Can I think of a property in this graph that represents a solution to my problem? If not:
    - Can I add properties to the nodes or edges that get me closer? 
    - Can I redefine the nodes or edges?

