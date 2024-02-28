p1 = ggplot(wine) +
    aes(x=Quality, color=Quality, fill=Quality) +
    geom_bar(alpha=.5)

p2 = ggplot(wine) +
    aes(x=Type, y=after_stat(prop), group=TRUE, fill=factor(after_stat(x)), color=factor(after_stat(x))) + 
    labs(fill="Type (%)", color="Type (%)") +
    geom_bar(alpha=.5)

grid.arrange(p1, p2, ncol=2)