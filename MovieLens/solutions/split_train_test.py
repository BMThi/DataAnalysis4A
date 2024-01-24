R_shape = (n_users, n_items)
X = ratings_df[['User ID','Movie ID']].values
y = ratings_df['Rating'].values

# ----- #

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33)

R_train = make_R(X_train, y_train, R_shape)
R_test = make_R(X_test, y_test, R_shape)