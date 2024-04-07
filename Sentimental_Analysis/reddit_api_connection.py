from dotenv import load_dotenv
import requests
import os


# Function to connect to the Reddit API
def connection():
    load_dotenv()
    CLIENT_ID = os.getenv('CLIENT_ID')
    API_KEY = os.getenv('SECRET_KEY')
    REDDIT_USERNAME = os.getenv('REDDIT_USERNAME')
    REDDIT_PASSWORD = os.getenv('REDDIT_PASSWORD')

    auth = requests.auth.HTTPBasicAuth(CLIENT_ID, API_KEY)

    data = {
        'grant_type': 'password',
        'username':REDDIT_USERNAME,
        'password':REDDIT_PASSWORD
    }

    headers = {'User-Agent': 'MyAPI/0.0.1'}
    
    res = requests.post('https://www.reddit.com/api/v1/access_token',
                        auth=auth,
                        data=data,
                        headers=headers)
    

    TOKEN = res.json()['access_token']

    headers['Authorization'] = f'bearer {TOKEN}'

    return headers
    








