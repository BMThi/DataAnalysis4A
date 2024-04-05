kmeans = KMeans(n_clusters=2, random_state=0, n_init='auto', init='k-means++')
kmeans = kmeans.fit(X)

y_pred_kmeans_mca = kmeans.labels_

kmeans_accuracy_mca = np.sum(y_pred_kmeans_mca==y)/y.shape[0]
print("Percentage of points correctly classified: {:.3f}%".format(100*kmeans_accuracy_mca))

ConfusionMatrixDisplay(confusion_matrix(y, y_pred_kmeans_mca)).plot()
plt.show()