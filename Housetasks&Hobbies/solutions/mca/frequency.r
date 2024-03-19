# Hobbies
par(mfrow=c(3,6))
I = 18
for (i in 1:I) {
  plot(hobbies[,i], main=colnames(hobbies)[i],
       ylab = "Count", col="steelblue", las = 2)
  }

# -- #

# Sociodemographic variables
par(mfrow=c(2,4))
I = 4
for (i in 18+1:I) {
  plot(hobbies[,i], main=colnames(hobbies)[i],
       ylab = "Count", col="steelblue", las = 2)
  }