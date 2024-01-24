print(R)
R_pred = W.dot(H)
R_pred[R_pred > 5] = 5.
R_pred[R_pred < 1] = 1.

print("")

print(R_pred.astype(np.int8))