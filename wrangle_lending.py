import pandas as pd
import numpy as np
import seaborn as sns
from scipy import stats 
import matplotlib.pyplot as plt
import hvplot.pandas

from sklearn.model_selection import train_test_split, RandomizedSearchCV
from sklearn.preprocessing import MinMaxScaler
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LogisticRegression

from sklearn.metrics import (
    accuracy_score, confusion_matrix, classification_report, 
    roc_auc_score, roc_curve, auc,
    plot_confusion_matrix, plot_roc_curve
)

from sklearn.ensemble import RandomForestClassifier




def clean_lending(df):
    #drop unneeded columns
    df = df.drop(['emp_title'], axis=1)
    df = df.drop(['emp_length'], axis=1)
    df = df.drop(['title'], axis=1)
    
    #impute
    df['mort_acc'].fillna(2.0, inplace = True)
    
    #drop small amount of nulls
    df = df.dropna()
    
    return df    

def remove_outliers(df):
    
    """Manually handle outliers according to eda"""
    df = df[df.dti <= 40]
    
    df = df[df.total_acc <= 115]

    df = df[df.annual_inc <= 250_000]
    
    df = df[df.revol_util <= 200]
    
    df = df[df.pub_rec <= 25]

    df = df[df.open_acc <= 60]
    
    df = df[df.home_ownership != 'ANY']
    df = df[df.home_ownership != 'NONE']
    df = df[df.home_ownership != 'OTHER']

    return df

def split_data(df):
    '''
    Takes in the original cleaned, prepped df and returns train, validate, and test dfs.
    '''
    train_validate, test = train_test_split(df, test_size=.2, 
                                        random_state=123, 
                                        stratify=df.loan_status)

    train, validate = train_test_split(train_validate, test_size=.3, 
                                   random_state=123, 
                                   stratify=train_validate.loan_status)
    return train, validate, test


def encode_features(train, validate, test):
    #encode categoricals
    train['home_ownership_encoded'] = train.home_ownership.map({'MORTGAGE': 0, 'RENT': 1,'OWN': 2})
    validate['home_ownership_encoded'] = validate.home_ownership.map({'MORTGAGE': 0, 'RENT': 1,'OWN': 2})
    test['home_ownership_encoded'] = test.home_ownership.map({'MORTGAGE': 0, 'RENT': 1,'OWN': 2})
    
    # Encode by creating dummy vars and concat with original df
    encoded_initial_list_status = pd.get_dummies(train.initial_list_status, drop_first=True)
    train = pd.concat([train, encoded_initial_list_status], axis=1)
    encoded_initial_list_status = pd.get_dummies(validate.initial_list_status, drop_first=True)
    validate = pd.concat([validate, encoded_initial_list_status], axis=1)
    encoded_initial_list_status = pd.get_dummies(test.initial_list_status, drop_first=True)
    test = pd.concat([test, encoded_initial_list_status], axis=1)
    
    encoded_verification_status = pd.get_dummies(train.verification_status, drop_first=True)
    train = pd.concat([train, encoded_verification_status], axis=1)
    encoded_verification_status = pd.get_dummies(validate.verification_status, drop_first=True)
    validate = pd.concat([validate, encoded_verification_status], axis=1)
    encoded_verification_status = pd.get_dummies(test.verification_status, drop_first=True)
    test = pd.concat([test, encoded_verification_status], axis=1)
    
    return train, validate, test

def drop_columns(train, validate, test):
    train = train.drop(columns=['term', 'grade', 'sub_grade','home_ownership', 'issue_d','purpose', 'verification_status','earliest_cr_line', 'initial_list_status','open_acc', 'pub_rec', 'total_acc', 
                                'application_type', 'pub_rec_bankruptcies', 'address'])
    validate = validate.drop(columns = ['term', 'grade', 'sub_grade','home_ownership', 'issue_d','purpose', 'verification_status','earliest_cr_line', 'initial_list_status','open_acc', 'pub_rec', 'total_acc', 
                                'application_type', 'pub_rec_bankruptcies', 'address'])
    test = test.drop(columns = ['term', 'grade', 'sub_grade','home_ownership', 'issue_d','purpose', 'verification_status','earliest_cr_line', 'initial_list_status','open_acc', 'pub_rec', 'total_acc', 
                                'application_type', 'pub_rec_bankruptcies', 'address'])
    return train, validate, test    