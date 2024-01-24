max_ratings = n_ratings_ind.max()
user_max_ratings = users_df[users_df['User ID']==n_ratings_ind.argsort()[-1]]

A = user_max_ratings.iloc[0]['Age']
G = user_max_ratings.iloc[0]['Gender']
O = user_max_ratings.iloc[0]['Occupation']
print("The user who rated the most films is a %i year old" % A, G, O)
print("He/She has rated %i movies" % max_ratings)