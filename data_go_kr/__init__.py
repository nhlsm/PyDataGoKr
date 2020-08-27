# import sys
import importlib

__version__ = '0.0.1'

__all__ = [
    'getCovid19GenAgeCaseInfJson',
    'getCovid19InfStateJson',
    'getCovid19SidoInfStateJson',
    'getMsrstnAcctoRltmMesureDnsty',
    'getMsrstnList',
    'getNearbyMsrstnList',
    'getNewAddressListAreaCd',
    'getRTMSDataSvcAptTrade',
    'getRTMSDataSvcRHTrade',
    'getRTMSDataSvcSHTrade',
    'getTMStdrCrdnt',
]

# TODO : refer to pandas/__init__.py

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