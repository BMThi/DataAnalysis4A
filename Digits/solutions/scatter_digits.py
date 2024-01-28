plt.figure(figsize = (8, 6))
plt.scatter(projected[:, 0], projected[:, 1],
            c = digits.target, alpha = 0.5,
            cmap = plt.cm.get_cmap('tab10_r', 10))

plt.xlabel('Component 1')
plt.ylabel('Component 2')
plt.colorbar()
plt.show()