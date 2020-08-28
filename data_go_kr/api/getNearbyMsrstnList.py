import logging
import sys
import pprint
import enum
import typing
from collections import OrderedDict

import requests
import xmltodict
import pandas as pd

from ..core.param import *
from ..core.reply import *

###########################################
# define global
###########################################
SVC_DESC = '측정소정보 조회 서비스'
SVC_FLAG = 'o'
SVC_ENDP = 'http://openapi.airkorea.or.kr/openapi/services/rest/MsrstnInfoInqireSvc'
SVC_URL  = 'http://openapi.airkorea.or.kr/openapi/services/rest/MsrstnInfoInqireSvc/getNearbyMsrstnList'
'''
SC-OA-09-01 측정소정보 조회 서비스    MsrstnInfoInqireSvc
SC-OA-09-02 대기오염정보 조회 서비스   ArpltnInforInqireSvc
SC-OA-09-03 대기오염통계 서비스  ArpltnStatsSvc
SC-OA-09-04 오존황사 발생정보조회 서비스 OzYlwsndOccrrncInforInqireSvc
SC-OA-09-05 미세먼지 경보 정보 조회 서비스   UlfptcaAlarmInqireSvc
'''
###########################################
# define type
###########################################

###########################################
# define req
###########################################
SVC_PARAMS = [
    Param('serviceKey', True),
    Param('tmX', True, 10),
    Param('tmY', True, 1),
    Param('ver', True, '1.0'),
]

def get_rsp(**kwargs) -> requests.models.Response:
    kwargs = Param.merge_args(SVC_PARAMS, **kwargs)
    return requests.get(SVC_URL, params=kwargs)

def get_reply(**kwargs) -> Reply:
    rsp = get_rsp(**kwargs)
    rsp_content = RspContent.fromRsp(rsp)
    return Reply(rsp, rsp_content, rsp_content.itemDataFrame() )

###########################################
# define rsp content
###########################################
class RspContent(OrderedDict):

    @staticmethod
    def fromRsp(rsp : requests.models.Response ) -> 'RspContent':
        # return RspContent( xmltodict.parse(rsp.content) )
        return RspContent( xmltodict.parse(rsp.content, force_list='item') )

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






