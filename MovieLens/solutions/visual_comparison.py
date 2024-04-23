# Visual comparison

print("User %i: A %i year old" % (user_idx, A), G, O,'\n')

fig, axes = plt.subplots(1, 2, figsize=(20, 10), sharex=True)

# ----- #

ax = axes[0]
cmap = plt.get_cmap('tab20', len(genre))
cmap = colors.ListedColormap(cmap.colors[predicted_movies['Genre'].values.squeeze().tolist()])

ax.barh(predicted_movies['Title'].values, predicted_movies['Rating'].values,  height=0.8, color=cmap.colors)
ax.set_title('Predicted movies', fontdict={"fontsize": 20})
ax.tick_params(axis="both", which="major", labelsize=15)

# ----- #

ax = axes[1]
cmap = plt.get_cmap('tab20', len(genre))
cmap = colors.ListedColormap(cmap.colors[favorite_movies['Genre'].values.squeeze().tolist()])

ax.barh(favorite_movies['Title'].values, favorite_movies['Rating'].values,  height=0.8, color=cmap.colors)
ax.set_title('Favorite movies', fontdict={"fontsize": 20})
ax.tick_params(axis="both", which="major", labelsize=15)

plt.subplots_adjust(top=0.90, bottom=0.05, wspace=0.50, hspace=0.3)
plt.show()