#çok değişkenli aykırı değer analizi = local outlier factor = lof:
#yoğunluğa bakılırak aykırı değerler bulunur
#eğer bir nokta komşu noktalara göre daha izole bir konumdaysa bu nokta aykırı değerdir

#17 yaşında olmak aykırı değer değildir
#3 kere evlenmiş olmak aykırı değer değildir
#17 yaşında olmak ve 3 kere evlenmiş olmak aykırı değerdir

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from click import style
from sklearn.neighbors import LocalOutlierFactor

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
pd.set_option('display.float_format', lambda x: '%.3f' % x)
pd.set_option('display.width', 500)

df = sns.load_dataset("diamonds")
df = df.select_dtypes(include=["float64","int64"])
df = df.dropna()
df.head()
#verisetinden sadece sayısal değişkenler seçilir
#verisetinden sayısal olmayan değişkenler silinir

def outlier_threshold(dataframe, column, q1=0.25, q3=0.75):
    quartile1 = dataframe[column].quantile(q1)
    quartile3 = dataframe[column].quantile(q3)
    interquartile_range = quartile3 - quartile1
    up = quartile3 + 1.5 * interquartile_range
    low = quartile1 - 1.5 * interquartile_range
    return low,up

def outlier_index(dataframe,column,print=False):
    low,up = outlier_threshold(df, column)

    if print:
        if dataframe[dataframe[column] > up].any(axis=None):
            print(dataframe[dataframe[column] > up])
        if dataframe[dataframe[column] < low].any(axis=None):
            print(dataframe[dataframe[column] < low])

    index1 = dataframe[dataframe[column] > up].index
    index2 = dataframe[dataframe[column] < low].index
    return index1.append(index2)

def outlier_number(dataframe,column):
    return len(outlier_index(dataframe,column))

df.columns

outlier_number(df,"carat")
outlier_number(df,"depth")
outlier_number(df,"table")
outlier_number(df,"price")
outlier_number(df,"x")
outlier_number(df,"y")
outlier_number(df,"z")
#değişkenlere ayrı ayrı bakıldığında outlier sayısı fazla çıkar

clf = LocalOutlierFactor(n_neighbors=20)
clf.fit_predict(df)
scores = clf.negative_outlier_factor_

sorted_scores = np.sort(scores)
sorted_scores_df = pd.DataFrame(sorted_scores)
sorted_scores_df.plot(stacked=True,xlim=[0,50],style=".-")
plt.show()

threshold = sorted_scores[3]
outliers = [value for value in sorted_scores if value < threshold]
outliers_rows = df[scores < threshold]

#LocalOutlierFactor:
#sklearn kütüphanesindeki bir sınıf
#lof algoritmasını uygulamak için kullanılır

#n_neighbors:
#bu parametre her bir veri noktasının değerlendirilmesinde dikkate alınacak komşu sayısını belirtir
#her bir veri noktasının en yakın 20 komşusuna bakılarak yoğunluk değerlendirilir

#clf.fit_predict():
#bu method verilen veri setini kullanarak modelin eğitimini yapar
#her veri noktasının outlier olup olmadığını belirtir
#outlier olan noktalar için -1 döner
#outlier olmayan noktalar için 1 döner

#clf.negative_outlier_factor_:
#her bir veri noktasının outlier olma olasılığını belirten bir dizi döner
#daha küçük değerler outlier olmaya daha yakın değerlerdir