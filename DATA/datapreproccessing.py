import pandas as pd
df = pd.read_csv(r"C:\Users\fozan\OneDrive\Desktop\GitHub\AI-Resume-Analyzer-And-Job-Match-Recommender\DATA\data.csv")
df= df[['category', 'resume_text', 'skills_list',
       'experience_years']]
print(df.info())
