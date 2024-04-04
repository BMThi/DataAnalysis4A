m = max(titanic['age'][titanic['who'] == 'child'])
print('To be considered as children, passengers must be under', int(m))