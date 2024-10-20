# veri ön işleme:
# çalışmalara başlamadan önce verinin uygun hale getirilmesi

# özellik mühendisliği:
# ham veriden değişken üretmek
# veri ön işleme başlığı altındadır

# datasets
# data retrieval
# data preparation
# modeling
# model evaluation
# deployment/monitoring

# aykırı değerler = outliers:
# doğrusal problemlerde aykırı değerlerin etkisi fazladır
# ağaç yöntemlerinde aykırı değerlerin etkisi azdır

# aykırı değerler nasıl belirlenir:
# sektör bilgisi
# standart sapma yaklaşımı
# z-skoru yaklaşımı
# tek değişkenli -> boxplot
# çok değişkenli -> lof

# iqr = interquartile range:
# q1 = veri setinin en alt %25'i
# q2 = veri setinin medyanı
# q3 = veri setinin en üst %75'i
# iqr = q3 - q1
# alt limit = q1 - (1.5 x iqr)
# üst limit = q3 + (1.5 x iqr)
# eğer bir değer bu limitlerin dışındaysa o değer aykırı değer kabul edilir

import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
pd.set_option('display.float_format', lambda x: '%.3f' % x)
pd.set_option('display.width', 500)

df = pd.read_csv("./titanic.csv")
df.head()

sns.boxplot(x=df["Age"])
plt.show()
# boxplot çizme

q1 = df["Age"].quantile(0.25)
# bu değişken küçükten büyüğe sıralandığında yüzde 25'deki değeri verir

q3 = df["Age"].quantile(0.75)
# bu değişken küçükten büyüğe sıralandığında yüzde 25'deki değeri verir

iqr = q3 - q1

up = q3 + (1.5 * iqr)
low = q1 - (1.5 * iqr)

df[(df["Age"] < low) | (df["Age"] > up)]
df[(df["Age"] < low) | (df["Age"] > up)].index