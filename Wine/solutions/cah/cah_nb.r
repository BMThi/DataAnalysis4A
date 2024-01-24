options(repr.plot.width = 10, repr.plot.height = 6)

ggarrange(
    fviz_nbclust(wine2[,-c(1,2)], FUNcluster=hcut, method="wss") + ggtitle("Optional number of cluster according Elbow"),
    fviz_nbclust(wine2[,-c(1,2)], FUNcluster=hcut, method="silhouette") + ggtitle("Optional number of cluster according Elbow")
)