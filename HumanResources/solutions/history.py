cols = ['YearsAtCompany', 'YearsInCurrentRole', 'YearsSinceLastPromotion']

fig,axes = plt.subplots(nrows=3, ncols=1, figsize=(10,10))

for i,c in enumerate(cols):
    sns.pointplot(x=data[c], y=data['TotalWorkingYears'], ax=axes[i], hue=data['Attrition'], palette={'Yes':'mediumvioletred', 'No':'cornflowerblue'})
    axes[i].set_xlabel(c)
    axes[i].set_ylabel('TotalWorkingYears')

plt.tight_layout()
plt.show()