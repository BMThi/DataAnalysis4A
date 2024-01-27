options(repr.plot.width = 15, repr.plot.height = 6)

# --- #

time_tick = 1 + 24*(0:6)  # vector corresponding to the beginning of days

# select a station
i = sample.int(nrow(loading), 1)

df = melt(loading[i,])  #the function melt reshapes it from wide to long
df$time_range = 1:ncol(loading)

ggplot(df, aes(x=time_range, y=value)) + geom_line(col="darkorchid") +
    geom_vline(xintercept=time_tick, col="orange", linetype="dashed") +
    labs(title=velib$names[i])