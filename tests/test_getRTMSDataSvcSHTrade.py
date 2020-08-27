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

from data_go_kr import getRTMSDataSvcSHTrade as svc
from data_go_kr.utils.dong_code import *

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

    def test_req_44(self):
        rsp = svc.req(serviceKey=SVC_KEY, LAWD_CD='11110', DEAL_YMD='201512')
        # logging.info('code: %s', rsp.status_code)
        # logging.info('hdr : %s', rsp.headers)
        # logging.info('cont: %s', rsp.content)
        self.assertEqual(rsp.status_code, 200)

        # rsp_dict = svc.RspDict(xmltodict.parse(rsp.content))
        rsp_dict = svc.RspDict.fromRsp(rsp)
        # logging.info('\n%s', pprint.pformat(rsp_dict))

        CNT = 44
        self.assertEqual(rsp_dict.totalCount(), CNT)
        self.assertEqual(len(rsp_dict.itemDictList()), CNT)
        self.assertEqual(len(rsp_dict.itemDataFrame()), CNT)

    def test_req_127(self):
        rsp = svc.req(serviceKey=SVC_KEY, LAWD_CD='50110', DEAL_YMD='201601')
        # logging.info('code: %s', rsp.status_code)
        # logging.info('hdr : %s', rsp.headers)
        # logging.info('cont: %s', rsp.content)
        self.assertEqual(rsp.status_code, 200)

        # rsp_dict = svc.RspDict(xmltodict.parse(rsp.content))
        rsp_dict = svc.RspDict.fromRsp(rsp)
        # logging.info('\n%s', pprint.pformat(rsp_dict))

        CNT = 127
        self.assertEqual(rsp_dict.totalCount(), CNT)
        self.assertEqual(len(rsp_dict.itemDictList()), CNT)
        self.assertEqual(len(rsp_dict.itemDataFrame()), CNT)
        # logging.info('\n%s', rsp_dict.itemDataFrame() )


    def test_req_0(self):
        rsp = svc.req(serviceKey=SVC_KEY, LAWD_CD='1111z', DEAL_YMD='201512')
        # logging.info('code: %s', rsp.status_code)
        # logging.info('hdr : %s', rsp.headers)
        # logging.info('cont: %s', rsp.content)
        self.assertEqual(rsp.status_code, 200)

        # rsp_dict = svc.RspDict(xmltodict.parse(rsp.content))
        rsp_dict = svc.RspDict.fromRsp(rsp)
        # logging.info('\n%s', pprint.pformat(rsp_dict))

        CNT = 0
        self.assertEqual(rsp_dict.totalCount(), CNT)
        self.assertEqual(len(rsp_dict.itemDictList()), CNT)
        self.assertEqual(len(rsp_dict.itemDataFrame()), CNT)

    def test_req_1(self):
        rsp = svc.req(serviceKey=SVC_KEY, LAWD_CD='42790', DEAL_YMD='200601')
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

    def test_req_2(self):
        rsp = svc.req(serviceKey=SVC_KEY, LAWD_CD='42790', DEAL_YMD='201602')
        # logging.info('code: %s', rsp.status_code)
        # logging.info('hdr : %s', rsp.headers)
        # logging.info('cont: %s', rsp.content)
        self.assertEqual(rsp.status_code, 200)

        # rsp_dict = svc.RspDict(xmltodict.parse(rsp.content))
        rsp_dict = svc.RspDict.fromRsp(rsp)
        # logging.info('\n%s', pprint.pformat(rsp_dict))

        CNT = 2
        self.assertEqual(rsp_dict.totalCount(), CNT)
        self.assertEqual(len(rsp_dict.itemDictList()), CNT)
        self.assertEqual(len(rsp_dict.itemDataFrame()), CNT)


    def _test_req_loop(self):
        # lawd_df = lawd_05('o')
        # logging.info('key: %s', lawd_df['법정동코드'] )
        # r = pd.date_range(start='20000101', end='20200801', freq='M')
        r = pd.date_range(start='20060101', end='20061201', freq='M')
        # r = pd.date_range(start='20160101', end='20161201', freq='M')
        lst = r.format(formatter=lambda x: x.strftime('%Y%m'))
        # logging.info('key: %s', type(lst) )
        # logging.info('key: %s', lst )
        for yyyymm in lst:
            # rsp = svc.req(serviceKey=SVC_KEY, LAWD_CD='11110', DEAL_YMD=yyyymm) # 서울 종로구
            # rsp = svc.req(serviceKey=SVC_KEY, LAWD_CD='28177', DEAL_YMD=yyyymm) # 인천 미추홀
            # rsp = svc.req(serviceKey=SVC_KEY, LAWD_CD='50110', DEAL_YMD=yyyymm) # 제주 제주시
            rsp = svc.req(serviceKey=SVC_KEY, LAWD_CD='42790', DEAL_YMD=yyyymm) # 강원도 화천군
            # logging.info('code: %s', rsp.status_code)
            # logging.info('hdr : %s', rsp.headers)
            # logging.info('cont: %s', rsp.content)
            # self.assertEqual(rsp.status_code, 200)
            # rsp_dict = svc.RspDict(xmltodict.parse(rsp.content))
            rsp_dict = svc.RspDict.fromRsp(rsp)
            logging.info('%s: %s', yyyymm, rsp_dict.totalCount() )

