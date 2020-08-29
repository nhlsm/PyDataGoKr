import typing
from collections import OrderedDict

import pandas as pd

class RspContentBase(OrderedDict):

    def resultCode(self) -> int:
        try:
            return int(self['response']['header']['resultCode'])
        except Exception as e:
            return -1

    def resultMsg(self) -> str:
        try:
            return self['response']['header']['resultMsg']
        except Exception as e:
            return '__UNKNOWN'

    def numOfRows(self) -> int:
        try:
            return int(self['response']['body']['numOfRows'])
        except Exception as e:
            return -1

    def pageNo(self) -> int:
        try:
            return int(self['response']['body']['pageNo'])
        except Exception as e:
            return -1

    def totalCount(self) -> int:
        try:
            return int(self['response']['body']['totalCount'])
        except Exception as e:
            # logging.exception(e)
            return 0

    def itemDictList(self) -> typing.List[OrderedDict]:
        cnt = self.totalCount()
        # normalize
        try:
            lst = self['response']['body']['items']['item']
            # logging.info('type(lst): %s', type(lst) )
            if lst is None:
                return []
            elif isinstance(lst, list):
                return lst[:cnt]    # work around
            else:
                return [lst]
        except Exception as e:
            # logging.exception(e)
            return []

    def itemDataFrame(self) -> pd.DataFrame:
        return pd.DataFrame(self.itemDictList())



