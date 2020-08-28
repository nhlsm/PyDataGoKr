# import sys
# import importlib

__version__ = '0.0.3'
'''
v0.0.3
SC-OA-09-01 측정소정보 조회 서비스        MsrstnInfoInqireSvc
    getNearbyMsrstnList 근접측정소 목록 조회
    getMsrstnList   측정소 목록 조회
    getTMStdrCrdnt  TM 기준좌표 조회

SC-OA-09-02 대기오염정보 조회 서비스      ArpltnInforInqireSvc
    getMsrstnAcctoRltmMesureDnsty   측정소별 실시간 측정정보 조회    
    getUnityAirEnvrnIdexSnstiveAboveMsrstnList  통합대기환경지수 나쁨 이상 측정소 목록조회 
    getCtprvnRltmMesureDnsty    시도별 실시간 측정정보 조회
    getMinuDustFrcstDspth   대기질 예보통보 조회
    getCtprvnMesureLIst 시도별 실시간 평균정보 조회
    getCtprvnMesureSidoLIst 시군구별 실시간 평균정보 조회

SC-OA-09-03 대기오염통계 서비스           ArpltnStatsSvc
    getMsrstnAcctoLastDcsnDnsty 측정소별 최종확정 농도 조회
    getDatePollutnStatInfo  기간별 오염통계 정보 조회

SC-OA-09-04 오존황사 발생정보조회 서비스   OzYlwsndOccrrncInforInqireSvc
    getOzAdvsryOccrrncInfo  오존주의보 발생정보 조회
    getYlwsndAdvsryOccrrncInfo  황사주의보 발생정보 조회

SC-OA-09-05 미세먼지 경보 정보 조회 서비스 UlfptcaAlarmInqireSvc
    getUlfptcaAlarmInfo 미세먼지 경보 현황 조회


v0.0.2
get_rsp, get_reply

v0.0.1 
1st

'''

# TODO : refer to pandas/__init__.py

from data_go_kr.api import (
    # 도로명 주소
    getNewAddressListAreaCd,
    # 부동산 실거래
    getRTMSDataSvcAptTrade,
    getRTMSDataSvcRHTrade,
    getRTMSDataSvcSHTrade,
    # 코로나19
    getCovid19GenAgeCaseInfJson,
    getCovid19InfStateJson,
    getCovid19SidoInfStateJson,
    # 에어코리아
    # 측정소정보 조회 서비스
    getNearbyMsrstnList,    # 근접측정소 목록 조회
    getMsrstnList,          # 측정소 목록 조회
    getTMStdrCrdnt,         # TM 기준좌표 조회
    # 대기오염정보 조회 서비스
    getMsrstnAcctoRltmMesureDnsty, # 측정소별 실시간 측정정보 조회
    # getUnityAirEnvrnIdexSnstiveAboveMsrstnList, # 통합대기환경지수 나쁨 이상 측정소 목록조회
    # getCtprvnRltmMesureDnsty, # 시도별 실시간 측정정보 조회
    # getMinuDustFrcstDspth, #대기질 예보통보 조회
    # getCtprvnMesureLIst, #시도별 실시간 평균정보 조회
    # getCtprvnMesureSidoLIst, #시군구별 실시간 평균정보 조회
    # 대기오염통계 서비스
    # getMsrstnAcctoLastDcsnDnsty, # 측정소별 최종확정 농도 조회
    # getDatePollutnStatInfo, #  기간별 오염통계 정보 조회
    # 오존황사 발생정보조회 서비스
    # getOzAdvsryOccrrncInfo, # 오존주의보 발생정보 조회
    # getYlwsndAdvsryOccrrncInfo, # 황사주의보 발생정보 조회
    # 미세먼지 경보 정보 조회 서비스
    # getUlfptcaAlarmInfo, # 미세먼지 경보 현황 조회
)

#
# def __bootstrap():
#     print('__bootstrap:', __name__)
#     for mod_name in __all__:
#         # print(mod_name)
#         # mod = importlib.import_module(__name__ + '.' + mod_name)
#         # mod = importlib.import_module(mod_name, __name__)
#         # print(mod)
#         importlib.import_module(__name__ + '.' + mod_name)
#
# __bootstrap()

def test_svc_key():
    '''
    just for test.
    :return: service key
    '''
    try:
        with open('../SVC_KEY.txt', 'r') as f:
            return f.read()
    except Exception as e:
        print('### PREPARE "../SVC_KEY.txt" file for test')
        raise e