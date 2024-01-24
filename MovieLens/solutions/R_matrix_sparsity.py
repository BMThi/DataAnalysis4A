sparsity = 1 - len(R.nonzero()[0]) / (R.shape[0] * R.shape[1])
print("Sparsity of R: %0.2f%%" % (sparsity * 100))