contrib = famd.column_contributions_.style.format('{:.2%}')
display(contrib.highlight_max(color='orange').highlight_min(color='lightblue'))