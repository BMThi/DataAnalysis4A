# seq = list(titanic.columns[ titanic.nunique() > .5*titanic.shape[0] ])

print('=== Non-meaningful columns ===')
print('Remove the columns:', ['alive', 'embark_town', 'pclass'])

# --- #
# Alive vs. Survived

titanic.drop('alive', axis=1, inplace=True)
titanic['survived'] = titanic['survived'].astype('category')
titanic['survived'] = titanic['survived'].cat.rename_categories({0: 'No', 1:'Yes'})

# --- #
# Embark_town vs Embarked

titanic.drop('embark_town', axis=1, inplace=True)
titanic['embarked'] = titanic['embarked'].astype('category')
titanic['embarked'] = titanic['embarked'].cat.rename_categories({'S': 'Southampton', 'C':'Cherbourg', 'Q':'Queenstown'})

# --- #
# Pclass

titanic.drop('pclass', axis=1, inplace=True)


# --- # --- #

print('')
print('=== Missing values ===')
print('Columns containing missing values are:', list(titanic.columns[titanic.isnull().sum()!=0]))

# --- #
# Embarked

print('')
print('Embarked - Rate of missing values:', titanic['embarked'].isnull().sum()/titanic.shape[0]*100)

E = titanic['embarked'].mode()[0]
titanic.fillna({'embarked': E}, inplace=True)

print('Port with more frequent boarding:', E)
print('--> We fill _embarked_ with', E)

# --- #
# Age

print('')
print('Age - Rate of missing values: {:.2f}%'.format(titanic['age'].isnull().sum()/titanic.shape[0]*100))
print('Age is a quantitative variable')
print('--> We fill _age_ with the median of titanic[age]')

titanic.fillna({'age': titanic['age'].median()}, inplace=True)

# --- #
# Deck

print('')
print('Deck - Rate of missing values: {:.2f}%'.format(titanic['deck'].isnull().sum()/titanic.shape[0]*100))

sns.catplot(data=titanic, x="deck", kind="count")
plt.plot()

print('The deck variable has too many missing values + It makes no sense to use the most common category here.')
print('--> We remove it from the dataset')

titanic.drop('deck', axis=1, inplace=True)

# --- #
# family_size
titanic['family_size'] = titanic['sibsp'] + titanic['parch']

# --- #

print('')
print('=== Checking ===')
print(titanic.isnull().sum())