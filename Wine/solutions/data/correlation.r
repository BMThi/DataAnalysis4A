M = cor(wine[,-c(1,2)])

corrplot(M, method='number', type='upper')

# corrplot.mixed(M, lower='circle', upper='number')