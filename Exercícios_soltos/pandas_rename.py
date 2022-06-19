import pandas as pd

def rename_columns(df, names):
    df_copy = df.copy()
    df_copy.columns = names
    return df_copy


df = pd.DataFrame(data=[[1,2,3], [4,5,6]], columns=list('123'))
names = ('A', 'B', 'C')

df_copy = df.copy()
df_copy.columns = names