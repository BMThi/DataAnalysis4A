grid.arrange(
    fviz_pca(pca, col.ind=as.factor(reskmeans$cluster), geom=c("point"), axes=c(1,2)) + ggtitle("Cluster with Kmeans"),
    fviz_pca(pca,col.ind=as.factor(reshclust), geom=c("point"), axes=c(1,2)) + ggtitle("Cluster with CAH") ,
    fviz_pca(pca,col.ind=as.factor(resICL$classification), geom=c("point"), axes=c(1,2)) + ggtitle("Cluster with GMM"),
    ncol=3
)