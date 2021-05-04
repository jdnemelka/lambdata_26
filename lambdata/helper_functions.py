import pandas as pd
import numpy as np
import re

def null_count(df):
    return df.isnull().sum()

def train_test_split(df):
        n_arrays = len(arrays)
    if n_arrays == 0:
        raise ValueError("At least one array required as input")

    arrays = indexable(*arrays)

    n_samples = _num_samples(arrays[0])
    n_train, n_test = _validate_shuffle_split(n_samples, test_size, train_size,
                                              default_test_size=0.25)

    if shuffle is False:
        if stratify is not None:
            raise ValueError(
                "Stratified train/test split is not implemented for "
                "shuffle=False")

        train = np.arange(n_train)
        test = np.arange(n_train, n_train + n_test)

    else:
        if stratify is not None:
            CVClass = StratifiedShuffleSplit
        else:
            CVClass = ShuffleSplit

        cv = CVClass(test_size=n_test,
                     train_size=n_train,
                     random_state=random_state)

        train, test = next(cv.split(X=arrays[0], y=stratify))

    return list(chain.from_iterable((_safe_indexing(a, train),
                                     _safe_indexing(a, test)) for a in arrays))

def addy_split(addy_series):
    #Create Dataframe
    df = pd.DataFrame()


    #Create City Column
    search = []
    for values in addy_series:
        search.append(re.match(r'[a-zA-Z]+[a-zA-Z],&')).group()

    df['city'] = search
    df['city'] = df['city'].str.replace(r',', '')

    #Create State Column
    search = []
    for values in addy_series:
        search.append(re.match(r'[A-Z]{2}')).group()

    df['State'] = search


    #Create Zip COde Column
    search = []
    for values in addy_series:
        search.append(re.match(r'[0-9]{5}')).group()

    df['Zip Code'] = search
    
    return df 
    

    