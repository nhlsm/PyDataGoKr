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
SVC_DESC = 'KOSIS 통계목록 서비스'
SVC_FLAG = 'TODO'
SVC_ENDP = 'http://kosis.kr/openapi/Data/statisticsList.do'
SVC_URL  = 'http://kosis.kr/openapi/Data/statisticsList.do'

###########################################
# define type
###########################################

###########################################
# define req
###########################################
SVC_PARAMS = [
    Param('method',       False, 'getList'),
    Param('serviceKey',   True),
    Param('vwCd',         True, 'MT_ZTITLE'),
    Param('parentListId', True, 'A'),
    Param('format',       True, 'json'),
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

    def numOfRows(self) -> int:
        try:
            return int(self['response']['body']['numOfRows'])
        except Exception as e:
            return -1

    def pageNo(self) -> int:
        try:
            return int(self['response']['body']['pageNo'])
        except Exception as e:
            return -1

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






