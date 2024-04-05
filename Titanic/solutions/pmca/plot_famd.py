def plot_famd(ax1=0, ax2=1, famd=famd, data=titanic_clip):
  dataset = famd.transform(data)
  dataset.reset_index(inplace=True)
  sns.scatterplot(data = dataset,
                  x = ax1, y = ax2,
                  hue = 'survived', alpha=.7)

  plt.xlabel('Component {} — {:.2f}%'.format(ax1, famd.percentage_of_variance_[ax1]))
  plt.ylabel('Component {} — {:.2f}%'.format(ax2, famd.percentage_of_variance_[ax2]))
  plt.grid(True)
  plt.show()