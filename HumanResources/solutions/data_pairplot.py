cols = ['TotalWorkingYears', 'YearsAtCompany', 'YearsInCurrentRole', 'YearsSinceLastPromotion', 'Attrition']

sns.pairplot(data[cols], hue = 'Attrition', palette={'Yes': 'mediumvioletred', 'No': 'cornflowerblue'})
plt.show()