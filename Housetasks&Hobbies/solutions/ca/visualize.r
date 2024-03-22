dt = as.table(as.matrix(housetasks))

# --- #

balloonplot(t(dt), main ="housetasks", xlab ="", ylab="",
            label = FALSE, show.margins = FALSE)

mosaicplot(dt, shade = TRUE, las=2,
           main = "housetasks")