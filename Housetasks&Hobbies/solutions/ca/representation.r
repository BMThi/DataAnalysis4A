# cos2: quality of representation of rows
res.ca$row$cos2

# -- #
print("")

i = 1
idx = which.max(res.ca$row$cos2[,i])

print(paste("The", row.names(housetasks)[idx], "task is best represented by axis", i))