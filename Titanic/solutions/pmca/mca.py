mca = prince.MCA(
    n_components=14,
    n_iter=10,
    copy=True,
    check_input=True,
    engine='sklearn',
    random_state=42
)
mca = mca.fit(titanic_quali)