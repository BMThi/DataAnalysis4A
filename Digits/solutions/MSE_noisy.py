print('--- Mean Squared Error ---')

MSE = np.mean((digits.data - noisy)** 2)
print('Noisy data:', round(MSE,2))

MSE = np.mean((digits.data - filtered)** 2)
print('Filtered data:', round(MSE,2))