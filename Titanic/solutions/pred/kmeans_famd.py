kmeans = KMeans(n_clusters=2, random_state=0, n_init='auto', init='k-means++')
kmeans = kmeans.fit(X)

y_pred_kmeans_famd = kmeans.labels_

kmeans_accuracy_famd = np.sum(y_pred_kmeans_famd==y)/y.shape[0]
print("Percentage of points correctly classified: {:.3f}%".format(100*kmeans_accuracy_famd))

ConfusionMatrixDisplay(confusion_matrix(y, y_pred_kmeans_famd)).plot()
plt.show()