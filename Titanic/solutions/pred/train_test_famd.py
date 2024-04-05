train, test = train_test_split(titanic_famd, test_size=0.2)

X_train = train[np.arange(5)].to_numpy()
y_train = train['survived'].to_numpy()

X_test = test[np.arange(5)].to_numpy()
y_test = test['survived'].to_numpy()

display(train)