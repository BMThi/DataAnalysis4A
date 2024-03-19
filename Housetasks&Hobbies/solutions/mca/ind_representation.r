# Color by cos2 values: quality on the individual map
fviz_mca_ind(res.mca, col.ind = "cos2",
             gradient.cols = c("blue", "yellow", "red"))


# Cos2 of individuals on Dim.1 and Dim.2
fviz_cos2(res.mca, choice="ind", axes=1:2)