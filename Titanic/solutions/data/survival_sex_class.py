# Survival depending on sex and class

fig = sns.catplot(
    data=titanic,
    x='who', y='survived', col='class',
    hue='who', kind='bar',
    aspect=.6
)

plt.suptitle('Survival depending on sex and class')
fig.set_titles("{col_name} {col_var}")
fig.set_xticklabels(["Men", "Women", "Children"])
fig.set_axis_labels("", "Survival Rate")
fig.set(ylim=(0, 1))

plt.tight_layout()
plt.show()