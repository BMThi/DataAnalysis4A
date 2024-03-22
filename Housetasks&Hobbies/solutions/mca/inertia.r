head(res.mca$eig)

fviz_screeplot(res.mca, addlabels=TRUE)
fviz_screeplot(res.mca, addlabels=TRUE, ncp=21)