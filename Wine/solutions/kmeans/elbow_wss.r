# The elbow method method use total within sum of square as metric

options(repr.plot.width = 9, repr.plot.height = 6)

fviz_nbclust(wine2[,-c(1,2)], FUNcluster=kmeans, method="wss") +
    ggtitle("Within sum of square (WSS) according to the number of clusters")