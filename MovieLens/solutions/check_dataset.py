n_ratings = ratings_df.shape[0]
n_users = len(ratings_df["User ID"].unique())
n_items = len(ratings_df["Movie ID"].unique())

print("Total number of ratings in the dataset: %i" % (n_ratings))
print("Number of persons who rated movies: %i" % (n_users))
print("Number of rated movies: %i" % (n_items))