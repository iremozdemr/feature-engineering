#msno:
#eksik verileri görselleştirmek için kullanılır
#eksik verileri analiz etmek için kullanılır

#bar grafiği:
#her sütundaki eksik değer sayısını gösterir

#matrix grafiği:
#hangi değerlerin eksik olduğunu gösterir
#eksik değerler beyaz ile gösterilir
#eksik olmayan değerler siyah ile gösterilir

#dendrogram:
#eksik değerlerin hangi özellikler ile ilişkili olduğunu gösterir

import pandas as pd
import missingno as msno
import matplotlib.pyplot as plt

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
pd.set_option('display.float_format', lambda x: '%.3f' % x)
pd.set_option('display.width', 500)

df = pd.read_csv("datasets/titanic.csv")
df.head()

print(df.isnull().sum())

msno.bar(df,figsize=(8, 4))
msno.matrix(df,figsize=(8, 4))
msno.heatmap(df,figsize=(8, 4))

plt.show()