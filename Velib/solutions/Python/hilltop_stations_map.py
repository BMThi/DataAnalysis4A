coord['hill'] = coord['bonus'].astype('category') # convert to categorical

# --- #

fig = px.scatter_mapbox(coord, lat = 'latitude', lon = 'longitude', 
                        mapbox_style = "carto-positron",
                        color = 'hill', 
                        color_discrete_map = {0:'midnightblue', 1:'plum'},
                        labels = {0: "hello", 1: "hi"},
                        zoom = 10, opacity = .9,
                        title = 'Hilltop stations')


fig.show()