
import pandas as pd

def date_transform(df, date_column, prefix=''):
    '''
    Transform an object-column with date information to datetime and creates
    additional separate columns for year, month and day

    INPUT:
        df (pd.DataFrame): Dataframe with a datetime-type column
        date_column (str): The datetime-type columns name

    OUTPUT (pd.DataFrame) Original dataframe df with three extra 
        columns 'year', 'month' and 'day' coresponding to the date_column
    '''
    df_trans = df
    # Transform the data columns in df_trans to date-type
    df_trans[date_column] = pd.to_datetime(df_trans[date_column])
    # Split the date information into three columns
    df_trans[prefix+"day"] = df_trans[date_column].map(lambda x: x.day)
    df_trans[prefix+"month"] = df_trans[date_column].map(lambda x: x.month)
    df_trans[prefix+"year"] = df_trans[date_column].map(lambda x: x.year)

    return df_trans


def price_transform(usd_col):
    ''' Returns the input column without $-sings and as float-type 
    
    INPUT (pd.Series)

    OUTPUT (pd.Series)
    '''

    col_return = usd_col
    col_return = col_return.replace(
        '[\$,]', '', regex=True).astype(float)
    return col_return


def rate_transform(percentage_col):
    ''' Returns the input column without %-sings and as float-type 
    
    INPUT (pd.Series)

    OUTPUT (pd.Series)'''

    col_return = percentage_col
    col_return = col_return.replace(
        '[\%,]', '', regex=True).astype(float)
    return col_return


def split_column_values(df, col_name, real_values, prefix=''):
    '''
    Returns the dataframe df with its original column col_name
    containing strings of listed values.
    In addition there will be new columns supplied by the
    column name list real_values.
    The new columns carry flags when the column name apears in the
    respective col_name entry.

    INPUT:
    df - the pandas dataframe with col_name as a column
    col_name (str)- the column name you want to look through
    real_values (list) - a list of strings you want to search for 
        in each row of df[col_name]
    prefix (str) - optional prefix for new column names

    OUTPUT:
    df (pd.DataFrame) - original df plus new columns with values {0,1}
    '''

    #loop through list of values
    for val in real_values:
        new_col_name = prefix+val
        df[new_col_name] = 0
        #loop through rows
        for idx in df.index:
            #if the pattern val is contained in this rows: set val to 1
            if val in df.loc[idx, col_name]:
                df.loc[idx, new_col_name] = 1
    return df


