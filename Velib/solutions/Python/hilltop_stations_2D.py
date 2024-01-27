plt.figure(figsize = (8, 8))

sctrplt = plt.scatter(coord['latitude'], coord['longitude'], 
                      c = coord['bonus'], cmap = sns.color_palette('tab20b', as_cmap=True))

plt.xlabel('Latitude', fontsize = 10)
plt.ylabel('Longitude', fontsize = 10)
plt.title('Hilltop stations', fontsize = 15)
plt.legend(handles = sctrplt.legend_elements()[0], labels = ["No hill", "Hill"], fontsize = 10)

plt.show()