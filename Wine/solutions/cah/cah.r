d = dist(wine2[,-c(1,2)], method="euclidean")

# Clustering
hclustsingle = hclust(d, method="single")
hclustcomplete = hclust(d, method="complete")
hclustaverage = hclust(d, method="average")

# --- #

#Dendograms visualization
options(repr.plot.width=10, repr.plot.height=10)

fviz_dend(hclustsingle, show_labels=FALSE, main='Dendrogram - Single linkage')
fviz_dend(hclustcomplete, show_labels=FALSE, main='Dendrogram - Complete linkage')
fviz_dend(hclustaverage, show_labels=FALSE, main='Dendrogram - Average linkage')