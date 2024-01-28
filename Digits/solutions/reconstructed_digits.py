d = 20
pca = PCA(d)  # project from 64 to 2 dimensions
projected = pca.fit_transform(digits.data)
reconstructed = pca.inverse_transform(projected)

print('MSE:', np.mean((digits.data - reconstructed)** 2))
print('')

# --- #
# Initial images

print('> Initial images')
fig = plt.figure(figsize=(6, 6))
fig.subplots_adjust(left=0, right=1, bottom=0, top=.5, hspace=0.05, wspace=0.05)

for i in range(32):
    ax = fig.add_subplot(4, 8, i + 1, xticks=[], yticks=[])
    ax.imshow(digits.data[i].reshape(8,8), cmap=plt.cm.binary, interpolation='nearest')
    ax.text(0, 7, str(digits.target[i]))
    
plt.show()
print('')

# --- #
# Reconstructed Images 

print('> Reconstructed images ')
fig = plt.figure(figsize=(6, 6))
fig.subplots_adjust(left=0, right=1, bottom=0, top=.5, hspace=0.05, wspace=0.05)

for i in range(32):
    ax = fig.add_subplot(4, 8, i + 1, xticks=[], yticks=[])
    ax.imshow(reconstructed[i].reshape(8,8), cmap=plt.cm.binary, interpolation='nearest')
    ax.text(0, 7, str(digits.target[i]))
    
plt.show()