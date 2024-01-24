print("Favorite movies for user %i: A %i year old" % (user_idx, A), G, O,'\n')

# ----- #

favorite_movies = pd.DataFrame(columns = ['Title', 'Rating', 'Genre'])
favorite_movies_index = np.argsort(-ratings_user)

for i in favorite_movies_index[:5]:
    pref = {'Title':movies_df.iloc[i]['Title'], 
            'Rating':ratings_user[i], 
            'Genre':movies_df.iloc[i]['Genre']}
    pref = pd.DataFrame([pref])
    favorite_movies = pd.concat([favorite_movies, pref], axis=0, ignore_index=True)
    
favorite_movies