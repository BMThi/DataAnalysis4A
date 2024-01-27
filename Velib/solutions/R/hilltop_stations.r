df = data.frame(size=c(sum(coord$bonus==0), sum(coord$bonus==1)),
                labels = c('No hill','Hill'))

ggplot(df, aes(x="", y=size, fill=labels)) +
    geom_bar(stat="identity", width=1) +
    geom_text(aes(label=size), position = position_stack(vjust = 0.5)) +
    coord_polar(theta = "y") +
    scale_color_hue(direction = -1) +  # to reverse the default colormap order
    theme_void()