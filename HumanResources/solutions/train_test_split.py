X = data.drop(['Attrition'],axis=1)
Y = data['Attrition']

train_x, test_x, train_y, test_y = train_test_split(X, Y, test_size=0.3, random_state=20)