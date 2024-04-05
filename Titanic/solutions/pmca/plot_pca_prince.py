pca.plot(titanic_quanti,
         x_component=0,
         y_component=1
         #color_rows_by='survived',
         #show_row_markers=True,
         #show_column_markers=True
)

# --- #

pca.plot(titanic_quanti,
         x_component=0,
         y_component=2,
         color_rows_by='survived',
         show_row_markers=True,
         show_column_markers=True
)

# --- #

pca.plot(titanic_quanti,
         x_component=1,
         y_component=2,
         color_rows_by='survived',
         show_row_markers=True,
         show_column_markers=True
)