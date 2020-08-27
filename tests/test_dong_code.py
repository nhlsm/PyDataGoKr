import unittest

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

    def test_0(self):
        # logging.info('dtypes: %s', LAWD_CODE.dtypes)
        # logging.info('key: %s', dong_code.LAWD_CODE )
        pass

    def test_1(self):
        # x = LAWD_CODE.query(' 법정동명.str.contains("서울") and 폐지여부=="존재" ')
        # logging.info('key: %s', x )

        # x = LAWD_CODE.query(' 법정동명.str.contains("인천광역시 미추홀구") and 폐지여부=="존재" ')
        # logging.info('key: %s', x )
        pass

    def test_2(self):
        # x = LAWD_CODE['법정동코드'].str[:5].unique()
        # logging.info('left5\n%s', x )

        # exists = LAWD_CODE.query( '폐지여부=="존재"' )
        # f5 = exists['법정동코드'].str[:5].unique()
        # logging.info('1:%s', len(f5) )
        #
        # x = LAWD_CODE.query( ' 법정동코드.str.slice(2, 5) != "000" and 법정동코드.str.endswith("00000") and 폐지여부=="존재"' )
        # logging.info('2:%s', len(x) )
        # logging.info('2:\n%s', x )

        # x = LAWD_CODE['법정동코드'].str.slice(2,5)
        # logging.info('left5\n%s', x )
        pass

    def test_lawd_01(self):
        class1_o = lawd_01('o')
        # logging.info('[o] class1: %s', len(class1_o) )
        # logging.info('\n%s', class1_o )

        class1_x = lawd_01('x')
        # logging.info('[x] class1: %s', len(class1_x) )
        # logging.info('\n%s', class1_x )

        class1_a = lawd_01('a')
        # logging.info('[a] class1: %s', len(class1_a) )
        # logging.info('\n%s', class1_a )
        self.assertEqual( len(class1_o) + len(class1_x), len(class1_a) )

    def test_lawd_05(self):
        class2_o = lawd_05('o')
        # logging.info('[o] class2: %s', len(class2_o) )
        # logging.info('\n%s', class2_o )

        class2_x = lawd_05('x')
        # logging.info('[x] class2: %s', len(class2_x) )
        # logging.info('\n%s', class2_x )

        class2_a = lawd_05('a')
        # logging.info('[a] class2: %s', len(class2_a) )
        # logging.info('\n%s', class2_a )
        self.assertEqual( len(class2_o) + len(class2_x), len(class2_a) )
