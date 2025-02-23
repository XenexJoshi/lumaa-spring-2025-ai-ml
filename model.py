from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def recommend_movie(input, data, count = 5):
  vectorizer = TfidfVectorizer(stop_words = 'english', lowercase = True)
  train_tfid = vectorizer.fit_transform(data['processed'].tolist() + [input])

  cosine_sim = cosine_similarity(train_tfid[-1], train_tfid[:-1]).flatten()
  max_sim = cosine_sim.argsort()[::-1][:count]
    
  recommendations = data.iloc[max_sim]
  return recommendations[['title', 'plot_synopsis']], cosine_sim[max_sim]

def generate_result(input, df, count = 5):
  result, score = recommend_movie(input, df, count)
  count = 0
  for _, row in result[1:].iterrows():
    print(f"Title: {row['title']}")
    print(f"Similarity Score: {score[count]}")
    count += 1
    print(f"Description: {row['plot_synopsis']}")
    print('\n')
