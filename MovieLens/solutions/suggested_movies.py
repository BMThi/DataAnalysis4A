# Suggested movies

n_recommendations = 5

watch_index = np.random.randint(0, len(movies_df["Title"]))
watch_title = movies_df.iloc[watch_index]['Title']
print("Suggested movies for user (without history) currently watching", watch_title,'\n')

# ----- #

movies_sim = movies_similarities[watch_index, :]
suggestions = np.argsort(-movies_sim)[1:n_recommendations + 1]

suggested_movies = pd.DataFrame(columns = ['Title', 'Genre', 'Similarity'])

for i in suggestions:
    suggest = {'Title':movies_df.iloc[i]['Title'], 
            'Similarity':movies_sim[i], 
            'Genre':movies_df.iloc[i]['Genre']}
    suggest = pd.DataFrame([suggest])
    suggested_movies = pd.concat([suggested_movies, suggest], axis=0, ignore_index=True)

suggested_movies