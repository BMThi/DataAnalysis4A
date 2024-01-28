options(repr.plot.width = 10, repr.plot.height = 10)

qmplot(data=coord, longitude, latitude, color=hill) +
    scale_color_hue(direction = -1) +
    labs(title = 'Hilltop stations')