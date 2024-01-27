# Stations in descending order of occurrence
station_names = coord.names.value_counts().sort_values(ascending=False)
print(station_names)

# --- #
print('')

# We display the station with the most occurrences, i.e. the station corresponding to the first line of 'station_name'.
name = station_names.index[0]
coord[coord.names == name]