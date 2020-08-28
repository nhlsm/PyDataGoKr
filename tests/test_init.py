import os
import sys
import logging
import importlib

import unittest

import data_go_kr as dgk

def category_from_url(url:str) -> str:
    return os.path.basename( os.path.dirname(url) )

class Test0(unittest.TestCase):
    """
    Test that the result sum of all numbers
    """

    @classmethod
    def setUpClass(cls):
        # debug
        LOG_FORMAT = '%(pathname)s:%(lineno)03d - %(message)s'
        # LOG_LEVEL = logging.DEBUG  # DEBUG(10), INFO(20), (0~50)
        LOG_LEVEL = logging.INFO  # DEBUG(10), INFO(20), (0~50)
        logging.basicConfig(format=LOG_FORMAT, level=LOG_LEVEL, stream=sys.stdout)

    def test_0(self):
        # logging.info('dtypes: %s', LAWD_CODE.dtypes)
        # logging.info('key: %s', dong_code.LAWD_CODE )
        # for k,v in data_go_kr.__dict__.items():
        #     logging.info('%s, %s, %s', k,v, type(v) )
        #
        # for mod_name in dgk.__all__:
        #     logging.info('%s', mod_name )
        #     mod = importlib.import_module( 'data_go_kr.' + mod_name)
        #     logging.info('  %s', mod.SVC_DESC)
        #     logging.info('  %s', mod.SVC_URL)
        #     logging.info('  %s', mod.SVC_FLAG)
        #     logging.info('  %s', category_from_url(mod.SVC_URL)  )
        #
        # # TODO: 1) sort by url, 2) make df  3) TODO or COMPLETE
        # logging.info('name: %s', getCovid19GenAgeCaseInfJson.SVC_DESC )
        # for m in sys.modules:
        #     if 'go' in m:
        #         logging.info('m: %s', m )
        pass
