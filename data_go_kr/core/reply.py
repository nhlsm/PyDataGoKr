import typing
from collections import OrderedDict

import requests
import pandas as pd

class Reply:
    def __init__(self, rsp:requests.models.Response = None, rsp_content : OrderedDict = None, df : pd.DataFrame = None):
        self.m_rsp: requests.models.Response = rsp
        self.m_rsp_content: OrderedDict = rsp_content
        self.m_df: pd.DataFrame = df

    def rsp(self):
        return self.m_rsp

    def rsp_content(self):
        return self.m_rsp_content

    def df(self):
        return self.m_df