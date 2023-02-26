
from beatport.session import BeatportSession

class My(object):

    def __init__(self, session: object):
        
        self.endpoint = "my"
        self.session: BeatportSession = session
        self.beatport: Beatport = Beatport(endpoint=self.endpoint, session=self.session)
        self.playlists: Playlists = Playlists(endpoint=self.endpoint, session=self.session)
        pass

class Playlists(My):

    def __init__(self, endpoint, session):
        super(My, self).__init__()
        self.session: BeatportSession = session
        self.endpoint =  endpoint + '/playlists/'


    def get(self, playlist_id:int):
    
        content = self.session.make_request(
            method='get',
            endpoint=self.endpoint + "{id}".format(id=playlist_id)
            
        )

        return content

    def get_all(self, page:int, per_page:int):

        params = {
            'page':page,
            'per_page':per_page
            }
    
        content = self.session.make_request(
            method='get',
            endpoint=self.endpoint,
            params=params
            
        )

        return content

    def create_playlist(self, name:str):
        
        params = {'name':name}
    
        content = self.session.make_request(
            method='post',
            endpoint=self.endpoint,
            json=params
            
        )

        return content

    def get_tracks(self, playlist_id:int, page:int, per_page:int):

        params = {
            'page':page,
            'per_page':per_page
            }
    
        content = self.session.make_request(
            method='get',
            endpoint=self.endpoint + "{id}/tracks/".format(id=playlist_id),
            params=params
            
        )

        return content


    def add_tracks(self, playlist_id:int,track_ids:list):

        params = {'track_ids':track_ids}
    
        content = self.session.make_request(
            method='post',
            endpoint=self.endpoint + "{id}/tracks/bulk/".format(id=playlist_id),
            json=params
            
        )

        return content

    def edit_tracks(self, playlist_id:int,items:list):

        params = {'items':items}
    
        content = self.session.make_request(
            method='patch',
            endpoint=self.endpoint + "{id}/tracks/bulk/".format(id=playlist_id),
            json=params
            
        )

        return content

    def delete_tracks(self, playlist_id:int, item_ids:list):

        params = {'item_ids':item_ids}

        content = self.session.make_request(
            method='delete',
            endpoint=self.endpoint + "{id}/tracks/bulk/".format(id=playlist_id),
            json=params
            
        )

        return content


class Beatport(My):

    def __init__(self, endpoint, session):
        self.session: BeatportSession = session
        self.endpoint =  endpoint + '/beatport/'
        self.artists = Artists(endpoint=self.endpoint, session=self.session)
        self.labels = Labels(endpoint=self.endpoint, session=self.session)
        self.tracks = Tracks(endpoint=self.endpoint, session=self.session)

    def get(self, publish_date:str, item_publish_date:str, page:int, per_page:int):

        params = {
            'publish_date':publish_date,
            'item_publish_date':item_publish_date,
            'page':page,
            'per_page':per_page
            }
    
        content = self.session.make_request(
            method='get',
            endpoint=self.endpoint,
            params=params
            
        )

        return content

class Artists(Beatport):

    def __init__(self, endpoint, session):
        self.endpoint =  endpoint + 'artists/'
        self.session: BeatportSession = session

    def get(self, publish_date:str=None, item_publish_date:str=None, page:int=None, per_page:int=None):

        params = {
            'publish_date':publish_date,
            'item_publish_date':item_publish_date,
            'page':page,
            'per_page':per_page
            }
    
        content = self.session.make_request(
            method='get',
            endpoint=self.endpoint,
            params=params
            
        )

        return content

class Labels(Beatport):

    def __init__(self, endpoint, session):
        self.endpoint =  endpoint + 'artists/'
        self.session: BeatportSession = session

    def get(self, publish_date:str, item_publish_date:str, page:int, per_page:int):

        params = {
            'publish_date':publish_date,
            'item_publish_date':item_publish_date,
            'page':page,
            'per_page':per_page
            }
    
        content = self.session.make_request(
            method='get',
            endpoint=self.endpoint,
            params=params
            
        )

        return content

class Tracks(Beatport):

    def __init__(self, endpoint, session):
        self.endpoint =  endpoint + 'tracks/'
        self.session: BeatportSession = session

    def get(self, publish_date:str=None, item_publish_date:str=None, page:int=None, per_page:int=None, order_by:str="-publish_date"):

        params = {
            'publish_date':publish_date,
            'item_publish_date':item_publish_date,
            'page':page,
            'per_page':per_page,
            'order_by':order_by
            }
    
        content = self.session.make_request(
            method='get',
            endpoint=self.endpoint,
            params=params
            
        )

        return content

