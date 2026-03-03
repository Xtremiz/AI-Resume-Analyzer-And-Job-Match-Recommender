import pandas as pd
import nltk_utils as d
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer

df = pd.read_csv(r"C:\Users\fozan\OneDrive\Desktop\GitHub\AI-Resume-Analyzer-And-Job-Match-Recommender\DATA\data.csv")

df["tags"] = df['resume_text']+df['skills_list']
df["tags"] = df["tags"].fillna("")
df= df[['tags','category']]


df["tags"]= df["tags"].apply(d.preprocess)
df["tags"]= df["tags"].apply(d.uniqueonly)
tfid = TfidfVectorizer(max_features=3000)

vector = np.array(tfid.fit_transform(df["tags"]))
similarity = cosine_similarity(vector)


