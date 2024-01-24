bad_movies, good_movies = [], []
for i in range(len(mean_ratings)):
    if mean_ratings[i] == 1:
        bad_movies.append(movies_df["Title"][i])
    if mean_ratings[i] == 5:
        good_movies.append(movies_df["Title"][i])

print("Flop - Example of movie with rating of 1:", np.random.choice(bad_movies))
print("Masterpiece - Example of movie with rating of 5:", np.random.choice(good_movies))