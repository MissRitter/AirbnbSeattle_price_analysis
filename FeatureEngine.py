
import numpy as np
import pandas as pd


# New price features
def new_features(df):
    '''
    Adds new features to the data set:
    bedroom_price
    head_price
    has_weekly_price
    has_monthly_price

    Drops:
    monthly_price
    weekly_price
    '''

    df=df
    df['bedroom_price'] = df['price']/df['bedrooms'].apply(
        lambda x: 1 if x==0 else x)
    df['head_price'] = df['price']/df['accommodates']
    df['has_weekly_price'] = df['weekly_price'].notnull().astype('int')
    df['has_monthly_price'] = df['monthly_price'].notnull().astype('int')

    df = df.drop(columns=['monthly_price','weekly_price'], axis=1)

    # New features form calendar price_[month]

    return df
