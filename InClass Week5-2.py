#!/usr/bin/env python
# coding: utf-8

# In[17]:


get_ipython().run_line_magic('matplotlib', 'inline')


# In[18]:


import json
import random

import numpy as np
import pandas as pd
import networkx as nx


# In[19]:


actor_map = {}
movie_actor_map = {}
actor_genre_map = {}

with open("imdb_movies_2000to2022.prolific.json", "r") as in_file:
    for line in in_file:
        
        this_movie = json.loads(line)
        
        for actor_id, actor_name in movie['actors']:
            actor_map[actor_id]= actor_name
            
        for actor_id, actor_name in movie['actors']:
            actor_genre= actor_genre_map.get(actor_id, {})
            
            for i in movie['genres']:
                actor_genre[g]= actor_genre.get(g,0) +1
                
            actor_genre_map[actor_id]= actor_genre
            
        movie_actor_map[movie["imdb_id"]] = ({
            "movie": movie["title"],
            "actors": set([item[0] for item in movie['actors']]),
            "genres": movie["genres"]
        })
 


# In[20]:


index = actor_genre_map.keys()
rows = [actor_genre_map[k] for k in index]
df = pd.DataFrame(rows, index=index)
df = df.fillna(0)

df


# In[21]:


actor_genre_map['nm0000129']


# In[22]:


from sklearn.metrics import DistanceMetric
dist = DistanceMetric.get_metric('cosine')
x='nm0000129'
y='nm0147147'
dist.pairwise(x,y)


# In[23]:


from sklearn.metrics import DistanceMetric
dist = DistanceMetric.get_metric('euclidean')
x='nm0000129'
y='nm0147147'
dist.pairwise(x,y)

