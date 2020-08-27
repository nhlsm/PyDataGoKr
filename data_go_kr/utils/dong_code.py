'''
dong code
    law dong

동 코드
    법정동
    행정동

법정동 코드 (10자리) : 법적주소
시도(2)+시군구(3)+읍면동(3)+리(2)

ex) 2817710100	인천광역시 미추홀구 숭의동

28 + 177 + 101 + 00

'''

import logging
import sys
import pprint
import enum
import typing
from collections import OrderedDict
from io import StringIO

import pandas as pd

def _init():
    print('_init()')

    # return pd.read_csv('../docs/법정동코드 전체자료.csv', dtype= {'법정동코드':'str'} )
    # with open('../docs/법정동코드 전체자료.txt', 'r') as f:
    #     text = f.read()
    #     # print(text)
    #     df = pd.read_csv(StringIO(text), sep='\t', dtype= {'법정동코드':'str'} )
    #     # print(df)
    #     # logging.info('key: %s', df )
    #     return df
    with open('../docs/법정동코드 전체자료.txt', 'r') as f:
        text = f.read()
        # print(text)
        return pd.read_csv(StringIO(text), sep='\t', dtype= {'법정동코드':'str'} )

LAWD_CODE : pd.DataFrame = _init()
'''
법정동코드, 법정동명, 폐지여부
1100000000, 서울특별시, 존재
1111000000, 서울특별시 종로구, 존재
1111010100, 서울특별시 종로구 청운동, 존재
1111010200, 서울특별시 종로구 신교동, 존재

make csv. ( euc_kr -> utf-8 ) 
https://rolandd.com/documentation/ro-csvi/save-a-csv-file-as-utf-8
'Edit filter settings'
'''

def lawd_01(exists = 'o') -> pd.DataFrame:
    query_str = ' 법정동코드.str.endswith("00000000") '
    if exists == 'o':
        query_str += ' and 폐지여부=="존재" '
    elif exists == 'x':
        query_str += ' and 폐지여부=="폐지" '
    return LAWD_CODE.query( query_str )

def lawd_05(exists = 'o') -> pd.DataFrame:
    query_str = ' 법정동코드.str.endswith("00000") and 법정동코드.str.slice(2, 5) != "000" '
    if exists == 'o':
        query_str += ' and 폐지여부=="존재" '
    elif exists == 'x':
        query_str += ' and 폐지여부=="폐지" '
    return LAWD_CODE.query( query_str )
