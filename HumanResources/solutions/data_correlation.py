plt.figure(figsize=(18,9))

# correlation between columns
sns.heatmap(data.corr(), annot=True, fmt='.1f')
plt.xticks(rotation=40)

plt.show()

# --- #

# strong correlation between columns
cols = ['Education','Age','MonthlyIncome','JobLevel','NumCompaniesWorked','TotalWorkingYears','YearsAtCompany',
       'YearsInCurrentRole', 'YearsSinceLastPromotion', 'YearsWithCurrManager']
sns.heatmap(data[cols].corr(), annot=True, fmt='.1f')
plt.xticks(rotation=40)
plt.show()