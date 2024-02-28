resBICall = mclustBIC(wine3, G=2:20)
summary(resBICall)

# --- #

resBICall = Mclust(wine3, G=2:20)
summary(resBICall)

fviz_mclust(resBICall, what="BIC")