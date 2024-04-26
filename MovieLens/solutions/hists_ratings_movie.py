movies_list = range(1, n_items+1)
mean_ratings = [ratings_df["Rating"][ratings_df["Movie ID"] == i].mean() for i in movies_list]
mean_ratings = np.array(mean_ratings)

binwidth = .1
bins = np.arange(min(mean_ratings), max(mean_ratings)+binwidth, binwidth)

plt.figure(figsize=(10,5))

plt.hist(mean_ratings, bins=bins, align="mid")
plt.xlabel("Average rating")
plt.ylabel("Frequency: number of movies with this average rating")

plt.show()