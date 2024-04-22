import pandas as pd


file_paths = ["data/daily_sales_data_0.csv", "data/daily_sales_data_1.csv", "data/daily_sales_data_2.csv"]
dfs = [pd.read_csv(file) for file in file_paths]

df = pd.concat(dfs, ignore_index=True)


df = df[df['product'] == 'pink morsel']


df['sales'] = df['quantity'] * df['price'].replace('[\$,]', '', regex=True).astype(float)


df = df[['sales', 'date', 'region']]

output_file = "formatted_sales_data.csv"
df.to_csv(output_file, index=False)

