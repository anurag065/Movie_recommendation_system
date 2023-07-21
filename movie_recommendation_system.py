# -*- coding: utf-8 -*-
"""Movie_recommendation_system.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1X9oVr20VrzbC4J3TrUPNx_z-roxpLmB2

1. Content based recommendation - Based on the content one likes
2. Popularity based recommendation - Based on Popularity
3. Collaborative based recommendation - watched by group of people and suggested to new user
"""

import numpy as np
import pandas as pd
from sklearn. feature_extraction. text import TfidfVectorizer
import difflib
from sklearn.metrics.pairwise import cosine_similarity

data= pd.read_csv('/content/movies.csv')
data.head(5)
data.shape

#selecting the relevant features
selected_features = ['genres','keywords','tagline','cast','director']
print(selected_features)

#replacing the null value with null string
for feature in selected_features:
  data[feature]= data[feature].fillna('')


#combining the coloumns
combined_features = data['genres']+' '+ data['keywords']+' '+ data['tagline']+' '+ data['cast']+' '+ data['director']
combined_features.head(3)

# converting the text data to feature vectors

vectorizer = TfidfVectorizer()
feature_vectors = vectorizer.fit_transform(combined_features)
print(feature_vectors)

#getting the similarity score using cosine similarity
#this will give you the similar data using the feature_vectors

cossim= cosine_similarity(feature_vectors)
print(cossim)
cossim.shape

#getting the movie name from the user
name =  input('Enter the name of the movie')

#creating a list with all the movie names given in the movie set

list_of_all_titles = data['title'].tolist()
print(list_of_all_titles)

#finding the close match for the movie name given by the user
find_close_match = difflib.get_close_matches(name, list_of_all_titles)
print(find_close_match)

close_match = find_close_match[0]
print(close_match)

#finding the index of the movie
index_of_movie = data[data.title==close_match]['index'].values[0]
print(index_of_movie)

# getting a list of similar movies

similarity_score = list(enumerate(cossim[index_of_movie]))
print(similarity_score)

"""first value represents the index of the movie and the second value represents the similarity"""

# sorting the movies based on their similarity score

sorted_similar_movies = sorted(similarity_score, key = lambda x:x[1], reverse = True)
print(sorted_similar_movies)

# print the name of similar movies based on the index

print('Movies suggested for you : \n')

i = 1

for movie in sorted_similar_movies:
  index = movie[0]
  title_from_index = data[data.index==index]['title'].values[0]
  if (i<30):
    print(i, '.',title_from_index)
    i+=1

"""# MOVIE RECOMMENDATION SYSTEM"""

import numpy as np
import pandas as pd
from sklearn. feature_extraction. text import TfidfVectorizer
import difflib
from sklearn.metrics.pairwise import cosine_similarity

data= pd.read_csv('/content/movies.csv')
data.head(5)
data.shape

#selecting the relevant features
selected_features = ['genres','keywords','tagline','cast','director']
#print(selected_features)

#replacing the null value with null string
for feature in selected_features:
  data[feature]= data[feature].fillna('')


#combining the coloumns
combined_features = data['genres']+' '+ data['keywords']+' '+ data['tagline']+' '+ data['cast']+' '+ data['director']
combined_features.head(3)

# converting the text data to feature vectors

vectorizer = TfidfVectorizer()
feature_vectors = vectorizer.fit_transform(combined_features)
#print(feature_vectors)

#getting the similarity score using cosine similarity
#this will give you the similar data using the feature_vectors

cossim= cosine_similarity(feature_vectors)
#print(cossim)
cossim.shape

#getting the movie name from the user
name =  input('Enter the name of the movie')

#creating a list with all the movie names given in the movie set

list_of_all_titles = data['title'].tolist()
#print(list_of_all_titles)

#finding the close match for the movie name given by the user
find_close_match = difflib.get_close_matches(name, list_of_all_titles)
#print(find_close_match)

close_match = find_close_match[0]
#print(close_match)

#finding the index of the movie
index_of_movie = data[data.title==close_match]['index'].values[0]
#print(index_of_movie)

# getting a list of similar movies

similarity_score = list(enumerate(cossim[index_of_movie]))
#print(similarity_score)

# sorting the movies based on their similarity score

sorted_similar_movies = sorted(similarity_score, key = lambda x:x[1], reverse = True)
#print(sorted_similar_movies)

# print the name of similar movies based on the index

print('Movies suggested for you : \n')

i = 1

for movie in sorted_similar_movies:
  index = movie[0]
  title_from_index = data[data.index==index]['title'].values[0]
  if (i<30):
    print(i, '.',title_from_index)
    i+=1

