from reddit_api_connection import connection
import requests
from Structured_NLP import basic_analysis
import pandas as pd


if __name__ == "__main__":
    headers = connection()

    res = requests.get('https://oauth.reddit.com/r/brasil/hot',
                        headers=headers, params = {'limit': 20})


    df_original = pd.DataFrame()

    for post in res.json()['data']['children']:
        dict = {
            'subreddit': post['data']['subreddit'],
            'titulo': post['data']['title'],
            'texto': post['data']['selftext'],
        }
        if len(dict['texto']) > 0:
            df_extended = pd.DataFrame([dict], columns=dict.keys())
            df_original = pd.concat([df_original, df_extended], ignore_index=True)

    for number,row in enumerate(df_original.iterrows()):
        print(f'Post {number}: {row[1]["titulo"]}')
        print(f'Texto: {row[1]["texto"]}')
        basic_analysis(row[1]['texto'])
        print('---------------------------------------------------------------')