
import pandas as pd
import numpy as np
import seaborn as sns


def load_and_process(csv_file_path):

    # Method Chain 1 (Load data and deal with missing data, drop unnecessary columns,and convert all strings to lowercase)

    df1 = (
          pd.read_csv(csv_file_path)
          .dropna(axis=1, how='all')                        #drops the neighbourhood column where all whole column is empty.
          .drop(['last_review','reviews_per_month'],axis=1)
          .applymap(lambda x:x.lower() if type(x) == str else x)
      )
    
    #Using boxplot and scatter plots, the outliers are determined.
    
    #sns.boxplot(x=df1['minimum_nights'])
    #sns.scatterplot(x='price',y='minimum_nights',data = df1)
    #sns.boxplot(x=df1['price'])
    
    df1.loc[df1['minimum_nights']>400, 'minimum_nights'] = df1['minimum_nights'].mean()
    df1.loc[df1['price']>150000,'price'] = df1['price'].mean()
    

    return df1


