import pandas as pd
import numpy as np

PATH = 'forestfires.csv'
LCASE_DAY_ABRV_DICT = {'sun':1,'mon':2,'tue':3,'wed':4,'thu':5,'fri':6,'sat':7}

def short_lcase_month_to_int(series):
    series = series.map(lambda x: x.title())
    series = pd.to_datetime(series, format='%b')
    series = series.map(lambda x: x.month)

def wrangle():
    #read csv to DataFrame
    df = pd.read_csv(PATH, sep=',', header=0)
    #Convert month abbreviations to integers
    short_lcase_month_to_int(df['month'])
    #Convert day abbreviations to integers
    df['day'] = df['day'].map(lambda x:LCASE_DAY_ABRV_DICT[x])
    #Create new ln of area column
    df['log(area)'] = np.log(df['area']+1)
    return df
