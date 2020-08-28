import pprint
import data_go_kr as dgk

SVC_KEY = dgk.test_svc_key() # fix it to your SVC_KEY

reply = dgk.getNewAddressListAreaCd.get_reply(serviceKey=SVC_KEY, searchSe='road', srchwrd='세종로 17')

rsp = reply.rsp()  # requests.model.Response
rsp_content = reply.rsp_content() # data_go_kr.api.getNewAddressListAreaCd.RspContent inherit OrderedDict
df = reply.df() # pandas.core.frame.DataFrame

print(type(rsp))
print(type(rsp_content))
print(type(df))

print('status_code:', rsp.status_code)
pprint.pprint(rsp_content['NewAddressListResponse']['cmmMsgHeader'])
'''
OrderedDict([('requestMsgId', None),
             ('responseMsgId', None),
             ('responseTime', '20200828:161903767'),
             ('successYN', 'Y'),
             ('returnCode', '00'),
             ('errMsg', None),
             ('totalCount', '2'),
             ('countPerPage', '10'),
             ('totalPage', '1'),
             ('currentPage', '1')])
'''