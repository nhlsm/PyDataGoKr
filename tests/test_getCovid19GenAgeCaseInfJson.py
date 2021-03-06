import logging
import sys
import unittest

import data_go_kr
from data_go_kr import getCovid19GenAgeCaseInfJson as svc

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

    def test_rsp_0(self):
        rsp = svc.get_rsp(serviceKey=SVC_KEY, startCreateDt='19990825', endCreateDt='19990825')
        # logging.info('code: %s', rsp.status_code)
        # logging.info('hdr : %s', rsp.headers)
        # logging.info('cont: %s', rsp.content)
        self.assertEqual(rsp.status_code, 200)

        rsp_content = svc.RspContent.fromRsp(rsp)
        # logging.info('\n%s', pprint.pformat(rsp_content))
        # logging.info('resultCode: %s', rsp_content.resultCode())
        # logging.info('resultMsg: %s', rsp_content.resultMsg())
        # logging.info('result: %s', rsp_content.result())
        # logging.info('df\n%s', rsp_content.itemDataFrame() )

        CNT = 0
        self.assertEqual(rsp_content.totalCount(), CNT)
        self.assertEqual(len(rsp_content.itemDictList()), CNT)
        self.assertEqual(len(rsp_content.itemDataFrame()), CNT)

    def test_rsp_11(self):
        rsp = svc.get_rsp(serviceKey=SVC_KEY, startCreateDt='20200823', endCreateDt='20200823')
        # logging.info('code: %s', rsp.status_code)
        # logging.info('hdr : %s', rsp.headers)
        # logging.info('cont: %s', rsp.content)
        self.assertEqual(rsp.status_code, 200)

        rsp_content = svc.RspContent.fromRsp(rsp)
        # logging.info('\n%s', pprint.pformat(rsp_content))
        # logging.info('\n%s', rsp_content.itemDataFrame().head())

        CNT = 11
        self.assertEqual(rsp_content.totalCount(), CNT)
        self.assertEqual(len(rsp_content.itemDictList()), CNT)
        self.assertEqual(len(rsp_content.itemDataFrame()), CNT)


    def test_rsp_110(self):
        rsp = svc.get_rsp(serviceKey=SVC_KEY, startCreateDt='20200801', endCreateDt='20200810')
        # logging.info('code: %s', rsp.status_code)
        # logging.info('hdr : %s', rsp.headers)
        # logging.info('cont: %s', rsp.content)
        self.assertEqual(rsp.status_code, 200)

        rsp_content = svc.RspContent.fromRsp(rsp)
        # logging.info('\n%s', pprint.pformat(rsp_content))
        # logging.info('\n%s', rsp_content.itemDataFrame() )

        CNT = 110
        self.assertEqual(rsp_content.totalCount(), CNT)
        self.assertEqual(len(rsp_content.itemDictList()), CNT)
        self.assertEqual(len(rsp_content.itemDataFrame()), CNT)

    def test_rsp_220(self):
        rsp = svc.get_rsp(serviceKey=SVC_KEY, startCreateDt='20200801', endCreateDt='20200820')
        # logging.info('code: %s', rsp.status_code)
        # logging.info('hdr : %s', rsp.headers)
        # logging.info('cont: %s', rsp.content)
        self.assertEqual(rsp.status_code, 200)

        rsp_content = svc.RspContent.fromRsp(rsp)
        # logging.info('\n%s', pprint.pformat(rsp_content))
        # logging.info('\n%s', rsp_content.itemDataFrame() )

        CNT = 220
        self.assertEqual(rsp_content.totalCount(), CNT)
        self.assertEqual(len(rsp_content.itemDictList()), CNT)
        self.assertEqual(len(rsp_content.itemDataFrame()), CNT)


    def test_get_reply_11(self):
        param = {
            'serviceKey' : SVC_KEY,
            'startCreateDt' : '20200823',
            'endCreateDt' : '20200823'
        }
        reply = svc.get_reply(**param)
        self.assertEqual(len(reply.df()), 11)

        # logging.info('\n%s', reply.df().head())