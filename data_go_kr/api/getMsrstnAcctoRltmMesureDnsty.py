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
from ..core.rspcontentbase import *

###########################################
# define global
###########################################
SVC_DESC = '측정소별 실시간 측정정보 조회'
SVC_FLAG = 'o'
SVC_ENDP = 'http://openapi.airkorea.or.kr/openapi/services/rest/ArpltnInforInqireSvc'
SVC_URL  = 'http://openapi.airkorea.or.kr/openapi/services/rest/ArpltnInforInqireSvc/getMsrstnAcctoRltmMesureDnsty'

###########################################
# define type
###########################################
DT_DAILY  = 'DAILY'
DT_MONTH  = 'MONTH'
DT_3MONTH = '3MONTH'

###########################################
# define req
###########################################
SVC_PARAMS = [
    Param('serviceKey', True),
    Param('stationName',True),
    Param('dataTerm',   True, DT_DAILY),
    Param('ver',        True, '1.0'),
    Param('numOfRows',  False, 3000),  # max 3 month: 3*30*24 = 2160
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
class RspContent(RspContentBase):
    @staticmethod
    def fromRsp(rsp : requests.models.Response ) -> 'RspContent':
        return RspContent( xmltodict.parse(rsp.content, force_list='item') )






