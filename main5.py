import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from sklearn.impute import KNNImputer

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
pd.set_option('display.float_format', lambda x: '%.3f' % x)
pd.set_option('display.width', 500)

df = pd.read_csv("datasets/titanic.csv")
df.head()

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

#çözüm 1: eksik verileri silmek:

new_df = df.dropna()

#çözüm 2: eksik verileri başka değerlerle doldurmak

mean = df["Age"].mean
new_df = df
new_df["Age"] = df["Age"].fillna(mean)

median = df["Age"].median
new_df = df
new_df["Age"] = df["Age"].fillna(median)

new_df = df
new_df["Age"] = df["Age"].fillna(18)

new_df = df
new_df["Embarked"] = df["Embarked"].fillna("missing")

#çözüm 3: eksik verileri tahmini değerlerle doldurmak

def find_column_types(dataframe):
    categorical = [column for column in dataframe.columns if dataframe[column].dtypes == "O"]
    numerical_but_categorical = [column for column in dataframe.columns if dataframe[column].dtypes != "O" and dataframe[column].nunique() < 10]
    categorical_but_cardinality = [column for column in dataframe.columns if dataframe[column].dtypes == "O" and dataframe[column].nunique() > 20]

    categorical = categorical + numerical_but_categorical
    categorical = [column for column in categorical if column not in categorical_but_cardinality]

    numerical = [column for column in dataframe.columns if dataframe[column].dtypes != "O"]
    numerical = [column for column in numerical if column not in numerical_but_categorical]

    # print(categorical_but_cardinality)
    # print(categorical)
    # print(numerical)

    return categorical, numerical

categorical_columns,numerical_columns = find_column_types(df)

print(categorical_columns)
print(numerical_columns)

dff = pd.get_dummies(df[categorical_columns+numerical_columns], drop_first=True)
dff = dff.astype(int)
dff.head()

scaler = MinMaxScaler()
dff = pd.DataFrame(scaler.fit_transform(dff),columns=dff.columns)

imputer = KNNImputer(n_neighbors=5)
dff = pd.DataFrame(imputer.fit_transform(dff),columns=dff.columns)