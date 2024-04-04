titanic_quanti = titanic[['survived','age','fare','family_size']]
titanic_quanti = titanic_quanti.set_index('survived')

pca = prince.PCA(
    n_components=3,
    n_iter=10,
    rescale_with_mean=True,
    rescale_with_std=True,
    copy=True,
    check_input=True,
    engine='sklearn',
    random_state=42
)
pca = pca.fit(titanic_quanti)