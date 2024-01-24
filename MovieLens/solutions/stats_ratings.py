print(ratings_df["Rating"].describe())

print('\n_____ \n')

ratings = ratings_df["Rating"]
print("Range of ratings: %i to %i" % (ratings.min(), ratings.max()))
print("Mean score: %f" % (ratings.mean()))
print("Median score: %f" % (ratings.median()))