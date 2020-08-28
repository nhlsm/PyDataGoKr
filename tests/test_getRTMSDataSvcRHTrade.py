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

import data_go_kr
from data_go_kr import getRTMSDataSvcRHTrade as svc
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
        SVC_KEY = data_go_kr.test_svc_key()

    def test_rsp_40(self):
        rsp = svc.get_rsp(serviceKey=SVC_KEY, LAWD_CD='11110', DEAL_YMD='201512')
        # logging.info('code: %s', rsp.status_code)
        # logging.info('hdr : %s', rsp.headers)
        # logging.info('cont: %s', rsp.content)
        self.assertEqual(rsp.status_code, 200)

        rsp_content = svc.RspContent.fromRsp(rsp)
        # logging.info('\n%s', pprint.pformat(rsp_content))

        CNT = 40
        self.assertEqual(rsp_content.totalCount(), CNT)
        self.assertEqual(len(rsp_content.itemDictList()), CNT)
        self.assertEqual(len(rsp_content.itemDataFrame()), CNT)

    def test_rsp_198(self):
        rsp = svc.get_rsp(serviceKey=SVC_KEY, LAWD_CD='50110', DEAL_YMD='201601')
        # logging.info('code: %s', rsp.status_code)
        # logging.info('hdr : %s', rsp.headers)
        # logging.info('cont: %s', rsp.content)
        self.assertEqual(rsp.status_code, 200)

        rsp_content = svc.RspContent.fromRsp(rsp)
        # logging.info('\n%s', pprint.pformat(rsp_content))

        CNT = 198
        self.assertEqual(rsp_content.totalCount(), CNT)
        self.assertEqual(len(rsp_content.itemDictList()), CNT)
        self.assertEqual(len(rsp_content.itemDataFrame()), CNT)
        # logging.info('\n%s', rsp_content.itemDataFrame() )


    def test_rsp_0(self):
        rsp = svc.get_rsp(serviceKey=SVC_KEY, LAWD_CD='1111z', DEAL_YMD='201512')
        # logging.info('code: %s', rsp.status_code)
        # logging.info('hdr : %s', rsp.headers)
        # logging.info('cont: %s', rsp.content)
        self.assertEqual(rsp.status_code, 200)

        rsp_content = svc.RspContent.fromRsp(rsp)
        # logging.info('\n%s', pprint.pformat(rsp_content))

        CNT = 0
        self.assertEqual(rsp_content.totalCount(), CNT)
        self.assertEqual(len(rsp_content.itemDictList()), CNT)
        self.assertEqual(len(rsp_content.itemDataFrame()), CNT)

    def test_rsp_2(self):
        rsp = svc.get_rsp(serviceKey=SVC_KEY, LAWD_CD='42790', DEAL_YMD='200601')
        # logging.info('code: %s', rsp.status_code)
        # logging.info('hdr : %s', rsp.headers)
        # logging.info('cont: %s', rsp.content)
        self.assertEqual(rsp.status_code, 200)

        rsp_content = svc.RspContent.fromRsp(rsp)
        # logging.info('\n%s', pprint.pformat(rsp_content))

        CNT = 2
        self.assertEqual(rsp_content.totalCount(), CNT)
        self.assertEqual(len(rsp_content.itemDictList()), CNT)
        self.assertEqual(len(rsp_content.itemDataFrame()), CNT)

    def test_rsp_1(self):
        rsp = svc.get_rsp(serviceKey=SVC_KEY, LAWD_CD='42790', DEAL_YMD='200602')
        # logging.info('code: %s', rsp.status_code)
        # logging.info('hdr : %s', rsp.headers)
        # logging.info('cont: %s', rsp.content)
        self.assertEqual(rsp.status_code, 200)

        rsp_content = svc.RspContent.fromRsp(rsp)
        # logging.info('\n%s', pprint.pformat(rsp_content))

        CNT = 1
        self.assertEqual(rsp_content.totalCount(), CNT)
        self.assertEqual(len(rsp_content.itemDictList()), CNT)
        self.assertEqual(len(rsp_content.itemDataFrame()), CNT)


    def __test_rsp_loop(self):
        # lawd_df = lawd_05('o')
        # logging.info('key: %s', lawd_df['법정동코드'] )
        # r = pd.date_range(start='20000101', end='20200801', freq='M')
        r = pd.date_range(start='20060101', end='20061201', freq='M')
        # r = pd.date_range(start='20160101', end='20161201', freq='M')
        lst = r.format(formatter=lambda x: x.strftime('%Y%m'))
        # logging.info('key: %s', type(lst) )
        # logging.info('key: %s', lst )
        for yyyymm in lst:
            # rsp = svc.get_rsp(serviceKey=SVC_KEY, LAWD_CD='11110', DEAL_YMD=yyyymm) # 서울 종로구
            # rsp = svc.get_rsp(serviceKey=SVC_KEY, LAWD_CD='28177', DEAL_YMD=yyyymm) # 인천 미추홀
            # rsp = svc.get_rsp(serviceKey=SVC_KEY, LAWD_CD='50110', DEAL_YMD=yyyymm) # 제주 제주시
            rsp = svc.get_rsp(serviceKey=SVC_KEY, LAWD_CD='42790', DEAL_YMD=yyyymm) # 강원도 화천군
            # logging.info('code: %s', rsp.status_code)
            # logging.info('hdr : %s', rsp.headers)
            # logging.info('cont: %s', rsp.content)
            # self.assertEqual(rsp.status_code, 200)
            rsp_content = svc.RspContent.fromRsp(rsp)
            logging.info('%s: %s', yyyymm, rsp_content.totalCount() )

