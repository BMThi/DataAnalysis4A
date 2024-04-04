titanic_quali = titanic[['survived','embarked','class','who','alone']] #,'family_size'
titanic_quali = titanic_quali.astype('category')
titanic_quali = titanic_quali.set_index('survived')

pd.get_dummies(titanic_quali)