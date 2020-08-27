import logging
import sys
import unittest

import data_go_kr
from data_go_kr import getNewAddressListAreaCd as svc

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

    def test_road_0(self):
        '''
        OrderedDict([('NewAddressListResponse',
              OrderedDict([('cmmMsgHeader',
                            OrderedDict([('requestMsgId', None),
                                         ('responseMsgId', None),
                                         ('responseTime', '20200825:011757807'),
                                         ('successYN', 'Y'),
                                         ('returnCode', '00'),
                                         ('errMsg', None),
                                         ('totalCount', '2'),
                                         ('countPerPage', '10'),
                                         ('totalPage', '1'),
                                         ('currentPage', '1')])),
                           ('newAddressListAreaCd',
                            [OrderedDict([('zipNo', '12621'),
                                          ('lnmAdres', '경기도 여주시 세종로 17 (홍문동)'),
                                          ('rnAdres', '경기도 여주시 홍문동 111-15')]),
                             OrderedDict([('zipNo', '12621'),
                                          ('lnmAdres',
                                           '경기도 여주시 세종로 17-1 (홍문동)'),
                                          ('rnAdres',
                                           '경기도 여주시 홍문동 111-2')])])]))])
        :return:
        '''
        rsp = svc.req(serviceKey=SVC_KEY, searchSe='road', srchwrd='세종로 17')
        # logging.info('code: %s', rsp.status_code)
        # logging.info('hdr : %s', rsp.headers)
        # logging.info('cont: %s', rsp.content)

        # rsp_dict = svc.RspDict(xmltodict.parse(rsp.content))
        rsp_dict = svc.RspDict.fromRsp(rsp)
        # logging.info('\n%s', pprint.pformat(rsp_dict))
        # logging.info('result: %s', rsp_dict.result())

        self.assertEqual(rsp.status_code, 200)
        self.assertEqual(rsp_dict['NewAddressListResponse']['cmmMsgHeader']['successYN'], 'Y')
        self.assertEqual(rsp_dict['NewAddressListResponse']['cmmMsgHeader']['totalCount'], '2')

        self.assertEqual(rsp_dict.totalCount(), 2)
        self.assertEqual(len(rsp_dict.itemDictList()), 2)
        self.assertEqual(len(rsp_dict.itemDataFrame()), 2)

    def test_road_1(self):
        rsp = svc.req(serviceKey=SVC_KEY, searchSe='road', srchwrd='세종로')
        # logging.info('code: %s', rsp.status_code)
        # logging.info('hdr : %s', rsp.headers)
        # logging.info('cont: %s', rsp.content)

        # rsp_dict = svc.RspDict(xmltodict.parse(rsp.content))
        rsp_dict = svc.RspDict.fromRsp(rsp)
        # logging.info('\n%s', pprint.pformat(rsp_dict))

        self.assertEqual(rsp.status_code, 200)
        self.assertEqual(rsp_dict['NewAddressListResponse']['cmmMsgHeader']['successYN'], 'Y')
        self.assertEqual(rsp_dict['NewAddressListResponse']['cmmMsgHeader']['totalCount'], None)

        self.assertEqual(rsp_dict.totalCount(), 0)
        self.assertEqual(len(rsp_dict.itemDictList()), 0)
        self.assertEqual(len(rsp_dict.itemDataFrame()), 0)


    def test_dong(self):
        rsp = svc.req(serviceKey=SVC_KEY, searchSe='dong', srchwrd='홍문동 111-15')
        # logging.info('code: %s', rsp.status_code)
        # logging.info('hdr : %s', rsp.headers)
        # logging.info('cont: %s', rsp.content)

        # rsp_dict = svc.RspDict(xmltodict.parse(rsp.content))
        rsp_dict = svc.RspDict.fromRsp(rsp)
        # logging.info('\n%s', pprint.pformat(rsp_dict))

        self.assertEqual(rsp.status_code, 200)
        self.assertEqual(rsp_dict['NewAddressListResponse']['cmmMsgHeader']['successYN'], 'Y')
        self.assertEqual(rsp_dict['NewAddressListResponse']['cmmMsgHeader']['totalCount'], '1')

        self.assertEqual(rsp_dict.totalCount(), 1)
        self.assertEqual(len(rsp_dict.itemDictList()), 1)
        self.assertEqual(len(rsp_dict.itemDataFrame()), 1)


    def test_post(self):
        rsp = svc.req(serviceKey=SVC_KEY, searchSe='post', srchwrd='12621')
        # logging.info('code: %s', rsp.status_code)
        # logging.info('hdr : %s', rsp.headers)
        # logging.info('cont: %s', rsp.content)

        # rsp_dict = svc.RspDict(xmltodict.parse(rsp.content))
        rsp_dict = svc.RspDict.fromRsp(rsp)
        # logging.info('\n%s', pprint.pformat(rsp_dict))

        self.assertEqual(rsp.status_code, 200)
        self.assertEqual(rsp_dict['NewAddressListResponse']['cmmMsgHeader']['successYN'], 'Y')
        self.assertEqual(rsp_dict['NewAddressListResponse']['cmmMsgHeader']['totalCount'], '168')

        self.assertEqual(rsp_dict.totalCount(), 168)
        # self.assertEqual(len(rsp_dict.itemDictList()), 168)
        # self.assertEqual(len(rsp_dict.itemDataFrame()), 168)

    def test_get_df_road_0(self):
        hdr, df = svc.get_df(serviceKey=SVC_KEY, searchSe='road', srchwrd='세종로 17')
        self.assertEqual(len(df), 2)
        # print(df)

    def test_get_df_road_1(self):
        hdr, df = svc.get_df(serviceKey=SVC_KEY, searchSe='road', srchwrd='세종로')
        # logging.info('key: %s', len(df))

        self.assertEqual(len(df), 0)

    def test_get_df_dong(self):
        hdr, df = svc.get_df(serviceKey=SVC_KEY, searchSe='dong', srchwrd='홍문동 111-15')
        # logging.info('key: %s', len(df) )

        self.assertEqual(len(df), 1)

    def test_get_df_post(self):
        hdr, df = svc.get_df(serviceKey=SVC_KEY, searchSe='post', srchwrd='12621')
        # logging.info('key: %s', len(df) )

        self.assertEqual(len(df), 168)
