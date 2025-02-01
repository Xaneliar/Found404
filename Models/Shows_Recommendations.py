import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.feature_extraction.text import TfidfVectorizer,CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity,cosine_similarity,linear_kernel
from ast import literal_eval
import warnings
from scipy.sparse import csr_matrix
warnings.filterwarnings('ignore')

df2 = pd.read_csv('datasets/TMDB_tv_dataset_v3.csv')
m = df2['vote_count'].quantile(0.9)
C = df2['vote_average'].mean()

def weight_average(x):
    v = x['vote_count']
    R = x['vote_average']
    return (v/(v+m))*R + (m/(v+m))*C

q_tvshows = df2.copy().loc[df2['vote_count'] >= m]
q_tvshows['score'] = q_tvshows.apply(weight_average , axis = 1)
q_tvshows = q_tvshows.sort_values('score' , ascending = False)
tfidf = TfidfVectorizer( stop_words='english' )
df2['overview'] = df2['overview'].fillna('')
tfidf_matrix = tfidf.fit_transform(df2['overview'])
tfidf_matrix_sparse = csr_matrix(tfidf_matrix)

tfidf_matrix_subset = tfidf_matrix[:30000]
cosine_sim = linear_kernel(tfidf_matrix_subset, tfidf_matrix_subset)

indices = pd.Series(df2.index, index=df2['name']).drop_duplicates()
def get_recommendations(title,cosine_sim = cosine_sim):
    idx = indices[title]
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1:11]
    tvshow_indices = [i[0] for i in sim_scores]
    return df2['name'].iloc[tvshow_indices]

if __name__ == "__main__":
    print(get_recommendations('Breaking Bad')).tolist()