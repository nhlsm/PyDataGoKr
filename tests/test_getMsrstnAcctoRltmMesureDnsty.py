import logging
import sys
import unittest

import data_go_kr
from data_go_kr import getMsrstnAcctoRltmMesureDnsty as svc


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

    def test_rsp_daily(self):
        rsp = svc.get_rsp(serviceKey=SVC_KEY, stationName='종로구', numOfRows=24, dataTerm='DAILY')
        # logging.info('code: %s', rsp.status_code)
        # logging.info('hdr : %s', rsp.headers)
        # logging.info('cont: %s', rsp.content)
        self.assertEqual(rsp.status_code, 200)

        rsp_content = svc.RspContent.fromRsp(rsp)
        df = rsp_content.itemDataFrame()
        logging.info('totalCount: %s', rsp_content.totalCount())
        logging.info('itemDictList: %s', len(rsp_content.itemDictList()))
        logging.info('itemDataFrame: %s', len(df))
        # logging.info('\n%s', df)
        self.assertEqual(len(df), rsp_content.totalCount())
        # logging.info('\n%s', pprint.pformat(rsp_content) )

    def test_rsp_month(self):
        rsp = svc.get_rsp(serviceKey=SVC_KEY, stationName='종로구', dataTerm='MONTH')
        # logging.info('code: %s', rsp.status_code)
        # logging.info('hdr : %s', rsp.headers)
        # logging.info('cont: %s', rsp.content)
        self.assertEqual(rsp.status_code, 200)

        rsp_content = svc.RspContent.fromRsp(rsp)
        df = rsp_content.itemDataFrame()
        # logging.info('totalCount: %s', rsp_content.totalCount())
        # logging.info('itemDictList: %s', len(rsp_content.itemDictList()))
        # logging.info('itemDataFrame: %s', len(df))
        self.assertEqual(len(df), rsp_content.totalCount())


    def test_rsp_3month(self):
        rsp = svc.get_rsp(serviceKey=SVC_KEY, stationName='종로구', dataTerm='3MONTH', ver='1.3')
        # logging.info('code: %s', rsp.status_code)
        # logging.info('hdr : %s', rsp.headers)
        # logging.info('cont: %s', rsp.content)
        self.assertEqual(rsp.status_code, 200)

        rsp_content = svc.RspContent.fromRsp(rsp)
        df = rsp_content.itemDataFrame()
        # logging.info('totalCount: %s', rsp_content.totalCount())
        # logging.info('itemDictList: %s', len(rsp_content.itemDictList()))
        # logging.info('itemDataFrame: %s', len(df))
        self.assertEqual(len(df), rsp_content.totalCount())

    def test_reply(self):
        reply = svc.get_reply(serviceKey=SVC_KEY, stationName='종로구', dataTerm='DAILY')
        self.assertEqual( reply.rsp_content().totalCount(), len(reply.df()))

        reply = svc.get_reply(serviceKey=SVC_KEY, stationName='종로구', dataTerm='MONTH')
        self.assertEqual( reply.rsp_content().totalCount(), len(reply.df()))

        reply = svc.get_reply(serviceKey=SVC_KEY, stationName='종로구', dataTerm='3MONTH')
        self.assertEqual( reply.rsp_content().totalCount(), len(reply.df()))
