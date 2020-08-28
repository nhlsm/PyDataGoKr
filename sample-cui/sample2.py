import os
import types

import pandas as pd

import data_go_kr as dgk

def category_from_url(url:str) -> str:
    return os.path.basename( os.path.dirname(url) )

for k,v in dgk.api.__dict__.items():
    if isinstance(v, types.ModuleType):
        print(k,v)

lst_name = []
lst_desc = []
lst_url = []
lst_cat = []
lst_flag = []
for k,v in dgk.api.__dict__.items():
    if isinstance(v, types.ModuleType):
        print(k)
        print('  ', v.SVC_DESC)
        print('  ', v.SVC_URL)
        print('  ', category_from_url(v.SVC_URL) )
        lst_name.append(k)
        lst_desc.append(v.SVC_DESC)
        lst_url.append(v.SVC_URL)
        lst_cat.append(category_from_url(v.SVC_URL) )
        lst_flag.append(v.SVC_FLAG)
        # print(k)
        # print(k)

df = pd.DataFrame( {
    'cat': lst_cat,
    'name' : lst_name,
    'desc' : lst_desc,
    'url' : lst_url,
    'flag' : lst_flag
})

# df = df.sort_values(by=['cat', 'name'] )
# df = df.sort_values(by=['url', 'name'] )
# df.style.set_properties(**{'text-align': 'left'})
# df.style.set_properties(**{'text-align': 'left'}).set_table_styles([ dict(selector='th', props=[('text-align', 'left')] ) ])
pd.set_option('display.colheader_justify', 'left')
pd.set_option('display.max_columns', 100)
pd.set_option('display.width', 10000)
pd.set_option('max_colwidth', -1)
# pd.set_option('display.expand_frame_repr', False)
print(df[['cat', 'name', 'flag', 'desc' ]])
# print(df)

