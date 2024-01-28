rng = np.random.default_rng(12)

noisy = rng.normal(digits.data, 4)
plot_digits(noisy)