train, test = train_test_split(titanic_mca, test_size=0.2)

X_train = train.drop('survived', axis=1).to_numpy()
y_train = train['survived'].to_numpy()

X_test = test.drop('survived', axis=1).to_numpy()
y_test = test['survived'].to_numpy()