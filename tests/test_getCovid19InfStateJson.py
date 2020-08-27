import logging
import sys
import pprint
import enum
import typing
import unittest
from collections import OrderedDict

import requests
import xmltodict
import pandas as pd

from data_go_kr import getCovid19InfStateJson as svc

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

        global SVC_KEY
        with open('../SVC_KEY.txt', 'r') as f:
            SVC_KEY = f.read()

    def test_req_0(self):
        rsp = svc.req(serviceKey=SVC_KEY, startCreateDt='19990825', endCreateDt='19990825')
        # logging.info('code: %s', rsp.status_code)
        # logging.info('hdr : %s', rsp.headers)
        # logging.info('cont: %s', rsp.content)
        self.assertEqual(rsp.status_code, 200)

        # rsp_dict = svc.RspDict(xmltodict.parse(rsp.content))
        rsp_dict = svc.RspDict.fromRsp(rsp)
        # logging.info('\n%s', pprint.pformat(rsp_dict))
        # logging.info('resultCode: %s', rsp_dict.resultCode())
        # logging.info('resultMsg: %s', rsp_dict.resultMsg())
        # logging.info('result: %s', rsp_dict.result())
        # logging.info('df\n%s', rsp_dict.itemDataFrame() )

        CNT = 0
        self.assertEqual(rsp_dict.totalCount(), CNT)
        self.assertEqual(len(rsp_dict.itemDictList()), CNT)
        self.assertEqual(len(rsp_dict.itemDataFrame()), CNT)

    def test_req_1(self):
        rsp = svc.req(serviceKey=SVC_KEY, startCreateDt='20200825', endCreateDt='20200825')
        # logging.info('code: %s', rsp.status_code)
        # logging.info('hdr : %s', rsp.headers)
        # logging.info('cont: %s', rsp.content)
        self.assertEqual(rsp.status_code, 200)

        # rsp_dict = svc.RspDict(xmltodict.parse(rsp.content))
        rsp_dict = svc.RspDict.fromRsp(rsp)
        # logging.info('\n%s', pprint.pformat(rsp_dict))

        CNT = 1
        self.assertEqual(rsp_dict.totalCount(), CNT)
        self.assertEqual(len(rsp_dict.itemDictList()), CNT)
        self.assertEqual(len(rsp_dict.itemDataFrame()), CNT)
        # logging.info('\n%s', rsp_dict.itemDataFrame() )

    def test_req_10(self):
        rsp = svc.req(serviceKey=SVC_KEY, startCreateDt='20200801', endCreateDt='20200810')
        # logging.info('code: %s', rsp.status_code)
        # logging.info('hdr : %s', rsp.headers)
        # logging.info('cont: %s', rsp.content)
        self.assertEqual(rsp.status_code, 200)

        # rsp_dict = svc.RspDict(xmltodict.parse(rsp.content))
        rsp_dict = svc.RspDict.fromRsp(rsp)
        # logging.info('\n%s', pprint.pformat(rsp_dict))
        # logging.info('\n%s', rsp_dict.itemDataFrame() )

        CNT = 10
        self.assertEqual(rsp_dict.totalCount(), CNT)
        self.assertEqual(len(rsp_dict.itemDictList()), CNT)
        self.assertEqual(len(rsp_dict.itemDataFrame()), CNT)

    def test_req_126(self):
        rsp = svc.req(serviceKey=SVC_KEY, startCreateDt='20200401', endCreateDt='20200801')
        # logging.info('code: %s', rsp.status_code)
        # logging.info('hdr : %s', rsp.headers)
        # logging.info('cont: %s', rsp.content)
        self.assertEqual(rsp.status_code, 200)

        # rsp_dict = svc.RspDict(xmltodict.parse(rsp.content))
        rsp_dict = svc.RspDict.fromRsp(rsp)
        # logging.info('\n%s', pprint.pformat(rsp_dict))

        CNT = 126
        self.assertEqual(rsp_dict.totalCount(), CNT)
        self.assertEqual(len(rsp_dict.itemDictList()), CNT)
        self.assertEqual(len(rsp_dict.itemDataFrame()), CNT)
        # logging.info('\n%s', rsp_dict.itemDataFrame() )
