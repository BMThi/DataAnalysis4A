loading_missing_value = loading.isna().sum().sort_values(ascending=False)

print('--- Loading ---')
print(loading_missing_value.sum())

# --- #
print('')

adds_missing_value = adds.isna().sum().sort_values(ascending=False)

print('--- Adds ---')
print(adds_missing_value)