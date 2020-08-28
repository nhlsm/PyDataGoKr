# import sys
# import importlib

__version__ = '0.0.2'
'''
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
    # covid
    getMsrstnAcctoRltmMesureDnsty,
    getMsrstnList,
    getNearbyMsrstnList,
    getTMStdrCrdnt,
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