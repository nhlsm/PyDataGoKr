import pprint
import data_go_kr as dgk

SVC_KEY = dgk.test_svc_key()

rsp = dgk.getNewAddressListAreaCd.req(serviceKey=SVC_KEY, searchSe='road', srchwrd='세종로 17')

rsp_dict = dgk.getNewAddressListAreaCd.RspDict.fromRsp(rsp)

pprint.pprint( rsp_dict['NewAddressListResponse']['cmmMsgHeader'] )
'''
OrderedDict([('requestMsgId', None),
             ('responseMsgId', None),
             ('responseTime', '20200827:213700307'),
             ('successYN', 'Y'),
             ('returnCode', '00'),
             ('errMsg', None),
             ('totalCount', '2'),
             ('countPerPage', '10'),
             ('totalPage', '1'),
             ('currentPage', '1')])
'''

print( rsp_dict.itemDataFrame().head() )
'''
   zipNo                lnmAdres             rnAdres
0  12621    경기도 여주시 세종로 17 (홍문동)  경기도 여주시 홍문동 111-15
1  12621  경기도 여주시 세종로 17-1 (홍문동)   경기도 여주시 홍문동 111-2
'''