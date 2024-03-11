ConfusionMatrixDisplay(confusion_matrix(clusters_kmeans, clusters_expert)).plot()
plt.xlabel('Expert ground truth')
plt.ylabel('With the GMM algorithm')
plt.show()

# --- #

cm, clusters_kmeans_sorted = matchClasses(clusters_expert, clusters_kmeans)

ConfusionMatrixDisplay(cm).plot()
plt.xlabel('Expert ground truth')
plt.ylabel('With the GMM algorithm')
plt.show()