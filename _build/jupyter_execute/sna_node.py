#!/usr/bin/env python
# coding: utf-8

# Describing a node
# =======
# ![cen](https://miro.medium.com/max/4220/1*2aM28nzxiJKUdShS75bzEA.png)

# ## Centrality Measurements
# ```{note}
# First of all, how should we define centrality? It just indicates the node is "central" to the network, which could indicate some sort of importance, significance, or having an advantaged position. However, that there are lots of specific ways we can think of centrality, and thus different ways of mathematically defining the concept.
#  ```

# In[ ]:





#  ### Degree Centrality
# Degree centrality measures how connected is a node. Thus, the degree of a node is a simple measure of centrality in which more highly connected nodes rank higher. 

# In[1]:


import networkx as nx
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns


# In[2]:


G = nx.generators.social.florentine_families_graph()


# In[3]:


print("Node Degree")
for v in G:
    print(f"{v:4} {G.degree(v):6}")
fig, ax = plt.subplots(1, 1, figsize=(8, 6))
nx.draw_networkx(G, with_labels=True,ax=ax)

plt.show()


# We can also normalize the degree centrality by dividing by the maximum possible degree in a simple graph $n-1$ where $n$ is the number of nodes in $G$.

# In[4]:


sorted(nx.centrality.degree_centrality(G).items(), key=lambda item: item[1])


# #### In-degree & Out-degree Centrality
# The in-degree centrality for a node v is the fraction of nodes its **incoming** edges are connected to.
# The out-degree centrality for a node v is the fraction of nodes its **outgoing** edges are connected to.

# In[5]:


G_di=nx.fast_gnp_random_graph(10, 0.2, directed=True, seed=2021)
nx.draw_circular(G_di,  with_labels=True)


# In[6]:


print(G_di.degree)
print(G_di.out_degree)
print(G_di.in_degree)


# In[7]:


nx.degree_centrality(G_di)


# In[8]:


nx.out_degree_centrality(G_di)


# ### 

# ### Closeness Centrality
# Closeness centraloity is a measurement of the ease of reaching of other nodes. How far am I on average from other nodes? It is defined as $n-1 \over \sum_{j} L(i,j) $. L is the length of the shortest distance between node $i$ and $j$.
# 
# Or in simple words closeness is (number of nodes - 1) / sum(distance from node to all other nodes)

# In[9]:


sorted(nx.centrality.closeness_centrality(G).items(), key=lambda item: item[1])


# ### Decay Centrality
# Decay Centrality is very similar to closeness centrality as they all weighs the distance of the node to the rest of the nodes. Unlike closeness centraity, it is based of a decay parameter (0 < δ < 1).
# $\sum_{j\neq i} δ^{L(i,j)} $.
# 
# You have to decide the δ and the basic idea is my direct friend (l=1) get the value of $δ^1$ while my friend's friend got value of $δ^2$, to $δ^n$. Then you add them up and got this value.
# 
# Higher the δ, the more focus was put on close connections. It weights distance exponentially.
# 
# Normalized version: $\sum_{j\neq i} δ^{L(i,j)}  \over (n-1)δ$
# 
# $(n-1)δ$ is the lowest decay possible (where every node is directed connected)

# ### Betweenness Centrality
# The idea is idea here is that when we look at two nodes, i and j, we can keep track of the full number of shortest paths between i and j. And then for any k that's not equal to i and j, we can ask what's the number of those shortest paths that k lies on, between i and j. A formal definition would be:
# 
# $\sum_{i,j \neq k} {p_k(i, j) \over p(i, j)} $
# 
# In a mroe simple words, Betweennewhat's the fraction of shortest paths that k lies on between other nodes.
# 
# We can normalize the value by dividing it by $2 \over (n-1)(n-2)$

# In[10]:


sorted(nx.centrality.betweenness_centrality(G).items(), key=lambda item: item[1])


# ### Eigenvector Centrality
# Eigenvector centrality mesaures not only how many people you connect with, but also how many people are conneected with the people you are connected with. S the idea of eigenvector centrality is that your importance comes from being connected to other important.
# 
# $C_i$ is porportional to $\sum_{j:friends of i} C_j$
# 
# It actually shares similar idea of a Markov process. Those egenvalues are from the eigenvector of the transition matrix when reaching stationary distribution. 
# 

# In[11]:


sorted(nx.centrality.eigenvector_centrality(G).items(), key=lambda item: item[1])


# ### Kat'z Centrality
# Similar to eigenvector centrality, it used the weighted counts of all paths coming tot he node. The weight of path of lenght n is counted with attenuation factor. 
# $k_i = β \sum_{j}A_{ij} + β^2 \sum_{j}A^2_{ij}+ ... $

# In[12]:


sorted(nx.centrality.katz_centrality(G).items(), key=lambda item: item[1])


# ### Summary
# - Degree: connectness
# - Closeness: ease of reaching out nodes
# - Betweenness: role of being a connector, intermediary
# - Eigenvector: connecting to important people

# ```{figure} images/ch5/centrality.png
# ---
# height: 350px
# name:  path
# ---
# Comparison of centrality metrics
# ```

# In[ ]:




