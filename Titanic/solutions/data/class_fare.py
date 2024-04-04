# Class vs. Fare

sns.catplot(
    data=titanic, x='fare', y='class', hue='who',
    kind='violin', bw_adjust=.5, cut=0,
)
plt.title('Class vs. Fare')
plt.show()