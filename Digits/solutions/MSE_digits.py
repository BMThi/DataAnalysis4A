n = digits.data.shape[1]
MSE = np.zeros(n-1)

for d in range(n-1):
    pca = PCA(d+1)  # project from 64 to 2 dimensions
    projected = pca.fit_transform(digits.data)
    reconstructed = pca.inverse_transform(projected)
    MSE[d] = np.mean((digits.data - reconstructed)** 2)

# --- #

plt.plot(np.arange(1,n), MSE)

plt.title('MSE according to the dimension of the PCA space')
plt.xlabel('Number of components in the PCA')
plt.ylabel('MSE')
plt.show()