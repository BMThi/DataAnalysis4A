plt.figure(figsize=(10,8))

# --- #

plt.subplot(2,2,1)
sns.histplot(data, x="MaritalStatus", hue="OverTime", palette="rocket")
plt.title('Overtime by Marital Status')

# --- #

plt.subplot(2,2,2)
sns.histplot(data, x="Department", hue="OverTime", palette="rocket")
# plt.xticks(rotation=35)
plt.title('Overtime by Department')

# --- #

plt.subplot(2,2,3)
sns.histplot(data, x="Gender", hue="OverTime", palette="rocket")
plt.title('Overtime by Gender')

# --- #

plt.subplot(2,2,4)
sns.histplot(data, x='Age', hue='OverTime', palette="rocket", kde=True)
plt.title('Distribution of Age by OverTime')

plt.tight_layout()
plt.show()