print('Number of duplicated lines:', data.duplicated().sum())
print('')

df = pd.DataFrame({
    'Unique':data.nunique(),
    'Null':data.isna().sum(),
    'NullPercent':data.isna().sum() / len(data),
    'Type':data.dtypes.values
})
display(df)