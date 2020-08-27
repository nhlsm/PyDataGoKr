import logging
import sys
import pprint
import enum
import typing
from collections import OrderedDict

import requests
import xmltodict
import pandas as pd

from .utils import reqspec

###########################################
# define global
###########################################
SVC_NAME = '보건복지부_코로나19시,도발생_현황 조회 서비스'
SVC_FLAG = 'o'
SVC_ENDP = 'http://openapi.data.go.kr/openapi/service/rest/Covid19'
SVC_URL  = 'http://openapi.data.go.kr/openapi/service/rest/Covid19/getCovid19SidoInfStateJson'

###########################################
# define type
###########################################

###########################################
# define req
###########################################
REQ_SPECS = [
    reqspec.Spec('serviceKey', True),
    reqspec.Spec('numOfRows', False, 10),
    reqspec.Spec('pageNo', False, 1),
    reqspec.Spec('startCreateDt', True),
    reqspec.Spec('endCreateDt', True),
]

def req(**kwargs) -> requests.models.Response:
    # logging.info('1. %s', pprint.pformat(kwargs) )
    kwargs = reqspec.merge_and_verify(REQ_SPECS, **kwargs)
    # logging.info('2. %s', pprint.pformat(kwargs))
    return requests.get(SVC_URL, params=kwargs)

def get_df(**kwargs) -> pd.DataFrame:
    rsp = req(**kwargs)
    rsp_dict = RspDict(xmltodict.parse(rsp.content))
    return rsp_dict.itemDataFrame()

###########################################
# define rsp
###########################################
class RspDict(OrderedDict):

    @staticmethod
    def fromRsp(rsp : requests.models.Response ) -> 'RspDict':
        # return RspDict( xmltodict.parse(rsp.content) )
        return RspDict( xmltodict.parse(rsp.content, force_list='item') )

    def resultCode(self) -> int:
        try:
            return int(self['response']['header']['resultCode'])
        except Exception as e:
            return -1

    def resultMsg(self) -> str:
        try:
            return self['response']['header']['resultMsg']
        except Exception as e:
            return '__UNKNOWN'

    def result(self) -> (int,str):
        return (self.resultCode(), self.resultMsg())

    def totalCount(self) -> int:
        try:
            return int(self['response']['body']['totalCount'])
        except Exception as e:
            # logging.exception(e)
            return 0

    def itemDictList(self) -> typing.List[OrderedDict]:
        # normalize
        try:
            lst = self['response']['body']['items']['item']
            # logging.info('type(lst): %s', type(lst) )
            if lst is None:
                return []
            elif isinstance(lst, list):
                return lst
            else:
                return [lst]
        except Exception as e:
            # logging.exception(e)
            return []

    def itemDataFrame(self) -> pd.DataFrame:
        return pd.DataFrame(self.itemDictList())





