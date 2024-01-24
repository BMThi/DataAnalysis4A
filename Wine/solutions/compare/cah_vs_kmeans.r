ggarrange(
    fviz_pca(acp, col.ind=as.factor(ClassK3), ellipse.type="norm", geom="point", axes=c(1,2)) + ggtitle("Cluster with CAH"),
    fviz_pca(acp, col.ind=as.factor(reskmeans$cluster), geom=c("point"), axes=c(1,2)) + ggtitle("Cluster with Kmeans")
)