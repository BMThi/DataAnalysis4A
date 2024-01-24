table('CAH'=ClassK3, 'Kmean'=reskmeans$cluster)

# --- #

# With the confusion matrix
conf_mat = confusion_matrix(targets=ClassK3, predictions=reskmeans$cluster )
plot_confusion_matrix(conf_mat)