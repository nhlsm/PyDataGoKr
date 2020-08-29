import xmltodict

from ..core.param import *
from ..core.reply import *
from ..core.rspcontentbase import *

###########################################
# define global
###########################################
SVC_DESC = '보건복지부_코로나19연령별,성별감염_현황 조회 서비스'
SVC_FLAG = 'o'
SVC_ENDP = 'http://openapi.data.go.kr/openapi/service/rest/Covid19'
SVC_URL  = 'http://openapi.data.go.kr/openapi/service/rest/Covid19/getCovid19GenAgeCaseInfJson'

###########################################
# define type
###########################################

###########################################
# define req
###########################################
SVC_PARAMS = [
    Param('serviceKey',   True),
    Param('startCreateDt',True),
    Param('endCreateDt',  True),
    Param('numOfRows',    False, 10),
    Param('pageNo',       False, 1),
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
