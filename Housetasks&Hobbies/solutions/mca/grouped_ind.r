fviz_mca_ind(res.mca, 
             label = "none", # hide individual labels
             habillage = "Exhibition", # color by groups 
             palette = c("steelblue", "orange"),
             #addEllipses = TRUE, ellipse.type = "confidence",
             ) 

fviz_mca_ind(res.mca, 
             label = "none", # hide individual labels
             habillage = "Gardening", # color by groups 
             palette = c("steelblue", "orange")
            ) 

fviz_mca_ind(res.mca, 
             label = "none", # hide individual labels
             habillage = "TV", # color by groups 
            ) 

# --- #

fviz_ellipses(res.mca, c("Exhibition", "Gardening", "TV"),
              geom = "point")

# plotellipses(res.mca, cex=0.2, magnify=12, keepvar=1:4)