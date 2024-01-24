cmap = plt.get_cmap('tab20', len(genre))
cmap = colors.ListedColormap(cmap.colors[predicted_movies['Genre'].values.squeeze().tolist()])

plt.barh(predicted_movies['Title'].values, predicted_movies['Rating'].values, height=0.8, color=cmap.colors)
plt.title('Predicted movies for user %i' % user_idx)

plt.show()