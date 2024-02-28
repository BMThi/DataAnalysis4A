options(repr.plot.width = 13, repr.plot.height = 6)

resICL = Mclust(wine3, G=3, modelNames="EVV")
# fviz_cluster(resICL, data=wine3, ellipse.type="norm", geom="point")

# --- #

aux = data.frame(
    label = paste("Cl", resICL$classification, sep=""), 
    proba = apply(resICL$z, 1, max))

p1 = ggplot(aux, aes(x=label, y=proba)) + geom_boxplot(colour=1:3, fill=1:3, alpha=.4)
p2 = fviz_cluster(resICL, data=wine3, ellipse.type="norm", geom="point") +
    ggtitle("") + theme(legend.position = "none")

grid.arrange(p1, p2, ncol = 2)