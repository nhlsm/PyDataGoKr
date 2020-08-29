import logging

import xmltodict

from ..core.param import *
from ..core.reply import *
from ..core.rspcontentbase import *

###########################################
# define global variable
###########################################
SVC_DESC = '새주소 5자리 우편번호 조회서비스'
SVC_FLAG = 'o'
SVC_ENDP = 'http://openapi.epost.go.kr:80/postal/retrieveNewAdressAreaCdService?_wadl&type=xml'
SVC_URL  = 'http://openapi.epost.go.kr:80/postal/retrieveNewAdressAreaCdService/retrieveNewAdressAreaCdService/getNewAddressListAreaCd'
# SVC_URL = 'http://---openapi.epost.go.kr:80/postal/retrieveNewAdressAreaCdService/retrieveNewAdressAreaCdService/getNewAddressListAreaCd'
# SVC_URL = 'http://openapi.epost.go.kr:80/postal/retrieveNewAdressAreaCdService/retrieveNewAdressAreaCdService/getNewAddressListAreaCd---'

###########################################
# define type
###########################################
SE_DONG = 'dong'
SE_ROAD = 'road'
SE_POST = 'post'

###########################################
# define req
###########################################
SVC_PARAMS = [
    Param('serviceKey', True),
    Param('searchSe', False, SE_POST),
    Param('srchwrd', True),
    Param('countPerPage', False, 10),
    Param('currentPage', False, 1)
]

def get_rsp(**kwargs) -> requests.models.Response:
    kwargs = Param.merge_args(SVC_PARAMS, **kwargs)
    return requests.get(SVC_URL, params=kwargs)

def get_reply(**kwargs) -> Reply:
    itemDictList = []
    currentPage = 1
    while (True):
        kwargs['countPerPage'] = 10
        kwargs['currentPage'] = currentPage
        rsp = get_rsp(**kwargs)

        rsp_content = RspContent.fromRsp(rsp)

        total = rsp_content.totalCount()
        chunk = rsp_content.itemDictList()
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
    return Reply(rsp, rsp_content, df)


###########################################
# define rsp content
###########################################
class RspContent(RspContentBase):
    @staticmethod
    def fromRsp(rsp : requests.models.Response ) -> 'RspContent':
        return RspContent( xmltodict.parse(rsp.content, force_list='newAddressListAreaCd') )

    # def resultCode(self) -> int:
    #     try:
    #         return int(self['response']['header']['resultCode'])
    #     except Exception as e:
    #         return -1
    #
    # def resultMsg(self) -> str:
    #     try:
    #         return self['response']['header']['resultMsg']
    #     except Exception as e:
    #         return '__UNKNOWN'
    #
    # def numOfRows(self) -> int:
    #     try:
    #         return int(self['response']['body']['numOfRows'])
    #     except Exception as e:
    #         return -1
    #
    # def pageNo(self) -> int:
    #     try:
    #         return int(self['response']['body']['pageNo'])
    #     except Exception as e:
    #         return -1

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

