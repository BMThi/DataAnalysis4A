def plot_pca(ax1=0, ax2=1, pca=pca, data=titanic_quanti):
  dataset = pca.transform(data)
  dataset.reset_index(inplace=True)
  sns.scatterplot(data = dataset,
                  x = ax1, y = ax2,
                  hue = 'survived', alpha=.7)

  plt.xlabel('Component {} — {:.2f}%'.format(ax1, pca.percentage_of_variance_[ax1]))
  plt.ylabel('Component {} — {:.2f}%'.format(ax2, pca.percentage_of_variance_[ax2]))
  plt.grid(True)
  plt.show()

plot_pca(0,1)
plot_pca(1,2)
plot_pca(0,2)