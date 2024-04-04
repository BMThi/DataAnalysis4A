# Survival Count

sns.catplot(data=titanic, x='survived', kind='count', hue='survived')

plt.xlabel('Survival Status')
plt.ylabel('Count')
plt.title('Survival Count')
plt.show()