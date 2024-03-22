# Change the color by contrib values
fviz_ca_row(res.ca, col.row = "contrib",
             gradient.cols = c("blue", "yellow", "red"), 
             repel = TRUE)