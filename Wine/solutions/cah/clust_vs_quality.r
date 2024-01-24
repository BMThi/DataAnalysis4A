# Clusters vs Quality of wine

table(ClassK3, wine$Quality)

# --- #

options(repr.plot.width = 10, repr.plot.height = 6)

ggarrange(
    fviz_pca(acp, col.ind=as.factor(ClassK3), geom=c("point"), axes=c(1,2)),
    fviz_pca_ind(acp, axes=c(1,2), geom=c("point"), habillage=wine$Quality)
)