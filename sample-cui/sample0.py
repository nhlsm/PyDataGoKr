import pprint

import data_go_kr
from data_go_kr import getNewAddressListAreaCd

SVC_KEY = data_go_kr.test_svc_key() # fix it to your SVC_KEY

# 새주소 5자리 우편번호 조회서비스. ( 도로명 주소 )
hdr, df = getNewAddressListAreaCd.get_df(serviceKey=SVC_KEY, searchSe='road', srchwrd='세종로 17')
pprint.pprint(hdr)
'''
OrderedDict([('requestMsgId', None),
             ('responseMsgId', None),
             ('responseTime', '20200827:221446136'),
             ('successYN', 'Y'),
             ('returnCode', '00'),
             ('errMsg', None),
             ('totalCount', '2'),
             ('countPerPage', '10'),
             ('totalPage', '1'),
             ('currentPage', '1')])
'''
print(df)

'''
   zipNo                lnmAdres             rnAdres
0  12621    경기도 여주시 세종로 17 (홍문동)  경기도 여주시 홍문동 111-15
1  12621  경기도 여주시 세종로 17-1 (홍문동)   경기도 여주시 홍문동 111-2
'''

# 새주소 5자리 우편번호 조회서비스. ( 우편번호 ) - req 가 여러번 발생하고, hdr 는 마지막 요청의 hdr.
params = {
    'serviceKey' : SVC_KEY,
    'searchSe' : 'post',
    'srchwrd' : '12621'
}
hdr, df = getNewAddressListAreaCd.get_df(**params)
pprint.pprint(hdr)
'''
OrderedDict([('requestMsgId', None),
             ('responseMsgId', None),
             ('responseTime', '20200827:221312584'),
             ('successYN', 'Y'),
             ('returnCode', '00'),
             ('errMsg', None),
             ('totalCount', '168'),
             ('countPerPage', '10'),
             ('totalPage', '17'),
             ('currentPage', '17')])
'''

print(df)
'''
     zipNo                             lnmAdres                  rnAdres
0    12621                  경기도 여주시 세종로 7 (홍문동)        경기도 여주시 홍문동 105-1
1    12621                경기도 여주시 세종로 7-7 (홍문동)        경기도 여주시 홍문동 120-7
2    12621                경기도 여주시 세종로 7-8 (홍문동)       경기도 여주시 홍문동 120-10
3    12621                  경기도 여주시 세종로 9 (홍문동)        경기도 여주시 홍문동 107-3
4    12621           경기도 여주시 세종로 11 (홍문동, 여주빌딩)     경기도 여주시 홍문동 110 여주빌딩
..     ...                                  ...                      ...
163  12621  경기도 여주시 청심로166번길 20-4 (홍문동, 가로판매대4)  경기도 여주시 홍문동 81-9 가로판매대4
164  12621  경기도 여주시 청심로166번길 20-5 (홍문동, 가로판매대5)  경기도 여주시 홍문동 81-9 가로판매대5
165  12621  경기도 여주시 청심로166번길 20-6 (홍문동, 가로판매대6)  경기도 여주시 홍문동 81-9 가로판매대6
166  12621  경기도 여주시 청심로166번길 20-7 (홍문동, 가로판매대7)  경기도 여주시 홍문동 81-9 가로판매대7
167  12621  경기도 여주시 청심로166번길 20-8 (홍문동, 가로판매대8)  경기도 여주시 홍문동 81-9 가로판매대8

[168 rows x 3 columns]
'''
