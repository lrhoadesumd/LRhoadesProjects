#!/usr/bin/env python
# coding: utf-8

# In[19]:


get_ipython().run_line_magic('matplotlib', 'inline')


# In[20]:


import pandas as pd


# In[22]:


df = pd.read_csv("imdb_movies_2000to2022.actorXgenre.csv")

actor_name_map = {}
actor_genre_map = {}
movie_actor_map = {}

for _, row in df.iterrows():
    actor_id = row['actor_id']
    genres = [col for col in row.index if row[col] != 0]  # Extract genres from non-zero columns

    for genre in genres:
        this_actors_genres = actor_genre_map.get(actor_id, {})
        this_actors_genres[genre] = this_actors_genres.get(genre, 0) + 1
        actor_genre_map[actor_id] = this_actors_genres

    actor_name_map[actor_id] = actor_id  # Assuming there's no actor names in this data

    movie_actor_map[actor_id] = {
        "genres": genres,
        "actors": {actor_id},  # Store actors as a set
        "movie": actor_id  # Assuming there's no movie titles in this data
    }



# In[23]:


index = actor_genre_map.keys()
rows = [actor_genre_map[k] for k in index]

df = pd.DataFrame(rows, index=index)
df = df.fillna(0)
df


# In[24]:


cluster_model = KMeans(n_clusters=k)
cluster_model.fit(df)


# In[25]:


cluster_labels = cluster_model.predict(df)
actor_cluster_df = pd.DataFrame(cluster_labels, index=df.index, columns=["cluster"])
actor_cluster_df["cluster"].value_counts()


# In[26]:


for cluster,actors in actor_cluster_df.groupby("cluster"):
    print("Cluster:", cluster, "Size:", actors.shape[0])
    
    for a_id in actors.sample(5).index:
        print("\t", a_id, actor_name_map[a_id])


# In[ ]:




