# cos2: quality of representation of rows
head(res.mca$var$cos2)

# --- #

i = c(1:2)

idx = which.max( rowSums(res.mca$var$cos2[,i]) )
hobby = row.names(res.mca$var$cos2)[idx]
if (idx >= nrow(res.mca$var$cos2)-4) {
    hobby = paste("cinema", hobby)
}
print(paste("The hobby best represented in Plan", i[1], '-', i[2], "is", hobby))

idx = which.min( rowSums(res.mca$var$cos2[,i]) )
hobby = row.names(res.mca$var$cos2)[idx]
if (idx >= nrow(res.mca$var$cos2)-4) {
    hobby = paste("TV", hobby)
}
print(paste("The hobby worst represented in Plan", i[1], '-', i[2], "is", hobby))