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
# define global variable
###########################################
SVC_DESC = '아파트매매 실거래자료'
SVC_FLAG = 'o'
SVC_ENDP = 'http://openapi.molit.go.kr:8081/OpenAPI_ToolInstallPackage/service/rest/RTMSOBJSvc/getRTMSDataSvcAptTrade?_wadl&type=xml'
SVC_URL  = 'http://openapi.molit.go.kr:8081/OpenAPI_ToolInstallPackage/service/rest/RTMSOBJSvc/getRTMSDataSvcAptTrade'

###########################################
# define type
###########################################

###########################################
# define req
###########################################
SVC_PARAMS = [
    Param('LAWD_CD', True),
    Param('DEAL_YMD', True),
    Param('serviceKey', True),
    # args.ArgSpec('numOfRows', False, 0),  test
]

def get_rsp(**kwargs) -> requests.models.Response:
    # logging.info('1. %s', pprint.pformat(kwargs) )
    kwargs = Param.merge_args(SVC_PARAMS, **kwargs)
    # logging.info('2. %s', pprint.pformat(kwargs))
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

