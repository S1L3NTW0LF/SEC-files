import pandas as pd
import numpy as np
import json

with open('submissions/CIK0000001750.json') as datafile:
    data_sub = json.load(datafile)


df_submissions = pd.DataFrame(data_sub['filings']['recent'])

df_10K = df_submissions.loc[df_submissions['form'] == '10-K']

accn_list = df_10K['accessionNumber']
accn_list = accn_list.reset_index(drop=True)

tickers = data_sub['tickers']
