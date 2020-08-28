
<!-- TOC -->

- [1. PyDataGoKr](#1-pydatagokr)
- [2. Usage](#2-usage)
    - [2.1. Simple](#21-simple)
    - [2.2. Detail](#22-detail)
- [3. Supported API List](#3-supported-api-list)
- [4. Installation](#4-installation)

<!-- /TOC -->


# 1. PyDataGoKr

PyDataGoKr 은 공공데이터 Open API 의 python wrapper

# 2. Usage
## 2.1. Simple

```python
import data_go_kr as dgk

SVC_KEY = dgk.test_svc_key() # fix it to your SVC_KEY

# 새주소 5자리 우편번호 조회서비스. ( 도로명 주소 )
reply = dgk.getNewAddressListAreaCd.get_reply(serviceKey=SVC_KEY, searchSe='road', srchwrd='세종로 17')
print(reply.df())
'''
   zipNo                lnmAdres             rnAdres
0  12621    경기도 여주시 세종로 17 (홍문동)  경기도 여주시 홍문동 111-15
1  12621  경기도 여주시 세종로 17-1 (홍문동)   경기도 여주시 홍문동 111-2
'''

# 새주소 5자리 우편번호 조회서비스. ( 우편번호 )
params = {
    'serviceKey' : SVC_KEY,
    'searchSe' : 'post',
    'srchwrd' : '12621'
}
reply = dgk.getNewAddressListAreaCd.get_reply(**params)
print(reply.df())
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

```

## 2.2. Detail

```python
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
```

# 3. Supported API List

```bash
   cat                             name                           flag  desc                          
0   retrieveNewAdressAreaCdService  getNewAddressListAreaCd        o     새주소 5자리 우편번호 조회서비스           
1   RTMSOBJSvc                      getRTMSDataSvcAptTrade         o     아파트매매 실거래자료                  
2   RTMSOBJSvc                      getRTMSDataSvcRHTrade          o     연립다세대 매매 실거래자료               
3   RTMSOBJSvc                      getRTMSDataSvcSHTrade          o     단독/다가구 매매 실거래 자료             
4   Covid19                         getCovid19GenAgeCaseInfJson    o     보건복지부_코로나19연령별,성별감염_현황 조회 서비스
5   Covid19                         getCovid19InfStateJson         o     보건복지부_코로나19감염현황 조회 서비스       
6   Covid19                         getCovid19SidoInfStateJson     o     보건복지부_코로나19시,도발생_현황 조회 서비스   
7   ArpltnInforInqireSvc            getMsrstnAcctoRltmMesureDnsty  TODO  측정소별 실시간 측정정보 조회             
8   MsrstnInfoInqireSvc             getMsrstnList                  TODO  측정소 목록 조회                    
9   MsrstnInfoInqireSvc             getNearbyMsrstnList            TODO  측정소정보 조회 서비스                 
10  MsrstnInfoInqireSvc             getTMStdrCrdnt                 TODO  TM 기준좌표 조회    
```

# 4. Installation
- TODO


