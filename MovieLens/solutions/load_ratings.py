names = ['User ID', 'Movie ID', 'Rating']
ratings_df = pd.read_csv("ml-100k/u.data", sep="\t", usecols=[0,1,2], names=names)

ratings_df.head()