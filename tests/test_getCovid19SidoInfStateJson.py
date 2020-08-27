import logging
import sys
import unittest

import pandas as pd

from data_go_kr import getCovid19SidoInfStateJson as svc


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

    def test_req_19(self):
        rsp = svc.req(serviceKey=SVC_KEY, startCreateDt='20200823', endCreateDt='20200823')
        # logging.info('code: %s', rsp.status_code)
        # logging.info('hdr : %s', rsp.headers)
        # logging.info('cont: %s', rsp.content)
        self.assertEqual(rsp.status_code, 200)

        # rsp_dict = svc.RspDict(xmltodict.parse(rsp.content))
        rsp_dict = svc.RspDict.fromRsp(rsp)
        # logging.info('\n%s', pprint.pformat(rsp_dict))
        # logging.info('\n%s', rsp_dict.itemDataFrame())

        CNT = 19
        self.assertEqual(rsp_dict.totalCount(), CNT)
        self.assertEqual(len(rsp_dict.itemDictList()), CNT)
        self.assertEqual(len(rsp_dict.itemDataFrame()), CNT)

    def test_req_209(self):
        rsp = svc.req(serviceKey=SVC_KEY, startCreateDt='20200801', endCreateDt='20200810')
        # logging.info('code: %s', rsp.status_code)
        # logging.info('hdr : %s', rsp.headers)
        # logging.info('cont: %s', rsp.content)
        self.assertEqual(rsp.status_code, 200)

        # rsp_dict = svc.RspDict(xmltodict.parse(rsp.content))
        rsp_dict = svc.RspDict.fromRsp(rsp)
        # logging.info('\n%s', pprint.pformat(rsp_dict))
        # logging.info('\n%s', rsp_dict.itemDataFrame() )
        # logging.info('%s', rsp_dict.totalCount() )

        CNT = 209
        self.assertEqual(rsp_dict.totalCount(), CNT)
        self.assertEqual(len(rsp_dict.itemDictList()), CNT)
        self.assertEqual(len(rsp_dict.itemDataFrame()), CNT)

    def __test_req_loop(self):
        # lawd_df = lawd_05('o')
        # logging.info('key: %s', lawd_df['법정동코드'] )
        # r = pd.date_range(start='20000101', end='20200801', freq='M')
        # r = pd.date_range(start='20060101', end='20061201', freq='M')
        # r = pd.date_range(start='20200315', end='20200415', freq='D')
        r = pd.date_range(start='20200601', end='20200610', freq='D')
        lst = r.format(formatter=lambda x: x.strftime('%Y%m%d'))
        # logging.info('key: %s', type(lst) )
        # logging.info('r: %s', r)
        logging.info('lst: %s', lst )
        for yyyymmdd in lst:
            # rsp = svc.req(serviceKey=SVC_KEY, LAWD_CD='11110', DEAL_YMD=yyyymm)
            # rsp = svc.req(serviceKey=SVC_KEY, LAWD_CD='28177', DEAL_YMD=yyyymm)
            rsp = svc.req(serviceKey=SVC_KEY, startCreateDt=yyyymmdd, endCreateDt=yyyymmdd)
            # logging.info('code: %s', rsp.status_code)
            # logging.info('hdr : %s', rsp.headers)
            # logging.info('cont: %s', rsp.content)
            # self.assertEqual(rsp.status_code, 200)
            # rsp_dict = svc.RspDict(xmltodict.parse(rsp.content))
            rsp_dict = svc.RspDict.fromRsp(rsp)
            logging.info('%s: %s', yyyymmdd, rsp_dict.totalCount() )


