## Simple 2D representation
# Monday at 6h, 12h and 23h

options(repr.plot.width = 13, repr.plot.height = 10)
hours = c(6, 12, 23)

dfi = coord
p = list()
for (i in 1:length(hours)){
    dfi$loading = loading[,hours[i]]
    p[[i]] = ggplot(dfi, aes(x=longitude, y=latitude, color=loading)) + 
        geom_point() +
        labs(title = paste("Stations loading - Monday",hours[i],"h"))
}

do.call(grid.arrange,c(p, ncol=2))