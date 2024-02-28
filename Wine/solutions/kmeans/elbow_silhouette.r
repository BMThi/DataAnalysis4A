fviz_nbclust(wine2[,-c(1,2)], FUNcluster=kmeans, method="silhouette") +
    ggtitle("Silhouette score according to the number of clusters")