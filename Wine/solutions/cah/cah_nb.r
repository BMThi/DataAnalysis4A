options(repr.plot.width = 12, repr.plot.height = 6)

grid.arrange(
    fviz_nbclust(wine2[,-c(1,2)], FUNcluster=hcut, method="wss") + ggtitle("WSS according to nb of clusters"),
    fviz_nbclust(wine2[,-c(1,2)], FUNcluster=hcut, method="silhouette") + ggtitle("silhouette according to nb of clusters"),
    ncol=2
)