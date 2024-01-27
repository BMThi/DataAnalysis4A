## Simple 2D representation
# Loading at 6pm, depending on the day of the week

options(repr.plot.width = 20, repr.plot.height = 15)

h = 18
hours = seq(h, 168, 24)
days  = list("Monday", "Tuesday", "Wednesday","Thursday", "Friday", "Saturday", "Sunday")

dfi = coord
p = list()
for (i in 1:7){
    dfi$loading = loading[,hours[i]]
    p[[i]] = ggplot(dfi, aes(x=longitude, y=latitude, color=loading)) + 
        geom_point() +
        labs(title = paste("Stations loading - ", days[i], h,"h"))
}

do.call(grid.arrange,c(p, ncol=3))