#!/usr/bin/env python
# coding: utf-8

# Network models
# ======
# 
# ![DD](https://www.researchgate.net/profile/Arkadiusz-Jedrzejewski/publication/313905152/figure/fig4/AS:613956733378562@1523390100341/The-degree-distribution-for-the-ER-model-with-N-10-4-and-two-values-of-p-The-results_W640.jpg)

# In[2]:


import networkx as nx
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import math


# ## Erdos‐Renyi Random Graphs
# 
# The inception of Network Science. Random graph model is where the number of vertices $n$ is fixed, but the probability of an edge connecting any two vertices is $p$. Serves as a benchmark $G(n,p)$.
# 
# ```{note}
# *Neighborhood*:  $N_i(g)$ = {$j | ij$ in ${g}$} 
#  Set of nodes j where the link from i to j exist.
# Degree of i: $d_i=\#N_i(g)$. The degree of i is just counting the number of neighbors.
# 
#  ```
# 
# $log(n) \over log(d)$ was an approximation of the average path length and diameter.

# In[5]:


G_ER=nx.random_graphs.gnp_random_graph(10, 0.5, seed=2021)
nx.draw_networkx(G_ER)


# In[10]:


G_ER=nx.random_graphs.gnp_random_graph(10, 0.1, seed=2021)
nx.draw_networkx(G_ER)


# In[11]:


G_ER=nx.random_graphs.gnp_random_graph(10, 0.9, seed=2021)
nx.draw_networkx(G_ER)


# In[ ]:





# ### Six degree separation

# N= 6.7 Billion  
# 
# d= 50 (friends, relatives, etc..)
# 

# In[28]:


math.log(67000000000)/math.log(50)


# ### Degree Distribution
# Average Degree only tells a part of the story

# In[49]:


nx.draw_networkx(nx.star_graph(9))


# In[50]:


nx.star_graph(10).degree


# In[52]:


sum(([j for i, j in nx.star_graph(9).degree]))/10


# In[36]:


nx.draw_networkx(nx.path_graph(10))


# In[39]:


nx.path_graph(10).degree


# In[47]:


sum(([j for i, j in nx.path_graph(10).degree]))/10


# For ER graph, the chance that a given node has exactly d links, is just follows what's known as a binomial distribution.
# 
# If you want to approximate for large n and relatively small p, you will have poisson distribution.

# In[59]:


plt.hist(list(dict(nx.degree(nx.random_graphs.gnp_random_graph(10000, 0.001, seed=2021))).values()))
plt.show()


# In[67]:


plt.hist(list(dict(nx.degree(nx.random_graphs.gnp_random_graph(1000, 0.6, seed=2021))).values()))
plt.show()


# In[ ]:





# For ER Graph, the clustering coeeficient is p. The edge density.
# 
# 

# ```{figure} images/ch4/gnp.ong.png
# ---
# height: 350px
# name:  path
# ---
# Real-world vs ER Graph
# ```

# In[69]:


nx.average_clustering(nx.random_graphs.gnp_random_graph(1000, 0.6, seed=2021))


# ### How to enrich ER model?
# Erdos-Renyi networks gave us some insight in to why the average path links might be small. But one thing that they didn't do very well was give an of of clustering. One observes actually have clustering coefficients which look significantly different than what would have happened if we were just working with a Erdős–Rényi random network.
# 
# Erdos-Renyi model misses clustering because the clustering is on the ordering of p which is going to have to go to 0 unless the average degree is becoming very, very large. 
# 
# - Models to generate clustering
# - Models to generate other than Poisson degree distributions
# - Models to fit to data

# ## The idea of "Small world" network
# 
# Start with ring‐lattice and then randomly pick some links
# to rewire
# -  start with high clustering but high diameter  
# - as rewire enough links, get low diameter
# - don’t rewire too many, keep high clustering

# In[10]:


# nx.draw_networkx(nx.watts_strogatz_graph(10, 4,  0))


# In[9]:


nx.draw_circular(nx.watts_strogatz_graph(10, 4,  0))


# In[110]:


nx.average_clustering(nx.watts_strogatz_graph(10, 4, 0))


# In[111]:


nx.diameter(nx.watts_strogatz_graph(10, 4, 0))


# In[120]:


nx.average_shortest_path_length(nx.watts_strogatz_graph(10, 4, 0, seed=2020))


# In[112]:


nx.draw_circular(nx.watts_strogatz_graph(10, 4, 0.2, seed=2021))


# In[113]:


nx.average_clustering(nx.watts_strogatz_graph(10, 4, 0.2, seed=2020))


# In[116]:


nx.diameter(nx.watts_strogatz_graph(10, 4, 0.2, seed=2020))


# In[119]:


nx.average_shortest_path_length(nx.watts_strogatz_graph(10, 4, 0.2, seed=2020))


# In[121]:


nx.draw_circular(nx.watts_strogatz_graph(10, 4, 1, seed=2021))


# ## Summary

# Small world model: low diameter and high clustering coefficient  
# Scale-free model: power law degree distribution  
# Transitive model: high clustering coefficient  

# ## The next huge advance in network science: scale-free models
# 
# 
# ```{figure} images/powerlaw.png
# ---
# height: 350px
# name:  power law
# ---
# Node degree distribution
# ```

# 
# 
# ```{figure} http://www.coppelia.io/wp-content/uploads/2015/08/philprettyv4.png
# ---
# name:  Philosophy
# ---
# History of Philosophy
# ```

# In[ ]:




