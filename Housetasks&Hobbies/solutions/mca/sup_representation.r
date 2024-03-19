df = data.frame(rowSums(res.mca$quali.sup$cos2[,c(1:2)]))
colnames(df) = "quality"
df = df %>% rownames_to_column()
#df

ggplot(df, aes(x=rowname, y=quality)) + 
    geom_col(fill='steelblue') +
    rotate_x_text(angle = 45)

# Order row names by quality values
ggplot(df, aes(x = reorder(rowname, quality), y = quality)) +
  geom_col(fill='steelblue')  +
  rotate_x_text(angle = 45)