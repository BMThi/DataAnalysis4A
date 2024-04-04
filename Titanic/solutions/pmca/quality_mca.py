quality_row = mca.row_cosine_similarities(titanic_quali).head(10).style.format('{:.3}')
display(quality_row)

quality_comun = mca.column_cosine_similarities(titanic_quali).style.format('{:.3}')
display(quality_comun.background_gradient())