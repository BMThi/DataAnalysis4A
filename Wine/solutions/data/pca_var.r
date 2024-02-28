options(repr.plot.width = 10, repr.plot.height = 8)

wine2 = wine
wine2[,-c(1,2)] = scale(wine[,-c(1,2)], scale=T, center=T) #sc
pca = PCA(wine2, quali.sup=c(1,2), scale.unit = TRUE, graph=FALSE)

# Visualisation of explained variance and variables
grid.arrange(
    fviz_eig(pca), 
    fviz_pca_var(pca,axes=c(1,2)),
    ncol=2
)

# -- #
# With ggarrange

ggarrange(
    fviz_eig(pca), 
    fviz_pca_var(pca,axes=c(1,2))
)