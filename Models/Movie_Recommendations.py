import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer,CountVectorizer
from sklearn.metrics.pairwise import linear_kernel,cosine_similarity
from ast import literal_eval
import warnings
warnings.filterwarnings('ignore')

df1 = pd.read_csv('datasets/tmdb_5000_credits.csv')
df2 = pd.read_csv('datasets/tmdb_5000_movies.csv')

df1.columns = ['id','title_x','cast','crew']
df2 = df2.merge(df1,on = 'id')
df2.head(5)

m = df2['vote_count'].quantile(0.9)
C = df2['vote_average'].mean()

def weight_average(x):
    v = x['vote_count']
    R = x['vote_average']
    return (v/(v+m))*R + (m/(v+m))*C

q_movies = df2.copy().loc[df2['vote_count'] >= m]
q_movies['score'] = q_movies.apply(weight_average , axis = 1)
q_movies = q_movies.sort_values('score' , ascending = False)

tfidf = TfidfVectorizer( stop_words='english' )
df2['overview'] = df2['overview'].fillna('')
tfidf_matrix = tfidf.fit_transform(df2['overview'])

cosine_sim = linear_kernel(tfidf_matrix, tfidf_matrix)

indices = pd.Series(df2.index, index=df2['title']).drop_duplicates()

def get_recommendations(title,cosine_sim = cosine_sim):
    idx = indices[title]
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1:11]
    movie_indices = [i[0] for i in sim_scores]
    return df2['title'].iloc[movie_indices]

features = ['cast', 'crew', 'keywords', 'genres']
for feature in features:
    df2[feature] = df2[feature].apply(literal_eval)
    
def get_director(x):
    for i in x:
        if (i['job'] == 'Director'):
            return i['name']
    return np.nan

def get_list(x):
    if (isinstance(x,list)):
        names = [i['name'] for i in x]
        if len(names) > 3:
            return names[:3]
        return names
    return []

df2['director'] = df2['crew'].apply(get_director)
features = ['cast', 'keywords', 'genres']
for feature in features:
    df2[feature] = df2[feature].apply(get_list)
    
def clean_data(x):
    if isinstance(x, list):
        return [str.lower(i.replace(" ", "")) for i in x]
    else:
        if isinstance(x, str):
            return str.lower(x.replace(" ", ""))
        else:
            return ''
        
features = ['cast', 'keywords', 'director', 'genres']
for feature in features:
    df2[feature] = df2[feature].apply(clean_data)
    
def create_soup(x):
    return ' '.join(x['keywords']) + ' ' + ' '.join(x['cast']) + ' ' + x['director'] + ' ' + ' '.join(x['genres'])
df2['soup'] = df2.apply(create_soup, axis=1)

count = CountVectorizer(stop_words='english')
count_matrix = count.fit_transform(df2['soup'])
cosine_sim2 = cosine_similarity(count_matrix, count_matrix)
df2 = df2.reset_index()
indices = pd.Series(df2.index, index=df2['title'])

if __name__ == "__main__":
    print(get_recommendations('The Conjuring')).tolist()