reshclust = cutree(hclustcomplete, 3)

# --- #

fviz_dend(hclustcomplete, k=3, show_labels=FALSE, rect=TRUE)