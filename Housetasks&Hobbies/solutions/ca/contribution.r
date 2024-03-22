# Contribution of rows (in %) to the definition of the dimensions.
res.ca$row$contrib

# -- #
print("")

i = 2
idx = which.max(res.ca$row$contrib[,i])

print(paste("The", row.names(housetasks)[idx], "task contributes most to dimension", i))