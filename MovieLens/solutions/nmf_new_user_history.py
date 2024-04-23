# Recompute NMF

newR = np.r_[R, my_ratings.T]

new_nmf = NMF(n_components=20, init="nndsvda", max_iter=int(1e3))
new_nmf.fit(newR)
newW = new_nmf.transform(newR)
newH = new_nmf.components_

newR_pred = newW.dot(newH)
newR_pred[newR_pred > 5] = 5.
newR_pred[newR_pred < 1] = 1.