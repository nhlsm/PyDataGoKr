import pprint
import logging
import sys
import unittest

import data_go_kr as dgk
from data_go_kr.api import getNewAddressListAreaCd as svc

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
        SVC_KEY = dgk.test_svc_key()

    def test_road_0(self):
        ##################################
        rsp = svc.get_rsp(serviceKey=SVC_KEY, searchSe='road', srchwrd='세종로 17')
        # logging.info('code: %s', rsp.status_code)
        # logging.info('hdr : %s', rsp.headers)
        # logging.info('cont: %s', rsp.content)

        rsp_content = svc.RspContent.fromRsp(rsp)
        # logging.info('\n%s', pprint.pformat(rsp_content))
        # logging.info('result: %s', rsp_content.result())

        self.assertEqual(200, rsp.status_code)
        self.assertEqual('Y', rsp_content['NewAddressListResponse']['cmmMsgHeader']['successYN'])

        CNT = 2
        self.assertEqual(CNT, rsp_content.totalCount())
        self.assertEqual(CNT, len(rsp_content.itemDictList()))
        self.assertEqual(CNT, len(rsp_content.itemDataFrame()))

        ##################################
        reply = svc.get_reply(serviceKey=SVC_KEY, searchSe='road', srchwrd='세종로 17')
        self.assertEqual( 200, reply.rsp().status_code)
        self.assertEqual( CNT, reply.rsp_content().totalCount() )
        self.assertEqual( CNT, len( reply.df() ) )

    def test_road_1(self):
        rsp = svc.get_rsp(serviceKey=SVC_KEY, searchSe='road', srchwrd='세종로')
        # logging.info('code: %s', rsp.status_code)
        # logging.info('hdr : %s', rsp.headers)
        # logging.info('cont: %s', rsp.content)

        rsp_content = svc.RspContent.fromRsp(rsp)
        # logging.info('\n%s', pprint.pformat(rsp_content))

        self.assertEqual(200, rsp.status_code)
        self.assertEqual('Y', rsp_content['NewAddressListResponse']['cmmMsgHeader']['successYN'])

        CNT = 0
        self.assertEqual(CNT, rsp_content.totalCount())
        self.assertEqual(CNT, len(rsp_content.itemDictList()))
        self.assertEqual(CNT, len(rsp_content.itemDataFrame()))


    def test_dong(self):
        rsp = svc.get_rsp(serviceKey=SVC_KEY, searchSe='dong', srchwrd='홍문동 111-15')
        # logging.info('code: %s', rsp.status_code)
        # logging.info('hdr : %s', rsp.headers)
        # logging.info('cont: %s', rsp.content)

        # rsp_content = svc.RspContent(xmltodict.parse(rsp.content))
        rsp_content = svc.RspContent.fromRsp(rsp)
        # logging.info('\n%s', pprint.pformat(rsp_content))

        self.assertEqual(200, rsp.status_code)
        self.assertEqual('Y', rsp_content['NewAddressListResponse']['cmmMsgHeader']['successYN'])

        CNT = 1
        self.assertEqual(CNT, rsp_content.totalCount())
        self.assertEqual(CNT, len(rsp_content.itemDictList()))
        self.assertEqual(CNT, len(rsp_content.itemDataFrame()))


    def test_post(self):
        rsp = svc.get_rsp(serviceKey=SVC_KEY, searchSe='post', srchwrd='12621', countPerPage = 20)
        # logging.info('code: %s', rsp.status_code)
        # logging.info('hdr : %s', rsp.headers)
        # logging.info('cont: %s', rsp.content)

        # rsp_content = svc.RspContent(xmltodict.parse(rsp.content))
        rsp_content = svc.RspContent.fromRsp(rsp)
        # logging.info('\n%s', pprint.pformat(rsp_content))

        self.assertEqual(200, rsp.status_code)
        self.assertEqual('Y', rsp_content['NewAddressListResponse']['cmmMsgHeader']['successYN'])

        CNT = 168
        self.assertEqual(CNT, rsp_content.totalCount())

        COUNT_PER_PAGE = 20
        self.assertEqual(COUNT_PER_PAGE, len(rsp_content.itemDictList()))
        self.assertEqual(COUNT_PER_PAGE, len(rsp_content.itemDataFrame()))

    def test_get_df_road_0(self):
        reply = svc.get_reply(serviceKey=SVC_KEY, searchSe='road', srchwrd='세종로 17')
        self.assertEqual(2, len(reply.df()))
        # print(df)

    def test_get_df_road_1(self):
        reply = svc.get_reply(serviceKey=SVC_KEY, searchSe='road', srchwrd='세종로')
        # logging.info('key: %s', len(reply.df()))

        self.assertEqual(0, len(reply.df()))

    def test_get_df_dong(self):
        reply = svc.get_reply(serviceKey=SVC_KEY, searchSe='dong', srchwrd='홍문동 111-15')
        # logging.info('key: %s', len(reply.df()) )

        self.assertEqual(1, len(reply.df()))

    def test_get_df_post(self):
        reply = svc.get_reply(serviceKey=SVC_KEY, searchSe='post', srchwrd='12621')
        # logging.info('key: %s', len(reply.df()) )

        self.assertEqual(168, len(reply.df()))
