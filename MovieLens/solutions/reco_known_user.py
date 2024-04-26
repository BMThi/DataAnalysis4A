# Recommendations - known user

n_recommendations = 5

user_idx = np.random.randint(n_users)
user = users_df[users_df['User ID']==user_idx]

A = user.iloc[0]['Age']
G = user.iloc[0]['Gender']
O = user.iloc[0]['Occupation']
print("Recommended movies for user %i: A %i year old" % (user_idx, A), G, O,'\n')

# ----- #

ratings_user = R[user_idx, :]
predictions_user = R_pred[user_idx, :]

unseen_indices = np.where(ratings_user == 0)[0]
predictions_unseen = predictions_user[unseen_indices]

# ----- #

predicted_movies = pd.DataFrame(columns = ['Title', 'Rating', 'Genre'])
predicted_movies_index = np.argsort(-predictions_unseen)

for ii in predicted_movies_index[:5]:
    i = unseen_indices[ii]
    reco = {'Title':movies_df.iloc[i]['Title'], 
            'Rating':predictions_user[i], 
            'Genre':movies_df.iloc[i]['Genre']}
    reco = pd.DataFrame([reco])
    predicted_movies = pd.concat([predicted_movies, reco], axis=0, ignore_index=True)
    
predicted_movies