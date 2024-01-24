ggarrange(
    fviz_pca(acp,col.ind=as.factor(resICL$classification), geom=c("point"), axes=c(1,2)) + ggtitle("Cluster with GMM"),
    fviz_pca(acp,col.ind=as.factor(ClassK3), geom=c("point"), axes=c(1,2)) + ggtitle("Cluster with CAH") 
)

# --- #

conf_mat = confusion_matrix(targets=ClassK3, predictions=reskmeans$cluster)
plot_confusion_matrix(conf_mat)