import pandas as pd
import sqlite3 as sq
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import warnings, re
import nltk
from IPython.display import Image
import datetime
from collections import Counter
from sklearn.decomposition import NMF
from sklearn.metrics import explained_variance_score
from pylab import rcParams
from pyemd import emd
from collections import Counter
import scipy as sp
from mlxtend.preprocessing import TransactionEncoder
from mlxtend.frequent_patterns import apriori
from mlxtend.frequent_patterns import association_rules


df_transactions = pd.read_csv('transactions.csv')

list_consecutive = []

name_prev = 'x'
for name,group in df_transactions.groupby(['SHOP','u_day','CONFIGURATIONID']):
    if name[0]!=name_prev:
        print(name[0])
        name_prev = name[0]

    #same shop,same line,same day
    i = 0
    
    for n,transaction in group.groupby('TRANSACTIONID'):
        if i == 0:
            i +=1
            transaction_prev = transaction
            continue
        #no cash transaction
        
        if transaction_prev['PERSONID'].unique()[0]!=0 and transaction['PERSONID'].unique()[0]!=0:
            
            time_first = transaction_prev[['year', 'month', 'day', 'hour','minute','second']].apply(lambda s : datetime.datetime(*s),axis = 1).iloc[0]
            time_second = transaction[['year', 'month', 'day', 'hour','minute','second']].apply(lambda s : datetime.datetime(*s),axis = 1).iloc[0]
            
            #two persons behind each other in the queue within a minute
            if (time_second-time_first).seconds < 60:
                list_consecutive.append([transaction_prev['PERSONID'].unique()[0],transaction['PERSONID'].unique()[0]])

        transaction_prev = transaction
        
list_consecutive_sorted = []

for item in list_consecutive:
    if item[0] != item[1]:
        list_consecutive_sorted.append(sorted(item))
        
df_pairs = pd.DataFrame(list_consecutive_sorted)
df_pairs['item'] = df_pairs[0].apply(str) + " "+ df_pairs[1].apply(str)
pairs = df_pairs['item'].value_counts()
df_pairs_frequencies = pd.DataFrame(pd.Series(pairs.index).apply(lambda x: x.split(' ')))
df_pairs_frequencies['frequency'] = pairs.values
df_pairs_frequencies.columns = ['pair','support']
df_pairs_frequencies['support'] = df_pairs_frequencies['support']/df_pairs_frequencies['support'].sum()

df_pairs_frequencies.to_pickle('new_pairs_all_rests')
