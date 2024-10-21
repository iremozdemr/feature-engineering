#kategorik değişken
#kategorik görünümlü kardinal değişkenler
#sayısal değişken
#sayısal görünümlü kategorik değişken

import pandas as pd

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
pd.set_option('display.float_format', lambda x: '%.3f' % x)
pd.set_option('display.width', 500)

df = pd.read_csv("datasets/titanic.csv")
df.head()

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

def check_outlier(dataframe,column):
    low,up = outlier_threshold(df, column)
    if dataframe[dataframe[column] > up].any(axis=None) or dataframe[dataframe[column] < low].any(axis=None):
        return True
    else:
        return False

#uç değerleri silme
def remove_outlier(dataframe,column):
    index = outlier_index(dataframe,column,True)
    dataframe.drop(df.index[index],inplace=True)

#uç değerleri baskılama
def cap_outlier(dataframe, column):
    low, up = outlier_threshold(dataframe, column)
    dataframe[column] = dataframe[column].clip(lower=low, upper=up)

def find_column_types(dataframe):
    categorical = [column for column in dataframe.columns if dataframe[column].dtypes == "O"]
    numerical_but_categorical = [column for column in dataframe.columns if dataframe[column].dtypes != "O" and dataframe[column].nunique() < 10]
    categorical_but_cardinality = [column for column in dataframe.columns if dataframe[column].dtypes == "O" and dataframe[column].nunique() > 20]

    categorical = categorical + numerical_but_categorical
    categorical = [column for column in categorical if column not in categorical_but_cardinality]

    numerical = [column for column in dataframe.columns if dataframe[column].dtypes != "O"]
    numerical = [column for column in numerical if column not in numerical_but_categorical]

    print(categorical_but_cardinality)
    print(categorical)
    print(numerical)

outlier_threshold(df, "Age")
outlier_index(df, "Age")
check_outlier(df,"Age")
remove_outlier(df,"Age")
cap_outlier(df,"Age")
find_column_types(df)