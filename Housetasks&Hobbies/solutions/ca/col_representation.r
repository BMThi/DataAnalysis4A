idx = which.max(colSums(res.ca$col$cos2[,c(1,2)]))
print(paste("In the CA plan,", colnames(housetasks)[idx], "is the best represented"))

idx = which.min(colSums(res.ca$col$cos2[,c(1,2)]))
print(paste("In the CA plan,", colnames(housetasks)[idx], "is the worst represented"))

# --- #

quality = data.frame(rowSums(res.ca$col$cos2[,c(1,2)]))
colnames(quality) = "Representation"
quality

# --- #

# Color by cos2 values: quality on the factor map
fviz_ca_col(res.ca, col.col = "cos2",
             gradient.cols = c("blue", "yellow", "red"), 
             repel = TRUE)