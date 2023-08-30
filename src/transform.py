# The python script that contains the definition that removes duplicates from data

def remove_duplicates(df):
    if df.duplicated().sum() > 0:
        print(f"number of duplicates = {df.duplicated().sum()}")
        df_cleaned = df.drop_duplicates(keep='first')
    else:
        df_cleaned = df
        print("no duplicates in dataframe")
    return df_cleaned