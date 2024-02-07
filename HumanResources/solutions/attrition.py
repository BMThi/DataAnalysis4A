plt.figure(figsize=(10,8))

# --- #

plt.subplot(2,2,1)
sns.histplot(data, x="MaritalStatus", hue="Attrition", palette={'Yes':'mediumvioletred', 'No':'cornflowerblue'})
plt.title('Attrition by Marital Status')

# --- #

plt.subplot(2,2,2)
sns.histplot(data, x="Department", hue="Attrition", palette={'Yes':'mediumvioletred', 'No':'cornflowerblue'})
# plt.xticks(rotation=35)
plt.title('Attrition by Department')

# --- #

plt.subplot(2,2,3)
sns.histplot(data, x="Gender", hue="Attrition", palette={'Yes':'mediumvioletred', 'No':'cornflowerblue'})
plt.title('Attrition by Gender')

# --- #

plt.subplot(2,2,4)
sns.histplot(data, x='Age', hue='Attrition', palette={'Yes':'mediumvioletred', 'No':'cornflowerblue'}, kde=True)
plt.title('Distribution of Age by Attrition')

plt.tight_layout()
plt.show()