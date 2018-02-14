import sys
import pandas as pd
import numpy as np
import math as mt
import os

# Add some extra indentation on the conditional continuation line
def load_donations(path):
    '''
    The function load data from a path and return a predefine structure as a data frame.

    The scope of the function is to load data from a file and return only a workable structure for the project.

    Returned workable structure is defined as
    'CMTE_ID', 'NAME', 'ZIP_CODE', 'TRANSACTION_DT', 'TRANSACTION_AMT', 'OTHER_ID'

    :param path: Absolute path of the input file from data should be load.
    :return: Data frame object
    '''

    load_data = pd.read_csv(os.path.abspath(path), sep="|", header=None)
    load_data.columns = ['CMTE_ID', 'AMNDT_IND', 'RPT_TP', 'TRANSACTION_PGI', 'IMAGE_NUM',
                         'TRANSACTION_TP', 'ENTITY_TP', 'NAME', 'CITY', 'STATE','ZIP_CODE',
                         'EMPLOYER', 'OCCUPATION', 'TRANSACTION_DT', 'TRANSACTION_AMT',
                         'OTHER_ID', 'TRAN_ID', 'FILE_NUM', 'MEMO_CD', 'MEMO_TEXT' ,'SUB_ID'
                         ]
    pop_columns = ['AMNDT_IND', 'RPT_TP', 'TRANSACTION_PGI', 'IMAGE_NUM','TRANSACTION_TP',
                   'ENTITY_TP', 'CITY', 'STATE', 'EMPLOYER', 'OCCUPATION', 'TRAN_ID',
                   'FILE_NUM', 'MEMO_CD', 'MEMO_TEXT' ,'SUB_ID']
    for pop_column in pop_columns:
        load_data.pop(pop_column)
    return load_data


def load_percentile_param(config_file_path):
    with open(os.path.abspath(config_file_path), 'r') as config_file:
        percentile_param = config_file.read().rstrip("\n")
    return percentile_param

def load_path_param():
    percentile_param = pd.Series({'1': '', '2': '', '3': ''})
    with open(os.path.abspath('./src/path_config'), 'r') as config_file:
        percentile_param = config_file.read().splitlines()
    return percentile_param


def eliminate_empty_records(self, column_name,is_empty, drop_column):
    '''
    The function select records from a data frame which are not empty for a column.

    Data Frame and columm name which want to be evaluate if its values is null as receive as parameter. The function
    return a data frame without the records that match the condition of null values.

    :param self:
    :param column_name:
    :return:
    '''

    if is_empty:
        clean_data = self[self[column_name].isnull()]
    else:
        clean_data = self[self[column_name].notnull()]
    if drop_column:
        clean_data.pop(column_name)
    return clean_data


def set_donor_index(self, key_left_part, key_right_part):
   '''
   This function create a new index for the data frame receive base on a combination of two columns.

   Key value is generated concatenating the data frame columns in this order:
   key = df.column [key_left_part] + df.column [key_right_part]

   :param self: data container
   :param key_left_part: first part of the combine key
   :param key_right_part: second part of the combine key
   :return: data container with new index
   '''

   _local_df = self
   _clean_key_left = _local_df[key_left_part].str.replace(' ', '').str.replace(',', '')
   _clean__key_right = _local_df[key_right_part].astype(str).str[0:5].replace(' ', '')
   _keys_ds = _clean_key_left + _clean__key_right
   _local_df['key'] = _keys_ds
   _local_df.pop('NAME')
   _local_df.set_index('key', inplace=True)
   return _local_df


def clean_record_data(self, column_name, orientation, length):
    if orientation == 'left':
        ds = self[column_name].astype(str).str[:length]
        self[column_name] = ds
    elif orientation == 'right':
        ds = self[column_name].astype(str).str[(-1*length):]
        self[column_name] = ds
    return self


def committees_donor_percentile(committees, donations, percentile):
    out_columns = ['CMTE_ID', 'ZIP_CODE', 'TRANSACTION_DT', 'PERCENTILE', 'TOTAL_AMT', 'TXN_CNT']
    donations.set_index(['CMTE_ID', 'ZIP_CODE', 'TRANSACTION_DT'], inplace=True)
    committee_keys = donations.index.unique().tolist()
    outArray = []
    for committee in committee_keys:
        total_donation = 0
        amt = 0
        cntr = 0
        comt_zip_year = donations.loc[committee]
        N = len(donations.loc[committee])
        rank = nearest_percentile(comt_zip_year['TRANSACTION_AMT'], percentile, N)
        print(rank)
        for index, donation in comt_zip_year.iterrows():
            myData=[]
            cntr += 1
            amt = donation['TRANSACTION_AMT']
            total_donation = total_donation + amt
            myData = [index[0], index[1], index[2], rank, total_donation, cntr]
            outArray.append(myData)
        output_df = pd.DataFrame(outArray, columns=out_columns)
    return output_df


def nearest_percentile(self, P, N):

    rank = (P/100) * N
    rank = mt.ceil(rank)
    print(rank)
    sorted_ = self.sort_values()
    print(sorted_)
    nearest_rank = sorted_.iloc[rank-1]
    return nearest_rank
