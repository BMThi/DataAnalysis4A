users = ratings_df["User ID"].values
movies = ratings_df["Movie ID"].values
ratings = ratings_df["Rating"].values

matrix_sparse = sparse.csr_matrix((ratings, (users, movies)), shape=(n_users+1, n_items+1))
R = matrix_sparse.todense()
R = np.array(R[1:, 1:])