fviz_mca_var(res.mca, 
             col.var = c(rep(c("no","yes"),17),"no",rep("yes",4)),
             title = "Graph of the hobbies",
             repel = TRUE)