components = pca.transform(noisy)
filtered = pca.inverse_transform(components)

plot_digits(filtered)