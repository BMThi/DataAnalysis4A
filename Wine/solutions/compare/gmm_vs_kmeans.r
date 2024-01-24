ggarrange(
    fviz_pca(acp, col.ind=as.factor(resICL$classification), ellipse.type="norm", geom="point", axes=c(1,2)) + ggtitle("Cluster with GMM"),
    fviz_pca(acp,col.ind=as.factor(reskmeans$cluster), geom=c("point"), axes=c(1,2)) + ggtitle("Cluster with Kmeans") 
)

# --- #

conf_mat = confusion_matrix(targets=resICL$classification, predictions=reskmeans$cluster )
plot_confusion_matrix(conf_mat)