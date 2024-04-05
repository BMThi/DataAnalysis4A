# Age vs. Fare
sns.scatterplot(data=titanic, x="age", y="fare", hue="class")

plt.xlabel('Age')
plt.ylabel('Fare')
plt.title('Age vs. Fare')
plt.show()