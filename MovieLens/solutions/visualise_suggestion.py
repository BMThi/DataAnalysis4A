# Visualise suggestion

cmap = plt.get_cmap('tab20', len(genre))
cmap = colors.ListedColormap(cmap.colors[suggested_movies['Genre'].values.squeeze().tolist()])

plt.barh(suggested_movies['Title'].values, suggested_movies['Similarity'].values, height=0.8, color=cmap.colors)
plt.title("Suggested movies for new user currently watching "+watch_title)

plt.show()