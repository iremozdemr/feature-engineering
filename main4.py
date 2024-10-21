#eksik değerlerle baş etme yöntemleri:
#silme
#değer atama
#tahmine dayalı yöntemler

#eksik değerlerin türleri:
#tamamen rastgele = mcar = missing completely at random
#kısmen rastgele = mar = missing at random
#rastgele değil = mnar = missing not at random

#eksik verinin rassallığı

import pandas as pd

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
pd.set_option('display.float_format', lambda x: '%.3f' % x)
pd.set_option('display.width', 500)

df = pd.read_csv("datasets/titanic.csv")
df.head()

#df.isnull() yerine df.isna() da kullanılabilir

df.isnull()
#tüm veri setinde null değerleri ve null olmayan değerleri gösterir

df.isnull().values
#array şeklinde yazar

df.isnull().values.any()
#null değer varsa true döner
#hiç null değer yoksa false döner

df.isnull().sum()
#sütunlarda kaç tane null değer olduğunu gösterir
df.isnull().sum().sum()
#verisetinde toplam kaç tane null değere sahip satır sayısı olduğunu gösterir
df.notnull().sum()
#sütunlarda kaç tane null olmayan değer olduğunu gösterir
df.notnull().sum().sum()
#verisetinde toplam kaç tane null olmayan değere sahip satır sayısı olduğunu gösterir

columns_with_null_values = [column for column in df.columns if df[column].isnull().sum() > 0]
columns_with_no_null_values = [column for column in df.columns if df[column].isnull().sum() == 0]

def null_values_summary1(df):
    for column in df.columns:
        null_count = df[column].isnull().sum()
        not_null_count = df[column].notnull().sum()
        ratio = null_count / len(df[column]) * 100
        print(column, null_count, not_null_count,ratio)

def null_values_summary2(df):
    summary_data = {
        "column" : [],
        "null count": [],
        "not null count": [],
        "ratio": []
    }

    for column in df.columns:
        null_count = df[column].isnull().sum()
        not_null_count = df[column].notnull().sum()
        ratio = null_count / len(df[column]) * 100

        summary_data["column"].append(column)
        summary_data["null count"].append(null_count)
        summary_data["not null count"].append(not_null_count)
        summary_data["ratio"].append(ratio)

    summary_df = pd.DataFrame(summary_data)
    return summary_df

null_values_summary1(df)
null_values_summary2(df)