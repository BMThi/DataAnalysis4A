# Clusters vs Type of wine

tbl = table(wine$Type, reshclust)
print(tbl)

options(repr.plot.width = 9, repr.plot.height = 6)
mosaicplot(tbl, color=c(2:4))

# --- #
options(repr.plot.width = 15, repr.plot.height = 6)

grid.arrange(
    fviz_pca(pca, axes=c(1,2), geom = c("point"), col.ind=as.factor(reshclust)),
    fviz_pca_ind(pca, axes=c(1,2), geom=c("point"), habillage=as.factor(reshclust)),
    fviz_pca_ind(pca, axes=c(1,2), geom=c("point"), habillage=wine$Type),
    ncol=3
)