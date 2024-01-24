plt.hist(ratings_df["Rating"], bins=range(1, 7), align="left")
plt.xlabel("Rating")
plt.ylabel("Frequency")
plt.grid(True)