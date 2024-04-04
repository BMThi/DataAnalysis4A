# Age vs. Class

sns.catplot(
    data=titanic, x='age', y='class', hue='sex',
    kind="violin", bw_adjust=.5, cut=0, #split=True
)
plt.title('Age vs. Class')
plt.show()