h     = 18
hours = seq(h, 168, 24)
load_per_hour = rowMeans(loading[,hours])

df = coord
df$loading = load_per_hour

# --- #

options(repr.plot.width = 10, repr.plot.height = 10)

qmplot(data=df, longitude, latitude, color=loading) +
    labs(title = paste('Stations loading - Weekly average at',h,'h'))