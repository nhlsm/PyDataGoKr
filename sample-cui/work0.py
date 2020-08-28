import os
import sys
import logging

import data_go_kr as dgk

SVC_KEY = dgk.test_svc_key() # fix it to your SVC_KEY

def test_0():
    # 새주소 5자리 우편번호 조회서비스. ( 도로명 주소 )
    rsp = dgk.getNewAddressListAreaCd.get_rsp(serviceKey=SVC_KEY, searchSe='road', srchwrd='세종로 17')
    logging.info('key: %s', rsp )

    reply = dgk.getNewAddressListAreaCd.get_reply(serviceKey=SVC_KEY, searchSe='road', srchwrd='세종로 17')
    logging.info('key: %s', reply )
    logging.info('\n%s', reply.df())

if __name__ == '__main__':
    # debug
    LOG_FORMAT = '%(pathname)s:%(lineno)03d - %(message)s'
    LOG_LEVEL = logging.INFO  # DEBUG(10), INFO(20), (0~50)

    # release
    #LOG_FORMAT = '%(message)s'
    # LOG_LEVEL = logging.INFO  # DEBUG(10), INFO(20), (0~50)

    logging.basicConfig(format=LOG_FORMAT, level=LOG_LEVEL, stream=sys.stdout)
    test_0()



