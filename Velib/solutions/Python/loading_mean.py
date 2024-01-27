print('--- Average fill rate ---')
print(loading.mean().mean())

# --- #
print('')

loading_mean = pd.Series(loading.mean(axis=1))

print('--- Least crowded station, on average ---')
i = loading_mean.idxmin()
print('Average fill rate :',loading_mean[i])
print(coord.loc[i])

# --- #
print('')

print('--- Fullest station, on average ---')
i = pd.Series(loading.mean(axis=1)).idxmax()
print('Average fill rate :',loading.mean(axis=1)[i])
print(coord.loc[i])