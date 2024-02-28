options(repr.plot.width = 10, repr.plot.height = 6)

resBIC = Mclust(wine3, G=9, modelNames = "VVE")
fviz_cluster(resBIC, data=wine3, ellipse.type="norm", geom="point")

# --- #

aux = data.frame(
    label = paste("Cluster", resBIC$classification, sep=""), 
    proba = apply(resBIC$z, 1, max))

ggplot(aux, aes(x=label, y=proba)) + 
    geom_boxplot(colour=1:9, fill=1:9, alpha=.4)