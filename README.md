
<!-- TOC -->

- [1. PyDataGoKr](#1-pydatagokr)
- [2. Usage](#2-usage)
    - [2.1. Simple](#21-simple)
    - [2.2. Complex](#22-complex)
- [3. Support](#3-support)
- [4. Installation](#4-installation)

<!-- /TOC -->


# 1. PyDataGoKr

PyDataGoKr 은 공공데이터 Open API 의 python wrapper 임.
- 요청은 requests 를 이용함.
- 응답은 OrderedDict, DataFrame 형태로 반환함.

# 2. Usage
## 2.1. Simple
- 결과값만 필요한 경우.
```python
import data_go_kr as dgk

SVC_KEY = dgk.test_svc_key()

# 새주소 5자리 우편번호 조회서비스
df = dgk.getNewAddressListAreaCd.get_df(serviceKey=SVC_KEY, searchSe='road', srchwrd='세종로 17')
print(df)

'''
   zipNo                lnmAdres             rnAdres
0  12621    경기도 여주시 세종로 17 (홍문동)  경기도 여주시 홍문동 111-15
1  12621  경기도 여주시 세종로 17-1 (홍문동)   경기도 여주시 홍문동 111-2
'''

# 보건복지부_코로나19연령별,성별감염_현황 조회 서비스
param = {
    'serviceKey' : SVC_KEY,
    'startCreateDt' : '20200823',
    'endCreateDt' : '20200823'
}
df = dgk.getCovid19GenAgeCaseInfJson.get_df(**param)
print(df.head())
'''
  confCase confCaseRate                 createDt  ...  gubun   seq updateDt
0      344         1.98  2020-08-23 10:24:13.605  ...    0-9  2840     null
1     1015         5.83  2020-08-23 10:24:13.605  ...  10-19  2839     null
2     4010        23.05  2020-08-23 10:24:13.605  ...  20-29  2838     null
3     2191        12.59  2020-08-23 10:24:13.605  ...  30-39  2837     null
4     2343        13.47  2020-08-23 10:24:13.605  ...  40-49  2836     null

[5 rows x 9 columns]
'''
```

## 2.2. Complex
- response 헤더가 필요한 경우.

```python
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
```

# 3. Support

```bash
TODO
```

# 4. Installation
- TODO


