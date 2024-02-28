table('CAH'=reshclust, 'Kmean'=reskmeans$cluster)

# --- #

# With the confusion matrix
conf_mat = confusion_matrix(targets=reshclust, predictions=reskmeans$cluster )
plot_confusion_matrix(conf_mat)