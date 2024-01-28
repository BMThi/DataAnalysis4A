pca = PCA(2)  # projection from 64 to 2 dimensions

projected = pca.fit_transform(digits.data)

print('--- PCA ---')
print('Initial dimension:', digits.data.shape)
print('Dimension after projection:', projected.shape)

print('')

print('--- Explained variance ---')
print('Component 1:', round(pca.explained_variance_[0],2), 'i.e.', round(100*pca.explained_variance_ratio_[0],2), '% of the total variance')
print('Component 2:', round(pca.explained_variance_[1],2), 'i.e.', round(100*pca.explained_variance_ratio_[1],2), '% of the total variance')

# print(pca.components_[:2])