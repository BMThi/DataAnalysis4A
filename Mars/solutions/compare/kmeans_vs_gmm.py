ConfusionMatrixDisplay(confusion_matrix(clusters_gmm, clusters_kmeans)).plot()

plt.xlabel('With the kmeans algorithm')
plt.ylabel('With the GMM algorithm')
plt.show()

# --- #

cm, clusters_kmeans_sorted = matchClasses(clusters_gmm, clusters_kmeans)

ConfusionMatrixDisplay(cm).plot()
plt.xlabel('With the kmeans algorithm')
plt.ylabel('With the GMM algorithm')
plt.show()