import logging
import sys
import pprint
import enum
import typing
import json
from collections import OrderedDict

import requests
import xmltodict
import pandas as pd

from . import args
from . import errors
# getRTMSDataSvcAptTrade
'''
                                          
'''
###########################################
# define global variable
###########################################
SVC_ENDP = None
SVC_URL = 'https://www.dhlottery.co.kr/store.do'

###########################################
# define type
###########################################


###########################################
# define argspec / req
###########################################
REQ_SPECS = [
    args.ArgSpec('method',    False, 'topStore'),
    args.ArgSpec('pageGubun', False, 'L645'),
]

def req(**kwargs) -> requests.models.Response:
    # logging.info('1. %s', pprint.pformat(kwargs) )
    kwargs = args.merge_and_verify(REQ_SPECS, **kwargs)
    # logging.info('2. %s', pprint.pformat(kwargs))
    return requests.get(SVC_URL, params=kwargs)

def test_0():
    rsp = req(drwNo = 903)
    logging.info('code: %s', rsp.status_code)
    logging.info('hdr : %s', rsp.headers)
    logging.info('cont: %s', rsp.content)
    # jsond = json.loads(rsp.content)
    # logging.info('\n%s', pprint.pformat(jsond) )

def get_df(**kwargs) -> pd.DataFrame:
    itemDictList = []
    currentPage = 1
    while (True):
        try:
            kwargs['countPerPage'] = 10
            kwargs['currentPage'] = currentPage
            rsp = req(**kwargs)

            rsp_dict = RspDict(xmltodict.parse(rsp.content))

            total = rsp_dict.totalCount()
            chunk = rsp_dict.itemDictList()
            itemDictList += chunk
            # logging.info('page:%d, total: %s/%s', currentPage, len(addressDictList), total)
            # https: // www.dhlottery.co.kr / common.do?method = getLottoNumber & drwNo = 903
            if len(chunk) <= 0:
                logging.warning('unexpected: len(chunk)(%d) <=0', len(chunk))
                break

            if len(itemDictList) == total:
                break
            elif len(itemDictList) > total:
                logging.warning('unexpected: len(itemDictList)(%d) > total', len(itemDictList) )
                break
            currentPage += 1
        except Exception as e:
            logging.exception(e)
            raise e

    # logging.info('list\n%s', pprint.pformat(addressList) )
    df = pd.DataFrame(itemDictList)
    # logging.info('%s, %s', len(itemDictList), len(df))
    # logging.info('\n%s', df )
    return df

class RspDict(OrderedDict):
    def totalCount(self) -> int:
        try:
            return int(self['NewAddressListResponse']['cmmMsgHeader']['totalCount'])
        except Exception:
            return 0

    def itemDictList(self) -> typing.List[OrderedDict]:
        try:
            lst = self['NewAddressListResponse']['newAddressListAreaCd']
            # normalize
            if isinstance(lst, list):
                return lst
            else:
                return [lst]
        except Exception:
            return []

    def itemDataFrame(self) -> pd.DataFrame:
        return pd.DataFrame(self.itemDictList())


def test_2():
    try:
        # rsp = get_rsp(serviceKey=SVC_KEY, searchSe=SearchSe.ROAD.value, srchwrd='세종로 17')
        # rsp = get_rsp(serviceKey=SVC_KEY, searchSe=SearchSe.ROAD.value, srchwrd='세종로 17', requestMsgId='1')
        # rsp = get_rsp(serviceKey=SVC_KEY, searchSe=SearchSe.ROAD.value, srchwrd='세종로')
        # rsp = get_rsp(serviceKey=SVC_KEY + '1', searchSe=SearchSe.ROAD.value, srchwrd='세종로 17')
        rsp = req(serviceKey=SVC_KEY, searchSe=SearchSe.POST.value, srchwrd='22170', countPerPage = 10, currentPage = 200)

        # logging.info('type(rsp): %s', type(rsp))
        logging.info('code: %s', rsp.status_code )
        logging.info('hdr : %s', pprint.pformat(rsp.headers) )
        logging.info('cont: %s', rsp.content)
        #
        # logging.info('POST: %s', SearchSe.POST )
        # logging.info('POST: %s', SearchSe.POST.value)

        rsp_dict = RspDict(xmltodict.parse(rsp.content))
        # logging.info('%s', type(rsp_dict))
        # logging.info('\n%s', pprint.pformat(rsp_dict) )
        lst = rsp_dict.itemDictList()
        logging.info('type: %s', type(lst) )
        # logging.info('\n%s', pprint.pformat(lst) )

        # df = rsp_dict.addressDataFrame()
        # logging.info('%s', list(df.columns) )
        # logging.info('df\n%s', df )
        # popo = NewAddressListResponse( xmltodict.parse(rsp.content) )
        # logging.info('%s', type(popo))
        # popo.dump()
        # # logging.info('\n%s', pprint.pformat(popo))
        # # logging.info('successYN: %s', popo.successYN())
        # # logging.info('totalCount: %s', popo.totalCount())
        # logging.info('hasResult:\n%s', popo.hasResult() )
        # logging.info('getList:\n%s', pprint.pformat(popo.getList()) )
    except Exception as e:
        logging.exception(e)
        raise e



if __name__ == '__main__':
    # debug
    LOG_FORMAT = '%(pathname)s:%(lineno)03d - %(message)s'
    # LOG_LEVEL = logging.DEBUG  # DEBUG(10), INFO(20), (0~50)
    LOG_LEVEL = logging.INFO  # DEBUG(10), INFO(20), (0~50)

    # release
    # LOG_FORMAT = '%(message)s'
    # LOG_LEVEL = logging.INFO  # DEBUG(10), INFO(20), (0~50)

    logging.basicConfig(format=LOG_FORMAT, level=LOG_LEVEL, stream=sys.stdout)
    # main( parse_arguments( sys.argv[1:]) )
    test_0()
    # test_2()
    # test_3()
