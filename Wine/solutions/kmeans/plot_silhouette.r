# Silhouette plots, according to the number of clusters
options(repr.plot.width = 15, repr.plot.height = 6)

# With 3 clusters
reskmeans = kmeans(wine2[,-c(1,2)], centers=3) 
sil = silhouette(reskmeans$cluster, dist(wine2[, -c(1:2)]))
p1 = fviz_silhouette(sil)

# With 4 clusters
reskmeans = kmeans(wine2[,-c(1,2)], centers=4) 
sil = silhouette(reskmeans$cluster, dist(wine2[, -c(1:2)]))
p2 = fviz_silhouette(sil)

grid.arrange(p1,p2,ncol=2)