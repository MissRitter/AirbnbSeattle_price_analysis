
import pandas as pd

from ExploreData import value_counter, index_by_key


def feature_encoding(df):
    '''
    Encodes remaining categorical columns for modeling
    or drops them in case they have too many unique values.
    
    This function assumes a previous dealing with categorical columns from
    'CategoricalPrep.transform_columns(df)' and
    'CategoricalPrep.drop_columns_analyze(df)'
    '''

    df = df
    # Fix one broken values up front:
    df.loc[df['zipcode']== '99\n98122', 'zipcode'] = '98122'

    df_categorical = df.select_dtypes(include=['object'])
    df_values = value_counter(df_categorical)

    few_values = df_values[df_values['val_count']<=100].index
    # Create dummy columns with 0 or 1 values:
    df_dummies = pd.get_dummies(
        df[few_values], prefix_sep='_',
        drop_first=True, dummy_na=True
        )
    # Join new dummy columns to 'df' and drop the original ones
    df = df.join(df_dummies)
    df = df.drop(few_values, axis = 1)

    # Drop remaining columns with more than 100 unique values
    to_many_values = df_values[df_values['val_count']>100].index
    df = df.drop(to_many_values, axis=1)

    return df


def drop_columns_train(df):
    '''
    Drops entire columns to prepare for modeling. This step is also contained
    in function 'feature_encoding(df)'
    '''

    df = df
    df_categorical = df.select_dtypes(include=['object'])
    df_values = value_counter(df_categorical)
    to_many_values = df_values[df_values['val_count']>100].index
    df.drop(to_many_values, axis=1)

    return df



def imputation(df):
    ''' Deals with missing values in pd.DataFrame 'df'.
    
    OUTPUT (pd.DataFrame): Returns an updated 'df' without missing values.
    '''
    df_values = value_counter(df)
    # Store names fo columns with missing values in 'nans_attributes'
    df_nans = df_values[df_values['nan_pcnt'] > 0]
    nans_attributes = df_nans.index

    # Keep information about NaN values in separate columns for
    # 'review_scores' and 'security_deposit'
    col_names = index_by_key(df, ['review_scores', 'security'])

    if 'has_review_scores_rating' not in col_names: # Don't run it twice!
        for col in col_names:
            # Create new column with prefixed name
            new_name = 'has_' + col
            df[new_name] = df[col].notnull().astype('int')
    # Impute original columns with 0
    df[col_names] = df[col_names].fillna(0, axis=0)
    # Remove column names from 'nans_attributes'
    nans_attributes = nans_attributes.difference(col_names)
    
    # Host_response_rate: Fill nan values with mean
    df['host_response_rate'] = df['host_response_rate'].fillna(
        df['host_response_rate'].mean())
    # Remove the name from 'nans_attributes'
    nans_attributes = nans_attributes.difference(['host_response_rate'])

    # The remaining columns can be filled with the mode
    df_mode = df[nans_attributes]
    df_mode = df_mode.fillna(df_mode.mode().squeeze(), axis=0)
    df[nans_attributes] = df_mode

    return df




