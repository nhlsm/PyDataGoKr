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
SVC_DESC = '측정소 목록 조회'
SVC_FLAG = 'TODO'
SVC_ENDP = 'http://openapi.airkorea.or.kr/openapi/services/rest/MsrstnInfoInqireSvc'
SVC_URL  = 'http://openapi.airkorea.or.kr/openapi/services/rest/MsrstnInfoInqireSvc/getMsrstnList'

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
    Param('numOfRows', False, 10),
    Param('pageNo', False, 1),
]

def get_rsp(**kwargs) -> requests.models.Response:
    kwargs = Param.merge_args(SVC_PARAMS, **kwargs)
    return requests.get(SVC_URL, params=kwargs)

def get_reply(**kwargs) -> Reply:
    itemDictList = []
    currentPage = 1
    while (True):
        kwargs['numOfRows'] = 10
        kwargs['pageNo'] = currentPage
        rsp = get_rsp(**kwargs)

        rsp_content = RspContent.fromRsp(rsp)

        total = rsp_content.totalCount()
        chunk = rsp_content.itemDictList()
        if len(chunk) <= 0:
            # logging.warning('unexpected: len(chunk)(%d) <=0', len(chunk))
            break

        itemDictList += chunk
        logging.info('page:%d, total: %s/%s', currentPage, len(itemDictList), total)

        if len(itemDictList) == total:
            break
        elif len(itemDictList) > total:
            logging.warning('unexpected: len(itemDictList)(%d) > total', len(itemDictList) )
            break
        currentPage += 1

    # logging.info('list\n%s', pprint.pformat(addressList) )
    df = pd.DataFrame(itemDictList)
    # logging.info('%s, %s', len(itemDictList), len(df))
    # logging.info('\n%s', df )
    return Reply(rsp, rsp_content, df)



###########################################
# define rsp content
###########################################
class RspContent(RspContentBase):
    @staticmethod
    def fromRsp(rsp : requests.models.Response ) -> 'RspContent':
        return RspContent( xmltodict.parse(rsp.content, force_list='item') )






