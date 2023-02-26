import json
from datetime import datetime, timedelta
import json
import os
import requests
from beatport.auxiliary import Auxiliary
from beatport.catalog import Catalog
from beatport.session import BeatportSession
from beatport.my import My



class BeatportClient():

    RESOURCE = 'https://api.beatport.com/'

    AUTH_ENDPOINT = 'auth/o/authorize?/'
    TOKEN_ENDPOINT = 'auth/o/token/'


    def __init__(self):
        """Initializes the Graph Client.
        ### Parameters
        ----
        client_id : str
            The application Client ID assigned when
            creating a new Microsoft App.
        client_secret : str
            The application Client Secret assigned when
            creating a new Microsoft App.
        redirect_uri : str
            The application Redirect URI assigned when
            creating a new Microsoft App.
        scope : List[str]
            The list of scopes you want the application
            to have access to.
        account_type : str, optional
            [description], by default 'common'
        office365 : bool, optional
            [description], by default False
        """

        self.api_version = 'v4'
        self.session = BeatportSession(client=self)
        self.auxiliary = Auxiliary(session=self.session)
        self.catalog = Catalog(session=self.session)
        self.my = My(session=self.session)

       
        
        self.access_token = self.getCreds()['access_token']
        

    def refresh_access_token(self):
        """Used to get new access token.
       
        """

        self.token_json = self.getCreds()

        params = {
                    "grant_type":"refresh_token",
                    "refresh_token":self.token_json['refresh_token'],
                    "client_id":self.token_json['client_id']
                    }
        print("Refreshing access token...")
        url = self.session.build_url(self.TOKEN_ENDPOINT)
        headers = self.session.build_headers()
        content = requests.post(url, headers=headers, data=params).json()

        """content = self.session.make_request(
            method='post',
            endpoint=self.TOKEN_ENDPOINT,
            params=params
            
        )"""
        print(content)

        expires_on  = datetime.now() + timedelta(seconds=content['expires_in'])

        content['expires_on'] = expires_on.strftime('%Y-%m-%d %H:%M:%S')
        content['client_id'] = self.token_json['client_id']

        self.access_token = content['access_token']
        self.setCreds(content)
        return content['access_token']

    def getCreds(self):
        with open(os.environ['TOKENS_PATH'], 'r') as f:
            self.token_json = json.load(f)['beatport']

        return self.token_json

    def setCreds(self, data):
        with open(os.environ['TOKENS_PATH'], 'r') as f:
            __allCreds = json.load(f)

        __allCreds['beatport'] = data
        with open(os.environ['TOKENS_PATH'], 'w') as outfile:
            outfile.write(json.dumps(__allCreds,indent=4,sort_keys=True))
        print("Credentials updated")





    