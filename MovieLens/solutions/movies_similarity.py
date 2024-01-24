movies_similarities = cosine_similarity(H.T)

plt.figure(figsize=(15,15))
plt.imshow(movies_similarities)
plt.title("Movies similarity matrix")
plt.show()