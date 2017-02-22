import pandas as pd
import numpy as np

PATH = 'forestfires.csv'

# can use this dictionary to map a Series of the abbreviations to integers
LCASE_DAY_ABRV_DICT = {'sun':1,'mon':2,'tue':3,'wed':4,'thu':5,'fri':6,'sat':7}

def short_lcase_month_to_int(series):
    """
    convert Series of lower case short abbreviations of month
    names to Series of corresponding integers.
    """
    int_series = series.map(lambda x: x.title())
    int_series = pd.to_datetime(int_series, format='%b')
    int_series = int_series.map(lambda x: x.month)
    return int_series

def wrangle():
	"""
	reads csv from dataframe, converts month and day short abbreviations
	to integers, creates 'log(area)' column and 'small' boolean column	
	"""
	
	df = pd.read_csv(PATH, sep=',', header=0)
	df['month'] = short_lcase_month_to_int(df['month'])
	df['day'] = df['day'].map(lambda x:LCASE_DAY_ABRV_DICT[x])
	df['log'] = np.log(df['area']+1)
	df['small'] = df['area']==0
	return df
