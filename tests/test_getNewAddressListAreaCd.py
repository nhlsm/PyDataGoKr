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

        self.assertEqual(rsp.status_code, 200)
        self.assertEqual(rsp_content['NewAddressListResponse']['cmmMsgHeader']['successYN'], 'Y')
        self.assertEqual(rsp_content['NewAddressListResponse']['cmmMsgHeader']['totalCount'], '2')

        CNT = 2
        self.assertEqual(rsp_content.totalCount(), CNT)
        self.assertEqual(len(rsp_content.itemDictList()), CNT)
        self.assertEqual(len(rsp_content.itemDataFrame()), CNT)

        ##################################
        reply = svc.get_reply(serviceKey=SVC_KEY, searchSe='road', srchwrd='세종로 17')
        self.assertEqual(reply.rsp().status_code, 200)
        self.assertEqual( reply.rsp_content().totalCount(), CNT )
        self.assertEqual( len( reply.df() ), CNT )

    def test_road_1(self):
        rsp = svc.get_rsp(serviceKey=SVC_KEY, searchSe='road', srchwrd='세종로')
        # logging.info('code: %s', rsp.status_code)
        # logging.info('hdr : %s', rsp.headers)
        # logging.info('cont: %s', rsp.content)

        rsp_content = svc.RspContent.fromRsp(rsp)
        # logging.info('\n%s', pprint.pformat(rsp_content))

        self.assertEqual(rsp.status_code, 200)
        self.assertEqual(rsp_content['NewAddressListResponse']['cmmMsgHeader']['successYN'], 'Y')
        self.assertEqual(rsp_content['NewAddressListResponse']['cmmMsgHeader']['totalCount'], None)

        CNT = 0
        self.assertEqual(rsp_content.totalCount(), CNT)
        self.assertEqual(len(rsp_content.itemDictList()), CNT)
        self.assertEqual(len(rsp_content.itemDataFrame()), CNT)


    def test_dong(self):
        rsp = svc.get_rsp(serviceKey=SVC_KEY, searchSe='dong', srchwrd='홍문동 111-15')
        # logging.info('code: %s', rsp.status_code)
        # logging.info('hdr : %s', rsp.headers)
        # logging.info('cont: %s', rsp.content)

        # rsp_content = svc.RspContent(xmltodict.parse(rsp.content))
        rsp_content = svc.RspContent.fromRsp(rsp)
        # logging.info('\n%s', pprint.pformat(rsp_content))

        self.assertEqual(rsp.status_code, 200)
        self.assertEqual(rsp_content['NewAddressListResponse']['cmmMsgHeader']['successYN'], 'Y')
        self.assertEqual(rsp_content['NewAddressListResponse']['cmmMsgHeader']['totalCount'], '1')

        CNT = 1
        self.assertEqual(rsp_content.totalCount(), CNT)
        self.assertEqual(len(rsp_content.itemDictList()), CNT)
        self.assertEqual(len(rsp_content.itemDataFrame()), CNT)


    def test_post(self):
        rsp = svc.get_rsp(serviceKey=SVC_KEY, searchSe='post', srchwrd='12621', countPerPage = 20)
        # logging.info('code: %s', rsp.status_code)
        # logging.info('hdr : %s', rsp.headers)
        # logging.info('cont: %s', rsp.content)

        # rsp_content = svc.RspContent(xmltodict.parse(rsp.content))
        rsp_content = svc.RspContent.fromRsp(rsp)
        # logging.info('\n%s', pprint.pformat(rsp_content))

        self.assertEqual(rsp.status_code, 200)
        self.assertEqual(rsp_content['NewAddressListResponse']['cmmMsgHeader']['successYN'], 'Y')
        self.assertEqual(rsp_content['NewAddressListResponse']['cmmMsgHeader']['totalCount'], '168')

        CNT = 168
        self.assertEqual(rsp_content.totalCount(), CNT)

        COUNT_PER_PAGE = 20
        self.assertEqual(len(rsp_content.itemDictList()), COUNT_PER_PAGE)
        self.assertEqual(len(rsp_content.itemDataFrame()), COUNT_PER_PAGE)

    def test_get_df_road_0(self):
        reply = svc.get_reply(serviceKey=SVC_KEY, searchSe='road', srchwrd='세종로 17')
        self.assertEqual(len(reply.df()), 2)
        # print(df)

    def test_get_df_road_1(self):
        reply = svc.get_reply(serviceKey=SVC_KEY, searchSe='road', srchwrd='세종로')
        # logging.info('key: %s', len(reply.df()))

        self.assertEqual(len(reply.df()), 0)

    def test_get_df_dong(self):
        reply = svc.get_reply(serviceKey=SVC_KEY, searchSe='dong', srchwrd='홍문동 111-15')
        # logging.info('key: %s', len(reply.df()) )

        self.assertEqual(len(reply.df()), 1)

    def test_get_df_post(self):
        reply = svc.get_reply(serviceKey=SVC_KEY, searchSe='post', srchwrd='12621')
        # logging.info('key: %s', len(reply.df()) )

        self.assertEqual(len(reply.df()), 168)
