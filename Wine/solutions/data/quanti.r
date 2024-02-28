# boxplot
options(repr.plot.width = 8, repr.plot.height = 6)

df = melt(wine[,-c(1,2)]) #gathering all numeric variable
ggplot(df, aes(x=variable, y=value)) + 
    geom_boxplot(color=c(1:6), fill=1:6, alpha=.3)

# --- #

# boxplot - zoom
options(repr.plot.width = 12, repr.plot.height = 6)

df1 = melt(wine[,c(3,4,7,8)])
p1 = ggplot(df1) + aes(x=variable, y=value) + 
    geom_boxplot(color=c(1,2,5,6), fill=c(1,2,5,6), alpha=.3)

df2 = melt(wine[,c(5,6)])
p2 = ggplot(df2) + aes(x=variable, y=value) +
    geom_boxplot(color=c(3,4), fill=c(3,4), alpha=.3)

grid.arrange(p1, p2, ncol=2)

# --- #

# violin plot
options(repr.plot.width = 13, repr.plot.height = 6)

p1 = ggplot(df1) + aes(x=variable, y=value, color=variable, fill=variable) + 
    geom_violin(alpha=.3)

p2 = ggplot(df2) + aes(x=variable, y=value, color=variable, fill=variable) + 
    geom_violin(alpha=.3)

grid.arrange(p1, p2, ncol=2)