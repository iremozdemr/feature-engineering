import pandas as pd
from sklearn.preprocessing import MinMaxScaler

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
pd.set_option('display.float_format', lambda x: '%.3f' % x)
pd.set_option('display.width', 500)

data = {
    'a': [14, 90, 56, 32, 85],
    'b': [400, 200, 300, 600, 700]
}

df = pd.DataFrame(data)

print("original dataset")
print(df)

scaler = MinMaxScaler()
#minmaxscaler nesnesi oluşturma

scaled_data = scaler.fit_transform(df)
print(type(scaled_data))
#veriyi dönüştürme

scaled_df = pd.DataFrame(scaled_data, columns=df.columns)
#dönüştürülmüş veriyi dataframe'e çevirme

print("scaled dataset")
print(scaled_df)