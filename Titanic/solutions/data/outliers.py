# Outliers detection

print('=== Outliers detection ===')
cpt = np.sum(titanic['fare']==0)
print('We will remove {:} lines'.format(cpt))

titanic = titanic[titanic['fare'] != 0]
print('"New" titanic dataset shape:', titanic.shape)

display(titanic)