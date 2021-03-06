import numpy as np
import pandas as pd
from ExploreData import sort_mean, value_counter, index_by_key
from TransformData import \
    price_transform, rate_transform, split_column_values, date_transform


def drop_columns_analyze(df):
    '''
    Drops entire columns of no interest from the data-set, to
    make analysis easier. Returns the reduced pd.DataFrame.
    '''

    list_column_values = value_counter(df)

    # Columns with constant values
    list_const_drop = list_column_values.loc[
        list_column_values['val_count']==1].index
    # Columns with no values
    list_nan_drop = list_column_values.loc[
        list_column_values['nan_pcnt']>=90].index
    # These column cary multiple values but mean the same (mainly typos)
    list_location_drop = df[['city', 'state', 'smart_location']].columns
    # Url columns carry no accessible information
    list_url_drop= df.columns[
        df.columns.to_series().str.contains('url',case=False)]
    # Drop for other reasons:
    list_else_drop= df[[
        'host_name', 'host_location',
        'neighbourhood', 'neighbourhood_cleansed'
        ]].columns
    # Combine all lists
    drop_columns_list = list_const_drop.append(
                        list_nan_drop).append(
                        list_location_drop).append(
                        list_url_drop).append(
                        list_else_drop)

    return df.drop(columns=drop_columns_list)


def transform_columns(df):
    '''
    Transforms columns from categorical to numeric type:
    currency, rate, date, binary string-values, ordinal values
    and special treatmend for some string value columns.

    This function deals only with the part of the categorical columns which
    is of interest for the following analysis.
    There will be categorical columns left in the data-set!

    OUTPUT (pd.DataFrame): The transformed input pd.DataFrame 'df'
    '''
    df = df
    list_column_values = value_counter(df)


    # Currency:
    # Select columns wit currency
    search_values = ['price', 'fee', 'deposit', 'extra']
    price_column_names  = index_by_key(df, search_values)
    # Transform values to float
    for col in price_column_names :
        df[col] = price_transform(df[col])

    # Rate:
    # Select columns with rate
    search_values_rate = ['rate']
    rate_column_names  = index_by_key(df, search_values_rate)
    # Transform values to float
    for col in rate_column_names :
        df[col] = rate_transform(df[col])

    # Date:
    # Transform host_since to date-type and split into year, day, month
    date_transform(df, 'host_since', 'host_since_')
    date_transform(df, 'first_review', 'first_review_')
    date_transform(df, 'last_review', 'last_review_')
    df = df.drop(columns=['host_since','first_review','last_review'])

    # Binary Strings:
    binary_map = {'t': 1, 'f': 0}
    # Identify columns with two values
    binary_cols = list_column_values.loc[
        list_column_values['val_count']==2 ].index
    for col in binary_cols:
        if df[col].dtype == 'object':  # Map only object columns
            df[col] = df[col].map(binary_map)

    # Ordinal:
    policy_map = {'strict':2, 'moderate':1, 'flexible':0}
    response_map = {'a few days or more':3, 'within a day':2,
    'within a few hours':1, 'within an hour':0}
    df['cancellation_policy'] = df['cancellation_policy'].map(policy_map)
    df['host_response_time'] = df['host_response_time'].map(response_map)

    # Other:

    # amenities : Split colum into one column per value
    # Identify all possible values:
    all_splitted_entrys = []
    for i in df.index:
        entry_split = df['amenities'].loc[i].replace(
            '{', '').replace('}', '').replace('"', '').split(sep=",")
        all_splitted_entrys = all_splitted_entrys+entry_split
    all_values = list(set(all_splitted_entrys))  # Removes duplicates
    all_values.remove('')

    # Create a new column for every value:
    split_column_values(df, 'amenities', all_values, 'amenities_')
    df.drop(columns=['amenities'], inplace=True)

    # host_verifications : Split column into column per value
    # Identify all possible values:
    all_splitted_entrys = []
    for i in df.index:
            entry_split = df['host_verifications'].loc[i].replace(
                '[', '').replace(']', '').replace("'", "").split(sep=", ")
            all_splitted_entrys = all_splitted_entrys+entry_split
    all_values = list(set(all_splitted_entrys))  # Removes duplicates
    all_values.remove('')
    all_values.remove('None')

    # Create a new column for every value:
    split_column_values(
        df,
        'host_verifications',
        all_values,
        'host_verifications_'
        )
    df.drop(columns='host_verifications', axis=1, inplace=True)

    return df

