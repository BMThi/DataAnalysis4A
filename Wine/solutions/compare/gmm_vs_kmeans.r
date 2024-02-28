grid.arrange(
    fviz_pca(pca, col.ind=as.factor(reskmeans$cluster), geom=c("point"), axes=c(1,2)) + ggtitle("Cluster with Kmeans"),
    fviz_pca(pca, col.ind=as.factor(resICL$classification), ellipse.type="norm", geom="point", axes=c(1,2)) + ggtitle("Cluster with GMM"),
    ncol=2
)

# --- #

conf_mat = confusion_matrix(targets=resICL$classification, predictions=reskmeans$cluster )
plot_confusion_matrix(conf_mat)