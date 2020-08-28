import logging
import pprint
import sys
import unittest

import data_go_kr
import data_go_kr.api.statisticsList as svc

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

    def __test_rsp(self):
        rsp = svc.get_rsp(serviceKey=SVC_KEY, tmX='244148.546388', tmY='412423.75772')
        # logging.info('code: %s', rsp.status_code)
        logging.info('hdr : %s', rsp.headers)
        logging.info('cont: %s', rsp.content)
        self.assertEqual(rsp.status_code, 200)

        rsp_content = svc.RspContent.fromRsp(rsp)
        # logging.info('\n%s', pprint.pformat(rsp_content))
        # logging.info('resultCode: %s', rsp_content.resultCode())
        # logging.info('resultMsg: %s', rsp_content.resultMsg())
        # logging.info('result: %s', rsp_content.result())
        # logging.info('df\n%s', rsp_content.itemDataFrame() )

        CNT = 525
        self.assertEqual(rsp_content.totalCount(), CNT)

        # reply = svc.get_reply(serviceKey=SVC_KEY, tmX='244148.546388', tmY='412423.75772')
        # df = reply.df()
        # logging.info('tot: %s', reply.rsp_content().totalCount() )
        # logging.info('len: %s', len(df) )
        # # logging.info('df\n%s', df )
        # logging.info('v1.0: %s', df.columns.values )
        #
        # reply = svc.get_reply(serviceKey=SVC_KEY, tmX='244148.546388', tmY='412423.75772', ver='1.1')
        # df = reply.df()
        # logging.info('tot: %s', reply.rsp_content().totalCount() )
        # logging.info('len: %s', len(df) )
        # # logging.info('df\n%s', df )
        # logging.info('v1.1: %s', df.columns.values )
    #
    # def __test_rsp_525_loop(self):
    #     rsp = svc.get_rsp(serviceKey=SVC_KEY, tmX='244148.546388', tmY='412423.75772'
    #                       , numOfRows=100
    #                       , pageNo=1
    #                       )
    #     self.assertEqual(rsp.status_code, 200)
    #
    #     rsp_content = svc.RspContent.fromRsp(rsp)
    #     logging.info('numOfRows: %s', rsp_content.numOfRows())
    #     logging.info('pageNo: %s', rsp_content.pageNo())
    #     logging.info('totalCount: %s', rsp_content.totalCount() )
    #
    #     logging.info('len(lst): %s', len(rsp_content.itemDictList())  )
    #     pass
    #
    # def __test_reply_525(self):
    #     reply = svc.get_reply(serviceKey=SVC_KEY, tmX='244148.546388', tmY='412423.75772')
    #     # logging.info('code: %s', rsp.status_code)
    #     # logging.info('hdr : %s', rsp.headers)
    #     # logging.info('cont: %s', rsp.content)
    #     # self.assertEqual(rsp.status_code, 200)
    #
    #     df = reply.df()
    #     self.assertEqual(len(df), 525)



