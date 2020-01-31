import time

import pandas as pd
import requests

import poster
import Credentials as c


url = 'https://api.stackexchange.com/2.2/questions/no-answers?order=desc&sort=creation&tagged=git&filter=!9Z(-wwYGT&&site=stackoverflow&team=stackoverflow.com/c/ncsu&key=' + c.secret['key']
headers = {
    'X-API-Access-Token': c.secret['AccessToken'],
    'Accept-Charset'    :'UTF-8'
}


async def question_Extractor():
    res = requests.get(url, headers=headers)
    print(res)

    data = res.json()
    print("0:\t")
    print(data)
    # print(data)
    cur_time = time.time()
    df = pd.DataFrame.from_dict(data['items'], orient='columns')
    df.index.name = 'id'
    # df['tags_string'] = [','.join(map(str, l)) for l in df['tags']]
    # df_filtered = df[df['tags_string'].str.contains('git')]
    # print(df_filtered)
    # df_filtered = df[cur_time - df['creation_date'] < 129600]
    df_filtered = df
    print(df_filtered)
    q_stream_builder = []
    q_stream = []
    for idx in df_filtered.index:
        q_stream_builder.append(df_filtered['question_id'][idx])
        q_stream_builder.append(df_filtered['title'][idx])
        q_stream_builder.append(df_filtered['body'][idx])
        q_stream_builder.append(df_filtered['owner'][idx]['display_name'])
        print(q_stream_builder[3])
        q_stream.append(q_stream_builder.copy())
        print("1:\t")
        print(q_stream)
        q_stream_builder.clear()

    print("2:\t")
    print(q_stream)
    return q_stream