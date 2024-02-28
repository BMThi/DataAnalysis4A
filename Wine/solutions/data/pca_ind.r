options(repr.plot.width = 10, repr.plot.height = 6)

grid.arrange(
    fviz_pca_ind(pca, axes=c(1,2), geom=c("point"), habillage=wine$Type),
    fviz_pca_ind(pca, axes=c(1,2), geom=c("point"), habillage=wine$Quality),
    ncol=2
)