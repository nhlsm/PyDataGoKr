import xmltodict

from ..core.param import *
from ..core.reply import *
from ..core.rspcontentbase import *

###########################################
# define global
###########################################
SVC_DESC = '미세먼지 경보 현황 정보를 조회하기 위한 서비스'
SVC_FLAG = 'o'
SVC_ENDP = 'http://openapi.airkorea.or.kr/openapi/services/rest/UlfptcaAlarmInqireSvc'
SVC_URL  = 'http://openapi.airkorea.or.kr/openapi/services/rest/UlfptcaAlarmInqireSvc/getUlfptcaAlarmInfo'

###########################################
# define type
###########################################
IC_PM10  = 'PM10'
IC_PM25  = 'PM25'
IC_ALL   = None

###########################################
# define req
###########################################
SVC_PARAMS = [
    Param('serviceKey', True),
    Param('year',       True),
    Param('itemCode',   False),    # IC_
    # Param('returnType', False),  # not work
    Param('numOfRows',  False, 3000),
    Param('pageNo',     False, 1),
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

