from analysis import load_data, reshape_data

df = load_data()
df = reshape_data(df)

print(df.head())
print(df.shape)


