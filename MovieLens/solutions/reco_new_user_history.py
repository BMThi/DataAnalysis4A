# Make recommendations

n_recommendations = 5

ratings_user = newR[-1, :]
predictions_user = newR_pred[-1, :]


# ----- #
# Favorite movies

favorite_movies = pd.DataFrame(columns = ['Title', 'Rating', 'Genre'])
favorite_movies_index = np.argsort(-ratings_user)

for i in favorite_movies_index[:5]:
    pref = {'Title':movies_df.iloc[i]['Title'], 
            'Rating':ratings_user[i], 
            'Genre':movies_df.iloc[i]['Genre']}
    pref = pd.DataFrame([pref])
    favorite_movies = pd.concat([favorite_movies, pref], axis=0, ignore_index=True)
    

# ----- #
# Predicted movies

unseen_indices = np.where(ratings_user == 0)[0]
predictions_unseen = predictions_user[unseen_indices]

predicted_movies = pd.DataFrame(columns = ['Title', 'Rating', 'Genre'])
predicted_movies_index = np.argsort(-predictions_unseen)

for ii in predicted_movies_index[:5]:
    i = unseen_indices[ii]
    reco = {'Title':movies_df.iloc[i]['Title'], 
            'Rating':predictions_user[i], 
            'Genre':movies_df.iloc[i]['Genre']}
    reco = pd.DataFrame([reco])
    predicted_movies = pd.concat([predicted_movies, reco], axis=0, ignore_index=True)
    
    
# ----- #

print('Favorite movies:')
display(favorite_movies)
print('')
print('Predicted movies:')
display(predicted_movies)