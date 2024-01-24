R_pred = W.dot(H)

err = np.linalg.norm(R - R_pred) / (R.shape[0]*R.shape[1])
print("Average reconstruction error: %0.5f%%" % (err * 100))