## Visualization on the Paris map
# Weekly average at 6 p.m.

h = 18
hours = np.arange(h, 168, 24)
load_per_hour = loading_data[:, hours].mean(axis=1)

# --- # 

fig = px.scatter_mapbox(coord, lat = 'latitude', lon = 'longitude', 
                        mapbox_style = "carto-positron",
                        color = load_per_hour, color_continuous_scale = px.colors.sequential.Plasma_r, #size = load_per_hour,
                        zoom  = 10, opacity = .9,
                        title = 'Stations loading - Weekly average at {} h'.format(h))

fig.show()