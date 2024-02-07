clf = LogisticRegression(solver='newton-cholesky')
clf.fit(train_x, train_y)

# --- #

pred_y = clf.predict(test_x)

accuracy = accuracy_score(test_y, pred_y, normalize=True, sample_weight=None)
print('Accuray:',round(accuracy,3))
print(' ')

# --- #

print(classification_report(test_y, pred_y))