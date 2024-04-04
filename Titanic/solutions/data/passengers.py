# Passengers distribution

fig = sns.catplot(data=titanic, x='who', kind='count', hue='sex')
fig.set_xticklabels(["Men", "Women", "Children"])

plt.xlabel('')
plt.ylabel('')
plt.title('Passenger distribution on the titanic — Sex ratio')
plt.show()

# --- #
print('')

fig = sns.catplot(data=titanic, x='class', kind='count', hue='who')
fig.set_xticklabels(["Men", "Women", "Children"])

plt.xlabel('')
plt.ylabel('')
plt.title('Passenger distribution on the titanic — Class filling')
plt.show()