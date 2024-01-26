## Visualization on the Paris map
# Days d at 6h, 12h and 23h

h = 18
hours = np.arange(h, 168, 24)
load_per_hour = loading_data[:, hours].mean(axis=1)

# --- # 

fig = px.scatter_mapbox(adds, lat = 'latitude', lon = 'longitude', 
                        mapbox_style = "carto-positron",
                        color = load_per_hour, color_continuous_scale = px.colors.sequential.Plasma_r, #size = load_per_hour,
                        zoom = 10, opacity = .9,
                        title = 'Stations loading - Weekly average at 6 p.m.')

fig.show()