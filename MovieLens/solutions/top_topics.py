topics_used = W[user_idx, :]
top_topics = topics_used.argsort()[: -3 - 1 : -1]
top_topics.sort()
print("Top topics: %i, %i, %i" % tuple(top_topics + 1))