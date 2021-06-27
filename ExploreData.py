
#import numpy as np
import pandas as pd

def cols_nan_ratio(df, nan_ratio, bigger=True) :
    '''
    Returns 'df's column names for columns with a ratio of more than
    'nan_ratio' NaN values if 'bigger' = True, or if 'bigger' = False those
    with a ratio of exactly 'nan_ratio' NaN values.

    INPUT:
        df (pd.DataFrame)
        nan_ratio (float): 1 >= nan_ratios >= 0
        bigger (bool)

    OUTPUT (pd.Index)
    '''
    col_ratios = df.isnull().sum()/df.shape[0]
    if bigger:
        return df.columns[col_ratios > nan_ratio]
    else:
        return df.columns[col_ratios == nan_ratio]



def sort_mean(df, column_group, column, sort_index=False) :
    '''
    Selects two columns from 'df' 'column_group' and 'column' and groups by
    'column_group' turning it into the index. It returns a sorted pd.Series.
    If 'sort_index' is True it sorts the index otherwise the data ('column').

    INPUT:
        df (pd.DataFrame)
        columns_group (str)
        columns (str)
        sort_index (bool)

    OUTPUT (pd.Series)
    '''
    temp_df = df[[column_group, column]]
    if sort_index:
        return temp_df.groupby(
        temp_df[column_group] ).mean().sort_index()
    else:
        return temp_df.groupby(
            temp_df[column_group] ).mean().sort_values(column)



def value_counter(df):
    ''' Generates information about values in each column of 'df'

    INPUT (pd.DataFrame)

    OUTPUT (pd.DataFrame): Index are the column names of the input 'df'. Each
        row contains information about the column in the index.
        column 'val_count': The number of unique values
        column 'val_pcnt': Percentage of unique values
        column 'nan_count': The number of NaN
        column 'nan_pcnt': Percentage of NaN values 
        column 'col_dtype': The columns type
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
        df (pd.DataFrame): The df to search
        key_list (list): Strings to search for
        col_bool (bool): Flag determining wether to search column or index names

    OUTPUT (pd.Index): search results
    '''
    if col_bool == True:
        search_series = df.columns.to_series()
        bool_series = search_series.str.contains('|'.join(key_list),case=False)

        return df.columns[bool_series]

    else:
        search_series = df.index.to_series()
        bool_series = search_series.str.contains('|'.join(key_list),case=False)

        return df.index[bool_series]


