mca = prince.MCA(
    n_components=15,
    n_iter=20,
    copy=True,
    check_input=True,
    engine='sklearn',
    random_state=42
)
mca = mca.fit(titanic_thresh)

display(mca.eigenvalues_summary)
mca.scree_plot()