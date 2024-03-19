idx = which.max(rowSums(res.ca$row$cos2[,c(1,2)]))
print(paste("In the CA plan, the", row.names(housetasks)[idx], "task is the best represented"))

idx = which.min(rowSums(res.ca$row$cos2[,c(1,2)]))
print(paste("In the CA plan, the", row.names(housetasks)[idx], "task is the worst represented"))

# --- #

quality = data.frame(rowSums(res.ca$row$cos2[,c(1,2)]))
colnames(quality) = "Representation"
quality

# --- #

# Color by cos2 values: quality on the factor map
fviz_ca_row(res.ca, col.row = "cos2",
             gradient.cols = c("blue", "yellow", "red"), 
             repel = TRUE)