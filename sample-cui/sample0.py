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