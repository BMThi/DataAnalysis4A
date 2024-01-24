nmf = NMF(n_components=20, init='nndsvda', max_iter=int(1e3))
nmf.fit(R)
W = nmf.transform(R)
H = nmf.components_

print("Number of iterations: ", nmf.n_iter_)
print("Movies features shape (transpose(H)): ", H.T.shape)
print("Users features shape (W): ", W.shape)
print("Reconstruction of R shape (W.H): ", W.dot(H).shape)