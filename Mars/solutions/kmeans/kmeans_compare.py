K = 6
n_pixel_x = 300
n_pixel_y = 128

cmap = plt.get_cmap('Set3', K)

# --- #

kmeans_pca = KMeans(n_clusters=K, init='k-means++', n_init='auto')
clusters_pca = kmeans_pca.fit_predict(mars_reduced)
mars_image_pca = clusters_pca.reshape((n_pixel_x, n_pixel_y))

kmeans_full = KMeans(n_clusters=K, init='k-means++', n_init='auto')
clusters_full = kmeans_full.fit_predict(mars_data)
mars_image_full = clusters_full.reshape((n_pixel_x, n_pixel_y))

# --- #

plt.subplot(1,2,1)
plt.imshow(mars_image_pca, interpolation="nearest", aspect="auto", cmap=cmap)
plt.title("On the reduced data (PCA)")
plt.grid(False)

plt.subplot(1,2,2)
plt.imshow(mars_image_full, interpolation="nearest", aspect="auto", cmap=cmap)
plt.title("On the complete data")
plt.grid(False)

plt.tight_layout()
plt.show()