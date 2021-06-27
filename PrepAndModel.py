
import pandas as pd

#from sklearn.linear_model import LinearRegression
#from sklearn.tree import DecisionTreeRegressor
#from sklearn.model_selection import train_test_split, cross_val_score
#from sklearn.metrics import r2_score, mean_squared_error

from ExploreData import value_counter, index_by_key




def drop_columns_train(df):
    ''' Drops entire columns to prepare for modeling '''

    df = df
    df_categorical = df.select_dtypes(include=['object'])
    df_values = value_counter(df_categorical)
    to_many_values = df_values[df_values['val_count']>100].index
    df.drop(to_many_values, axis=1)

    return df



def feature_encoding(df):
    '''
    Encodes remaining categorical columns for modeling
    or drops them in case they have too many unique values
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



def imputation(df):
    ''' Deals with missing values in the data set '''

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



def imputation_old(df):
    '''
    Identifies columns with NaN
    imputes the mode for columns with 35 values or less
    imputes the mean for the rest
    '''

    df_values = value_counter(df)
    df_nans = df_values[df_values['nan_pcnt'] > 0]

    col_fill_mode = df_nans[df_nans['val_count']<=35].index
    col_fill_mean = df_nans[df_nans['val_count']>35].index

    df_mode = df[col_fill_mode]
    df_mode = df_mode.fillna(df_mode.mode().squeeze(), axis=0)

    df_mean = df[col_fill_mean]
    df_mean =df_mean.fillna(df_mean.mean(), axis=0)

    df = df.drop(df_nans.index, axis=1)
    df = df.join(df_mean).join(df_mode)
    return df


def drop_to_much_information(df):
    ''' Drops information not fitting the question
    '''
    return df


