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
# define global variable
###########################################
SVC_NAME = '새주소 5자리 우편번호 조회서비스'
SVC_FLAG = 'o'
SVC_ENDP = 'http://openapi.epost.go.kr:80/postal/retrieveNewAdressAreaCdService?_wadl&type=xml'
SVC_URL  = 'http://openapi.epost.go.kr:80/postal/retrieveNewAdressAreaCdService/retrieveNewAdressAreaCdService/getNewAddressListAreaCd'
# SVC_URL = 'http://---openapi.epost.go.kr:80/postal/retrieveNewAdressAreaCdService/retrieveNewAdressAreaCdService/getNewAddressListAreaCd'
# SVC_URL = 'http://openapi.epost.go.kr:80/postal/retrieveNewAdressAreaCdService/retrieveNewAdressAreaCdService/getNewAddressListAreaCd---'


###########################################
# define type
###########################################
class SearchSe(enum.Enum):
    DONG = 'dong'
    ROAD = 'road'
    POST = 'post'

###########################################
# define req
###########################################
REQ_SPECS = [
    reqspec.Spec('serviceKey', True),
    reqspec.Spec('searchSe', False, SearchSe.POST.value),
    reqspec.Spec('srchwrd', True),
    reqspec.Spec('countPerPage', False, 10),
    reqspec.Spec('currentPage', False, 1)
]

def req(**kwargs) -> requests.models.Response:
    # logging.info('1. %s', pprint.pformat(kwargs) )
    kwargs = reqspec.merge_and_verify(REQ_SPECS, **kwargs)
    # logging.info('2. %s', pprint.pformat(kwargs))
    return requests.get(SVC_URL, params=kwargs)

def get_df(**kwargs) -> pd.DataFrame:
    itemDictList = []
    currentPage = 1
    while (True):
        kwargs['countPerPage'] = 10
        kwargs['currentPage'] = currentPage
        rsp = req(**kwargs)

        rsp_dict = RspDict.fromRsp(rsp)

        total = rsp_dict.totalCount()
        chunk = rsp_dict.itemDictList()
        if len(chunk) <= 0:
            # logging.warning('unexpected: len(chunk)(%d) <=0', len(chunk))
            break

        itemDictList += chunk
        # logging.info('page:%d, total: %s/%s', currentPage, len(addressDictList), total)

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
    return rsp_dict.header(), df

###########################################
# define rsp
###########################################
class RspDict(OrderedDict):

    @staticmethod
    def fromRsp(rsp : requests.models.Response ) -> 'RspDict':
        # return RspDict( xmltodict.parse(rsp.content) )
        return RspDict( xmltodict.parse(rsp.content, force_list='newAddressListAreaCd') )

    def header(self) -> OrderedDict:
        return self['NewAddressListResponse']['cmmMsgHeader']

    def totalCount(self) -> int:
        try:
            return int(self['NewAddressListResponse']['cmmMsgHeader']['totalCount'])
        except Exception as e:
            # logging.exception(e)
            return 0

    def itemDictList(self) -> typing.List[OrderedDict]:
        # normalize
        try:
            lst = self['NewAddressListResponse']['newAddressListAreaCd']
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
