# Stations in descending order of occurrence
station_name = adds.names.value_counts().sort_values(ascending=False)
print(station_name)

# --- #
print('')

# We display the station with the most occurrences, i.e. the station corresponding to the first line of 'station_name'.
name = station_name.index[0]
adds[adds.names == name]