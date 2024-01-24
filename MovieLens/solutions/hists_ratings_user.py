users_list = range(1, n_users+1)
n_ratings_ind = [np.count_nonzero(ratings_df["User ID"] == i) for i in users_list]
n_ratings_ind = np.array(n_ratings_ind)

# ----- #

binwidth_all = 10
bins_all = np.arange(min(n_ratings_ind), max(n_ratings_ind)+binwidth_all, binwidth_all)

threshold = 150
binwidth_threshold = 3
bins_threshold = np.arange(min(n_ratings_ind), 150+binwidth_threshold, binwidth_threshold)

# ----- #

plt.figure(figsize=(10,5))

plt.subplot(1,2,1)
plt.hist(n_ratings_ind, bins=bins_all, align="left")
plt.xlabel("Number of ratings")
plt.ylabel("Frequency: Number of users with this much ratings")

plt.subplot(1,2,2)
plt.hist(n_ratings_ind, bins=bins_threshold, align="left")
plt.xlabel("Number of ratings")
plt.ylabel("Frequency: Number of users with this much ratings")

plt.tight_layout()
plt.show()