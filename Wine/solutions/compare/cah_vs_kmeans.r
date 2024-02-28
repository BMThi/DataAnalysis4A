grid.arrange(
    fviz_pca(pca, col.ind=as.factor(reskmeans$cluster), geom=c("point"), axes=c(1,2)) + ggtitle("Cluster with Kmeans"),
    fviz_pca(pca, col.ind=as.factor(reshclust), ellipse.type="norm", geom="point", axes=c(1,2)) + ggtitle("Cluster with CAH"),
    ncol=2
)