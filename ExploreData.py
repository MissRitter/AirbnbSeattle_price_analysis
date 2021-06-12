
import numpy as np
import pandas as pd

def cols_nan_ratio(df1, nan_ratio, bigger=True) :
    '''
    INPUT - 
    OUTPUT - 
    '''
    col_ratios = df1.isnull().sum()/df1.shape[0]
    if bigger:
        return df1.columns[col_ratios > nan_ratio]
    else:
        return df1.columns[col_ratios == nan_ratio]



def sort_mean(df, column_group, column_interst, sort_index=False) :
    '''
    INPUT - 
    OUTPUT - 
    '''
    temp_df = df[[column_group, column_interst]]
    if sort_index:
        return temp_df.groupby(
        temp_df[column_group] ).mean().sort_index()
    else:
        return temp_df.groupby(
            temp_df[column_group] ).mean().sort_values(column_interst)



def value_counter(df):
    '''
    INPUT - 
    OUTPUT - 
    '''
    v_count = []
    v_pcnt = []
    na_count = []
    na_pcnt = []
    col_type = []
    
    cols = df.columns
    length = df.shape[0]
    for i in cols:
        v_count.append(df[i].value_counts().size)
        v_pcnt.append(df[i].value_counts().size/length*100)
        na_count.append(df[i].isnull().sum())
        na_pcnt.append(df[i].isnull().sum()/length*100)
        col_type.append(df[i].dtype)
    all_together = {
        'val_count': v_count,
        'nan_count': na_count,
        'val_pcnt': v_pcnt,
        'nan_pcnt': na_pcnt,
        'col_dtype': col_type
        }
    return pd.DataFrame(data=all_together, index=cols)


def index_by_key(df, key_list, col_bool=True):
    '''
    Returns a pandas.Index object
    with entries according to patterns in key_list and appearance in df.

    INPUT:
    df - the pandas DataFrame to search
    key_list - a list of strings to search for
    col_bool - a boolean flag determining wether to
        search column or index names

    OUTPUT:
    A pandas.Index object with the search result
    '''
    if col_bool == True:
        search_series = df.columns.to_series()
        bool_series = search_series.str.contains('|'.join(key_list),case=False)
        return df.columns[bool_series]
    else:
        search_series = df.index.to_series()
        bool_series = search_series.str.contains('|'.join(key_list),case=False)
        return df.index[bool_series]


