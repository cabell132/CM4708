
from beatport.session import BeatportSession

class Catalog(object):

    def __init__(self, session: object):
        
        self.endpoint = "catalog"
        self.session: BeatportSession = session
        self.artists: Artists = Artists(endpoint=self.endpoint, session=self.session)
        self.charts: Charts = Charts(endpoint=self.endpoint, session=self.session)
        self.genres: Genres = Genres(endpoint=self.endpoint, session=self.session)
        self.labels: Labels = Labels(endpoint=self.endpoint, session=self.session)
        self.playlists: Playlists = Playlists(endpoint=self.endpoint, session=self.session)
        self.releases: Releases = Releases(endpoint=self.endpoint, session=self.session)
        self.search: Search = Search(endpoint=self.endpoint, session=self.session)
        self.sub_genres: SubGenres = SubGenres(endpoint=self.endpoint, session=self.session)
        self.tracks: Tracks = Tracks(endpoint=self.endpoint, session=self.session)
        pass

class Artists(Catalog):

    def __init__(self, endpoint, session):
        super(Catalog, self).__init__()
        self.session: BeatportSession = session
        self.endpoint =  endpoint + '/artists/'


    def search(self, name: str = None, name_exact: str = None,
                     created: str = None, updated: str = None,
                     id: int = None, enabled: bool = None,
                     page: int=None, per_page: int = None):

        """
        
        :param name: Filter name by case-insensitive text containment.
        :type  name: string

        :param name_exact: Filter by name exact match.
        :type  name_exact: string

        :param created: Filter by exact, less/greater than equal and range.
                Supports slice syntax:
                
                `date=1970-01-01` (exact)
                `date=:1971-01-01` (less than equal)
                `date=1970-01-01:` (greater than equal)
                `date=1970-01-01:1971-01-01` (range)
                
        :type  created: string

        :param updated: Filter by exact, less/greater than equal and range.
                Supports slice syntax:
                
                `date=1970-01-01` (exact)
                `date=:1971-01-01` (less than equal)
                `date=1970-01-01:` (greater than equal)
                `date=1970-01-01:1971-01-01` (range)
                
        :type  updated: string

        :param id: Filter by artist id exact match.
                Supports `OR` lookup:
                
                `param=value1,value2`
                
        :type  id: int

        :param enabled: Filter by enabled.
        :type  enabled: bool

        """

        params = {
                  'name':name,
                  'name_exact':name_exact,
                  'created':created,
                  'updated':updated,
                  'id':id,
                  'enabled':enabled,
                  'page':page,
                  'per_page':per_page,
                    }

    

        content = self.session.make_request(
            method='get',
            endpoint=self.endpoint ,
            params=params,
            
        )

        return content

    def get(self, artist_id:int, enabled: bool = None,
            page: int=None, per_page: int = None):

        """:param artist_id: Filter by artist id exact match.
                Supports `OR` lookup:
                
                `param=value1,value2`
                
        :type  artist_id: int"""

        params = {'enabled':enabled,
                  'page':page,
                  'per_page':per_page}

    
        content = self.session.make_request(
            method='get',
            endpoint=self.endpoint + "{id}".format(id=artist_id),
            params = params
            
        )

        return content

    def get_images(self, artist_id:int):

        """
        Returns Artist's Images
        
        :param artist_id: Filter by artist id exact match.
                    Supports `OR` lookup:
                
                    `param=value1,value2`
                
        :type  artist_id: int"""

    
        content = self.session.make_request(
            method='get',
            endpoint=self.endpoint + "{id}/images".format(id=artist_id)
            
        )

        return content

    def top_tracks(self, artist_id:int, num:int, enabled: bool = None,
                   page: int=None, per_page: int = None):

        """
        Returns top num tracks for artist by most popular rank
        
        :param artist_id: Filter by artist id exact match.
                    Supports `OR` lookup:
                
                    `param=value1,value2`
                
        :type  artist_id: int
        
        :param num: limited between 1 and 100
                
        :type  num: int"""

        params = {'enabled':enabled,
                  'page':page,
                  'per_page':per_page}

    
        content = self.session.make_request(
            method='get',
            endpoint=self.endpoint + "{id}/top/{num}".format(id=artist_id,
                                                             num=num),
            params=params
            
            
        )

        return content

    def tracks(self, artist_id:int, enabled: bool = None,
               page: int=None, per_page: int = None):

        """
        Returns artist's tracks
        
        :param artist_id: Filter by artist id exact match.
                    Supports `OR` lookup:
                
                    `param=value1,value2`
                
        :type  artist_id: int
        """

        params = {'enabled':enabled,
                  'page':page,
                  'per_page':per_page}

    
        content = self.session.make_request(
            method='get',
            endpoint=self.endpoint + "{id}/tracks/".format(id=artist_id),
            params=params
            
        )

        return content


    def facets(self):

    
        content = self.session.make_request(
            method='get',
            endpoint=self.endpoint + "facets"
            
        )

        return content

class Charts(Catalog):

    def __init__(self, endpoint, session):
        super(Catalog, self).__init__()
        self.session: BeatportSession = session
        self.endpoint =  endpoint + '/charts/'

    def search(self, add_date: str = None, dj_name: str = None,
                     dj_slug: str = None, dj_id: int = None,
                     id: int = None, enabled: bool = None,
                     name: str = None, updated: str = None,
                     created: str = None,
                     genre_name: str = None, genre_id: int = None,
                     sub_genre_name: str = None, sub_genre_id: str = None,
                     is_approved: bool = None, is_published: bool = None,
                     is_indexed: bool = None, user_id: int = None,
                     username: str = None, register_ip_address: str = None,
                     track_id: int = None, publish_date: str = None,
                     is_curated_playlist: bool = None, curated_playlist_genre_id: int = None,
                     page: int=None, per_page: int = None):

        """
        
        """

        params = {
                  'add_date':add_date,
                  'dj_name':dj_name,
                  'dj_slug':dj_slug,
                  'dj_id':dj_id,
                  'genre_name':genre_name,
                  'genre_id':genre_id,
                  'sub_genre_name':sub_genre_name,
                  'sub_genre_id':sub_genre_id,
                  'is_approved':is_approved,
                  'is_published':is_published,
                  'is_indexed':is_indexed,
                  'user_id':user_id,
                  'username':username,
                  'register_ip_address':register_ip_address,
                  'track_id':track_id,
                  'publish_date':publish_date,
                  'is_curated_playlist':is_curated_playlist,
                  'curated_playlist_genre_id':curated_playlist_genre_id,
                  'name':name,
                  'created':created,
                  'updated':updated,
                  'id':id,
                  'enabled':enabled,
                  'page':page,
                  'per_page':per_page,
                    }

    

        content = self.session.make_request(
            method='get',
            endpoint=self.endpoint,
            params=params,
            
        )

        content['topic'] = 'beatport_charts_requests'
        return content

    def facets(self):

    
        content = self.session.make_request(
            method='get',
            endpoint=self.endpoint + "facets"
            
        )

        return content

    def get(self, chart_id:int, enabled: bool = None,
            page: int=None, per_page: int = None):

        """:param chart_id: Filter by chart id exact match.
                Supports `OR` lookup:
                
                `param=value1,value2`
                
        :type  chart_id: int"""

        params = {'enabled':enabled,
                  'page':page,
                  'per_page':per_page}

    
        content = self.session.make_request(
            method='get',
            endpoint=self.endpoint + "{id}".format(id=chart_id),
            params = params
            
        )

        return content

    def get_images(self, chart_id:int, enabled: bool = None,
                   page: int=None, per_page: int = None):

        """
        Returns Charts's Images
        
        :param chart_id: Filter by chart id exact match.
                    Supports `OR` lookup:
                
                    `param=value1,value2`
                
        :type  chart_id: int"""

        params = {'enabled':enabled,
                  'page':page,
                  'per_page':per_page}

    
        content = self.session.make_request(
            method='get',
            endpoint=self.endpoint + "{id}/images".format(id=chart_id),
            params=params
            
        )

        return content

    def get_tracks(self, chart_id:int, enabled: bool = None,
                   page: int=None, per_page: int = None):

        """
        Returns Charts's tracks
        
        :param chart_id: Filter by chart id exact match.
                    Supports `OR` lookup:
                
                    `param=value1,value2`
                
        :type  chart_id: int
        """
        params = {'enabled':enabled,
                  'page':page,
                  'per_page':per_page}

    
        content = self.session.make_request(
            method='get',
            endpoint=self.endpoint + "{id}/tracks/".format(id=chart_id),
            params=params
            
        )
        content['chart_id'] = chart_id
        content['topic'] = 'beatport_charts_tracks_requests'

        track_no = 1
        for track in content['results']:
            track['track_no'] = track_no
            track_no += 1
        return content

class Genres(Catalog):

    def __init__(self, endpoint, session):
        super(Catalog, self).__init__()
        self.session: BeatportSession = session
        self.endpoint =  endpoint + '/genres/'
    
    def search(self, name: str = None, enabled: bool = None,
                     order_by: int = None,
                     page: int=None, per_page: int = None):

        """
        
        """

        params = {
                  'name':name,
                  'enabled':enabled,
                  'order_by':order_by,
                  'page':page,
                  'per_page':per_page,
                    }

        content = self.session.make_request(
            method='get',
            endpoint=self.endpoint,
            params=params,
            
        )

        return content

    def facets(self):

    
        content = self.session.make_request(
            method='get',
            endpoint=self.endpoint + "facets"
            
        )

        return content

    def get_all(self):
        
        params = {'page':1,
                  'per_page':150}
   
        content = self.session.make_request(
            method='get',
            endpoint=self.endpoint ,
            params=params
            
        )

        return content

    def get(self, genre_id:int, enabled: bool = None,
            page: int=None, per_page: int = None):

        """:param genre_id: Filter by genre id exact match.
                Supports `OR` lookup:
                
                `param=value1,value2`
                
        :type  genre_id: int"""

        params = {'enabled':enabled,
                  'page':page,
                  'per_page':per_page}


    
        content = self.session.make_request(
            method='get',
            endpoint=self.endpoint + "{id}".format(id=genre_id),
            params=params
            
        )

        return content

    def get_subgenres(self, genre_id:int, enabled: bool = None,
                      page: int=None, per_page: int = None):

        """
        Return this genre's sub-genres

        :param genre_id: Filter by genre id exact match.
                Supports `OR` lookup:
                
                `param=value1,value2`
                
        :type  genre_id: int"""

        params = {'enabled':enabled,
                  'page':page,
                  'per_page':per_page}


    
        content = self.session.make_request(
            method='get',
            endpoint=self.endpoint + "{id}/sub-genres/".format(id=genre_id),
            params=params
            
        )

        return content

    def get_top_tracks(self, genre_id:int, num:int, enabled: bool = None,
                       page: int=None, per_page: int = None):

        """
        Returns top num tracks for genre by most popular rank
        
        :param genre_id: Filter by genre id exact match.
                    Supports `OR` lookup:
                
                    `param=value1,value2`
                
        :type  genre_id: int
        
        :param num: limited between 1 and 100
                
        :type  num: int"""

        params = {'enabled':enabled,
                  'page':page,
                  'per_page':per_page}


    
        content = self.session.make_request(
            method='get',
            endpoint=self.endpoint + "{id}/top/{num}".format(id=genre_id,
                                                             num=num),
            params=params
            
        )

        return content

    def get_tracks(self, genre_id:int, enabled: bool = None,
                   page: int=None, per_page: int = None):

        """
        Returns genre's tracks
        
        :param genre_id: Filter by artist id exact match.
                    Supports `OR` lookup:
                
                    `param=value1,value2`
                
        :type  genre_id: int
        """

        params = {'enabled':enabled,
                  'page':page,
                  'per_page':per_page}

    
        content = self.session.make_request(
            method='get',
            endpoint=self.endpoint + "{id}/tracks/".format(id=genre_id),
            params=params
            
        )

        return content

class Labels(Catalog):

    def __init__(self, endpoint, session):
        super(Catalog, self).__init__()
        self.session: BeatportSession = session
        self.endpoint =  endpoint + '/labels/'

    def search(self, created : str = None, default_pre_order_weeks : str = None, enabled : str = None, 
                hype_active : str = None, hype_eligible : str = None, hype_trial_start_date : str = None, 
                hype_trial_end_date : str = None, id : str = None, is_available_for_hype : str = None, 
                is_available_for_pre_order : str = None, is_available_for_streaming : str = None, 
                label_manager : str = None, name_exact : str = None, name : str = None, 
                supplier_name : str = None, supplier_id : int = None, updated : str = None):
        """
        
        :param created: 	Filter on exact, less/greater than equal and range.
                            Supports slice syntax:
                            `date=1970-01-01` (exact)
                            `date=:1971-01-01` (less than equal)
                            `date=1970-01-01:` (greater than equal)
                            `date=1970-01-01:1971-01-01` (range)
            
        :type  created: 

        :param default_pre_order_weeks: 	Filter by Default Pre-Order Weeks exact match.
                                            Supports `OR` lookup:
                                            `param=value1,value2`
            
        :type  default_pre_order_weeks:     

        :param enabled: 	Filter by enabled boolean match.
        :type  enabled:     bool

        :param hype_active: 	Filter on active enrollment in Hype.
        :type  hype_active: 

        :param hype_eligible: 	Filter on Hype eligibility.
        :type  hype_eligible: 

        :param hype_trial_start_date: 	Filter on exact, less/greater than equal and range.
                                        Supports slice syntax:
                                        `date=1970-01-01` (exact)
                                        `date=:1971-01-01` (less than equal)
                                        `date=1970-01-01:` (greater than equal)
                                        `date=1970-01-01:1971-01-01` (range)
            
        :type  hype_trial_start_date: 

        :param hype_trial_end_date: 	Filter on exact, less/greater than equal and range.
                                        Supports slice syntax:
                                        `date=1970-01-01` (exact)
                                        `date=:1971-01-01` (less than equal)
                                        `date=1970-01-01:` (greater than equal)
                                        `date=1970-01-01:1971-01-01` (range)
            
        :type  hype_trial_end_date: 

        :param id: 	Filter by ID exact match.
                    Supports `OR` lookup:
                    `param=value1,value2`
            
        :type  id: 

        :param is_available_for_hype: 	Filter by Is Available for Hype exact match.
        :type  is_available_for_hype: 

        :param is_available_for_pre_order: 	Filter by Is Available for Pre-Order exact match.
        :type  is_available_for_pre_order: 

        :param is_available_for_streaming: 	Filter by Is Available for Streaming exact match.
        :type  is_available_for_streaming: 

        :param label_manager: 	Filter by case-insensitive Label Manager name containment.
        :type  label_manager: 

        :param name_exact: 	Filter by exact label name.
        :type  name_exact: 

        :param name: 	Filter by case-insensitive name containment.
                        Supports `OR` lookup:
                        `param=value1,value2`
            
        :type  name: 

        :param supplier_name: 	Filter by case-insensitive supplier name containment.
                    Supports `OR` lookup:
                    `param=value1,value2`
            
        :type  supplier_name: 

        :param supplier_id: 	Filter by exact supplier ID.
                    Supports `OR` lookup:
                    `param=value1,value2`
            
        :type  supplier_id: 

        :param updated: 	Filter on exact, less/greater than equal and range.
                    Supports slice syntax:
                    `date=1970-01-01` (exact)
                    `date=:1971-01-01` (less than equal)
                    `date=1970-01-01:` (greater than equal)
                    `date=1970-01-01:1971-01-01` (range)
            
        :type  updated: 



        """

        params = {

            "created" : created, "default_pre_order_weeks" : default_pre_order_weeks, "enabled" : enabled, 
            "hype_active" : hype_active, "hype_eligible" : hype_eligible, "hype_trial_start_date" : hype_trial_start_date, 
            "hype_trial_end_date" : hype_trial_end_date, "id" : id, "is_available_for_hype" : is_available_for_hype, 
            "is_available_for_pre_order" : is_available_for_pre_order, "is_available_for_streaming" : is_available_for_streaming, 
            "label_manager" : label_manager, "name_exact" : name_exact, "name" : name, "supplier_name" : supplier_name, 
            "supplier_id" : supplier_id, "updated" : updated, 
        }

        content = self.session.make_request(
            method='get',
            endpoint=self.endpoint,
            params = params
            
        )

        return content

    def get(self, label_id:int, enabled: bool = None,
            page: int=None, per_page: int = None):

        """:param label_id: Filter by label id exact match.
                Supports `OR` lookup:
                
                `param=value1,value2`
                
        :type  label_id: int"""

    
        content = self.session.make_request(
            method='get',
            endpoint=self.endpoint + "{id}".format(id=label_id)
            
        )

        return content

    def get_download(self, label_id:int, enabled: bool = None,
                     page: int=None, per_page: int = None):

        """:param label_id: Filter by label id exact match.
                Supports `OR` lookup:
                
                `param=value1,value2`
                
        :type  label_id: int"""

    
        content = self.session.make_request(
            method='get',
            endpoint=self.endpoint + "{id}/download".format(id=label_id)
            
        )

        return content

    def get_images(self, label_id:int, enabled: bool = None,
                   page: int=None, per_page: int = None):

        """:param label_id: Filter by label id exact match.
                Supports `OR` lookup:
                
                `param=value1,value2`
                
        :type  label_id: int"""

    
        content = self.session.make_request(
            method='get',
            endpoint=self.endpoint + "{id}/images".format(id=label_id)
            
        )

        return content

    def get_releases(self, label_id:int, enabled: bool = None,
                     page: int=None, per_page: int = None):

        """:param label_id: Filter by label id exact match.
                Supports `OR` lookup:
                
                `param=value1,value2`
                
        :type  label_id: int"""

    
        content = self.session.make_request(
            method='get',
            endpoint=self.endpoint + "{id}/releases".format(id=label_id)
            
        )

        return content

    def get_top_tracks(self, label_id:int, num:int, enabled: bool = None,
                       page: int=None, per_page: int = None):

        """
        Returns top num tracks for label by most popular rank
        
        :param label_id: Filter by label id exact match.
                    Supports `OR` lookup:
                
                    `param=value1,value2`
                
        :type  label_id: int
        
        :param num: limited between 1 and 100
                
        :type  num: int"""

    
        content = self.session.make_request(
            method='get',
            endpoint=self.endpoint + "{id}/top/{num}".format(id=label_id,
                                                             num=num)
            
        )

        return content

    def facets(self):

    
        content = self.session.make_request(
            method='get',
            endpoint=self.endpoint + "facets"
            
        )

        return content

class Playlists(Catalog):

    def __init__(self, endpoint, session):
        super(Catalog, self).__init__()
        self.session: BeatportSession = session
        self.endpoint =  endpoint + '/playlists/'

    def facets(self):

    
        content = self.session.make_request(
            method='get',
            endpoint=self.endpoint + "facets"
            
        )

        return content

class Releases(Catalog):

    def __init__(self, endpoint, session):
        super(Catalog, self).__init__()
        self.session: BeatportSession = session
        self.endpoint =  endpoint + '/releases/'

    def search(self, artist_name : str = None, artist_id : int = None, catalog_number : str = None, 
                     created : str = None, current_status : int = None, enabled : bool = None, 
                     encoded_date : str = None, exclusive : bool = None, genre_name : str = None, 
                     genre_id : int = None, id : int = None, is_available_for_streaming : bool = None, 
                     label_name : str = None, label_id : int = None, label_enabled : bool = None, 
                     name : str = None, new_release_date : str = None, pre_order_date : str = None, 
                     publish_date : str = None, release_type_id : int = None, sub_genre_id : str = None, 
                     supplier_name : str = None, supplier_id : int = None, track_name : str = None, 
                     track_id : int = None, upc : str = None, updated : str = None, type : str = None, 
                     type_id : int = None, order_by : str = None, page: int = None, per_page: int = None):


        """
        :param artist_name: 	Filter by case-insensitive artist name containment.
                                Supports `OR` lookup:
                                `param=value1,value2`
        :type  artist_name: 

        :param artist_id: 	Filter by exact artist ID match.
                            Supports `OR` lookup:
                            `param=value1,value2`
        :type  artist_id: int

        :param catalog_number: 	Filter by case-insensitive catalog number exact match.
                                Supports `OR` lookup:
                                `param=value1,value2`
        :type  catalog_number: 

        :param created: 	Filter by exact, less/greater than equal and range.
                            Supports slice syntax:
                            `date=1970-01-01` (exact)
                            `date=:1971-01-01` (less than equal)
                            `date=1970-01-01:` (greater than equal)
                            `date=1970-01-01:1971-01-01` (range)
        :type  created: 

        :param current_status: 	Filter on current_status ID exact match.
                                Supports `OR` lookup:
                                `param=value1,value2`
        :type  current_status: 

        :param enabled: 	Filter by enabled boolean match
        :type  enabled:     bool

        :param encoded_date: 	Filter by exact, less/greater than equal and range.
                                Supports slice syntax:
                                `date=1970-01-01` (exact)
                                `date=:1971-01-01` (less than equal)
                                `date=1970-01-01:` (greater than equal)
                                `date=1970-01-01:1971-01-01` (range)
        :type  encoded_date: 

        :param exclusive: 	Filter by exclusive boolean match
        :type  exclusive:   bool

        :param genre_name: 	Filter by case-insensitive genre exact match.
                            Supports `OR` lookup:
                            `param=value1,value2`
        :type  genre_name: 

        :param genre_id: 	Filter by exact genre ID match.
                    Supports `OR` lookup:
                    `param=value1,value2`
        :type  genre_id: int

        :param id: 	Filter by exact ID match.
                    Supports `OR` lookup:
                    `param=value1,value2`
        :type  id: 

        :param is_available_for_streaming: 	Filter on streaming available boolean match
        :type  is_available_for_streaming:  bool

        :param label_name: 	Filter by case-insensitive label name containment.
                            Supports `OR` lookup:
                            `param=value1,value2`
        :type  label_name: 

        :param label_id: 	Filter by exact label ID match.
                            Supports `OR` lookup:
                            `param=value1,value2`
        :type  label_id: int

        :param label_enabled: 	Filter on enabled boolean match
        :type  label_enabled:   bool

        :param name: 	Filter by case-insensitive name containment.
                        Supports `OR` lookup:
                        `param=value1,value2`
        :type  name: 

        :param new_release_date: 	Filter by exact, less/greater than equal and range.
                                    Supports slice syntax:
                                    `date=1970-01-01` (exact)
                                    `date=:1971-01-01` (less than equal)
                                    `date=1970-01-01:` (greater than equal)
                                    `date=1970-01-01:1971-01-01` (range)
        :type  new_release_date: 

        :param pre_order_date: 	Filter by exact, less/greater than equal and range.
                                Supports slice syntax:
                                `date=1970-01-01` (exact)
                                `date=:1971-01-01` (less than equal)
                                `date=1970-01-01:` (greater than equal)
                                `date=1970-01-01:1971-01-01` (range)
        :type  pre_order_date: 

        :param publish_date: 	Filter by exact, less/greater than equal and range.
                                Supports slice syntax:
                                `date=1970-01-01` (exact)
                                `date=:1971-01-01` (less than equal)
                                `date=1970-01-01:` (greater than equal)
                                `date=1970-01-01:1971-01-01` (range)
        :type  publish_date: 

        :param release_type_id: 	Filter by exact type ID match.
                                    Supports `OR` lookup:
                                    `param=value1,value2`
        :type  release_type_id: int

        :param sub_genre_id: 	Filter by exact sub-genre ID match.
                                Supports `OR` lookup:
                                `param=value1,value2`
        :type  sub_genre_id: int

        :param supplier_name: 	Filter by case-insensitive name containment.
                                Supports `OR` lookup:
                                `param=value1,value2`
        :type  supplier_name: 

        :param supplier_id: 	Filter by case-insensitive name containment.
                                Supports `OR` lookup:
                                `param=value1,value2`
        :type  supplier_id: int

        :param track_name: 	Filter by case-insensitive track name containment.
                            Supports `OR` lookup:
                            `param=value1,value2`
        :type  track_name: 

        :param track_id: 	Filter by exact track ID match.
                            Supports `OR` lookup:
                            `param=value1,value2`
        :type  track_id: int

        :param upc: 	Filter by exact ID match.
                        Supports `OR` lookup:
                        `param=value1,value2`
        :type  upc: 

        :param updated: 	Filter by exact, less/greater than equal and range.
                            Supports slice syntax:
                            `date=1970-01-01` (exact)
                            `date=:1971-01-01` (less than equal)
                            `date=1970-01-01:` (greater than equal)
                            `date=1970-01-01:1971-01-01` (range)
        :type  updated: 

        :param type: 	Filter on track type. Either Release, Album or Mix
                        Supports `OR` lookup:
                        `param=value1,value2`
        :type  type: 

        :param type_id: 	Filter on release type id
                            Supports `OR` lookup:
                            `param=value1,value2`
        :type  type_id: int

        :param order_by: 	Order by a field. Choices: publish_date, release_date, label, name, id
                            and status. Use -genre for descending or:type  order_by:
        :type  order_by: 

"""


        params = {
            "artist_name" : artist_name, "artist_id" : artist_id, "catalog_number" : catalog_number, 
            "created" : created, "current_status" : current_status, "enabled" : enabled, 
            "encoded_date" : encoded_date, "exclusive" : exclusive, "genre_name" : genre_name, 
            "genre_id" : genre_id, "id" : id, "is_available_for_streaming" : is_available_for_streaming, 
            "label_name" : label_name, "label_id" : label_id, "label_enabled" : label_enabled, 
            "name" : name, "new_release_date" : new_release_date, "pre_order_date" : pre_order_date, 
            "publish_date" : publish_date, "release_type_id" : release_type_id, "sub_genre_id" : sub_genre_id, 
            "supplier_name" : supplier_name, "supplier_id" : supplier_id, "track_name" : track_name, 
            "track_id" : track_id, "upc" : upc, "updated" : updated,  "type" : type, 
            "type_id" : type_id, "order_by" : order_by, "page":page, "per_page":per_page

        }


        content = self.session.make_request(
            method='get',
            endpoint=self.endpoint,
            params = params
            
        )

        return content

    def similar(self, artist_name : str = None, artist_id : int = None, catalog_number : str = None, 
                     created : str = None, current_status : int = None, enabled : bool = None, 
                     encoded_date : str = None, exclusive : bool = None, genre_name : str = None, 
                     genre_id : int = None, id : int = None, is_available_for_streaming : bool = None, 
                     label_name : str = None, label_id : int = None, label_enabled : bool = None, 
                     name : str = None, new_release_date : str = None, pre_order_date : str = None, 
                     publish_date : str = None, release_type_id : int = None, sub_genre_id : str = None, 
                     supplier_name : str = None, supplier_id : int = None, track_name : str = None, 
                     track_id : int = None, upc : str = None, updated : str = None, type : str = None, 
                     type_id : int = None, order_by : str = None, page: int = None, per_page: int = None):


        """
        :param artist_name: 	Filter by case-insensitive artist name containment.
                                Supports `OR` lookup:
                                `param=value1,value2`
        :type  artist_name: 

        :param artist_id: 	Filter by exact artist ID match.
                            Supports `OR` lookup:
                            `param=value1,value2`
        :type  artist_id: int

        :param catalog_number: 	Filter by case-insensitive catalog number exact match.
                                Supports `OR` lookup:
                                `param=value1,value2`
        :type  catalog_number: 

        :param created: 	Filter by exact, less/greater than equal and range.
                            Supports slice syntax:
                            `date=1970-01-01` (exact)
                            `date=:1971-01-01` (less than equal)
                            `date=1970-01-01:` (greater than equal)
                            `date=1970-01-01:1971-01-01` (range)
        :type  created: 

        :param current_status: 	Filter on current_status ID exact match.
                                Supports `OR` lookup:
                                `param=value1,value2`
        :type  current_status: 

        :param enabled: 	Filter by enabled boolean match
        :type  enabled:     bool

        :param encoded_date: 	Filter by exact, less/greater than equal and range.
                                Supports slice syntax:
                                `date=1970-01-01` (exact)
                                `date=:1971-01-01` (less than equal)
                                `date=1970-01-01:` (greater than equal)
                                `date=1970-01-01:1971-01-01` (range)
        :type  encoded_date: 

        :param exclusive: 	Filter by exclusive boolean match
        :type  exclusive:   bool

        :param genre_name: 	Filter by case-insensitive genre exact match.
                            Supports `OR` lookup:
                            `param=value1,value2`
        :type  genre_name: 

        :param genre_id: 	Filter by exact genre ID match.
                    Supports `OR` lookup:
                    `param=value1,value2`
        :type  genre_id: int

        :param id: 	Filter by exact ID match.
                    Supports `OR` lookup:
                    `param=value1,value2`
        :type  id: 

        :param is_available_for_streaming: 	Filter on streaming available boolean match
        :type  is_available_for_streaming:  bool

        :param label_name: 	Filter by case-insensitive label name containment.
                            Supports `OR` lookup:
                            `param=value1,value2`
        :type  label_name: 

        :param label_id: 	Filter by exact label ID match.
                            Supports `OR` lookup:
                            `param=value1,value2`
        :type  label_id: int

        :param label_enabled: 	Filter on enabled boolean match
        :type  label_enabled:   bool

        :param name: 	Filter by case-insensitive name containment.
                        Supports `OR` lookup:
                        `param=value1,value2`
        :type  name: 

        :param new_release_date: 	Filter by exact, less/greater than equal and range.
                                    Supports slice syntax:
                                    `date=1970-01-01` (exact)
                                    `date=:1971-01-01` (less than equal)
                                    `date=1970-01-01:` (greater than equal)
                                    `date=1970-01-01:1971-01-01` (range)
        :type  new_release_date: 

        :param pre_order_date: 	Filter by exact, less/greater than equal and range.
                                Supports slice syntax:
                                `date=1970-01-01` (exact)
                                `date=:1971-01-01` (less than equal)
                                `date=1970-01-01:` (greater than equal)
                                `date=1970-01-01:1971-01-01` (range)
        :type  pre_order_date: 

        :param publish_date: 	Filter by exact, less/greater than equal and range.
                                Supports slice syntax:
                                `date=1970-01-01` (exact)
                                `date=:1971-01-01` (less than equal)
                                `date=1970-01-01:` (greater than equal)
                                `date=1970-01-01:1971-01-01` (range)
        :type  publish_date: 

        :param release_type_id: 	Filter by exact type ID match.
                                    Supports `OR` lookup:
                                    `param=value1,value2`
        :type  release_type_id: int

        :param sub_genre_id: 	Filter by exact sub-genre ID match.
                                Supports `OR` lookup:
                                `param=value1,value2`
        :type  sub_genre_id: int

        :param supplier_name: 	Filter by case-insensitive name containment.
                                Supports `OR` lookup:
                                `param=value1,value2`
        :type  supplier_name: 

        :param supplier_id: 	Filter by case-insensitive name containment.
                                Supports `OR` lookup:
                                `param=value1,value2`
        :type  supplier_id: int

        :param track_name: 	Filter by case-insensitive track name containment.
                            Supports `OR` lookup:
                            `param=value1,value2`
        :type  track_name: 

        :param track_id: 	Filter by exact track ID match.
                            Supports `OR` lookup:
                            `param=value1,value2`
        :type  track_id: int

        :param upc: 	Filter by exact ID match.
                        Supports `OR` lookup:
                        `param=value1,value2`
        :type  upc: 

        :param updated: 	Filter by exact, less/greater than equal and range.
                            Supports slice syntax:
                            `date=1970-01-01` (exact)
                            `date=:1971-01-01` (less than equal)
                            `date=1970-01-01:` (greater than equal)
                            `date=1970-01-01:1971-01-01` (range)
        :type  updated: 

        :param type: 	Filter on track type. Either Release, Album or Mix
                        Supports `OR` lookup:
                        `param=value1,value2`
        :type  type: 

        :param type_id: 	Filter on release type id
                            Supports `OR` lookup:
                            `param=value1,value2`
        :type  type_id: int

        :param order_by: 	Order by a field. Choices: publish_date, release_date, label, name, id
                            and status. Use -genre for descending or:type  order_by:
        :type  order_by: 

"""


        params = {
            "artist_name" : artist_name, "artist_id" : artist_id, "catalog_number" : catalog_number, 
            "created" : created, "current_status" : current_status, "enabled" : enabled, 
            "encoded_date" : encoded_date, "exclusive" : exclusive, "genre_name" : genre_name, 
            "genre_id" : genre_id, "id" : id, "is_available_for_streaming" : is_available_for_streaming, 
            "label_name" : label_name, "label_id" : label_id, "label_enabled" : label_enabled, 
            "name" : name, "new_release_date" : new_release_date, "pre_order_date" : pre_order_date, 
            "publish_date" : publish_date, "release_type_id" : release_type_id, "sub_genre_id" : sub_genre_id, 
            "supplier_name" : supplier_name, "supplier_id" : supplier_id, "track_name" : track_name, 
            "track_id" : track_id, "upc" : upc, "updated" : updated,  "type" : type, 
            "type_id" : type_id, "order_by" : order_by, "page":page, "per_page":per_page

        }


        content = self.session.make_request(
            method='get',
            endpoint=self.endpoint + '/similar/',
            params = params
            
        )

        return content

    def beatbot(self, id):
        """
        Get a list of releases that are similar to the release with the given id.

        :param id: 	Filter by exact ID match.
                    Supports `OR` lookup:
                    `param=value1,value2`
        :type  int:

        
        """


        content = self.session.make_request(
            method='get',
            endpoint=self.endpoint + '/{}/beatbot/'.format(id)
            
        )

        return content

    def get_top_tracks(self, num:int, enabled: bool = None,
                       page: int=None, per_page: int = None):

        """
        Returns top num tracks most popular rank
        
        :param release_id: Filter by genre id exact match.
                    Supports `OR` lookup:
                
                    `param=value1,value2`
                
        :type  genre_id: int
        
        :param num: limited between 1 and 100
                
        :type  num: int"""

    
        content = self.session.make_request(
            method='get',
            endpoint=self.endpoint + "/top/{num}".format(num=num)
            
        )

        return content

    def facets(self):

    
        content = self.session.make_request(
            method='get',
            endpoint=self.endpoint + "facets"
            
        )

        return content

class Search(Catalog):

    def __init__(self, endpoint, session):
        super(Catalog, self).__init__()
        self.session: BeatportSession = session
        self.endpoint =  endpoint + '/search/'

    def facets(self):

    
        content = self.session.make_request(
            method='get',
            endpoint=self.endpoint + "facets"
            
        )

        return content

class SubGenres(Catalog):

    def __init__(self, endpoint, session):
        super(Catalog, self).__init__()
        self.session: BeatportSession = session
        self.endpoint =  endpoint + '/sub-genres/'

    def facets(self):

    
        content = self.session.make_request(
            method='get',
            endpoint=self.endpoint + "facets"
            
        )

        return content

class Tracks(Catalog):

    def __init__(self, endpoint, session):
        super(Catalog, self).__init__()
        self.session: BeatportSession = session
        self.endpoint =  endpoint + '/tracks/'

    def search(self, artist_name : str = None, artist_id : int = None, available_worldwide : bool = None, 
               bpm : str = None, catalog_number : str = None, change_date : str = None, 
               chord_type_id : int = None, current_status : int = None, enabled : bool = None, 
               encode_status : str = None, encoded_date : str = None, exclusive_date : str = None, 
               exclusive_period : str = None, free_download_start_date : str = None, free_download_end_date : str = None, 
               genre_enabled : bool = None, genre_name : str = None, genre_id : int = None, 
               guid : str = None, id : int = None, isrc : str = None, 
               is_available_for_streaming : bool = None, is_classic : bool = None, key_name : str = None, 
               key_id : int = None, label_manager : str = None, label_name : str = None, 
               label_id : int = None, label_enabled : str = None, mix_name : str = None, 
               name : str = None, new_release_date : str = None, pre_order_date : str = None, 
               publish_date : str = None, publish_status : str = None, release_name : str = None, 
               release_id : int = None, sale_type : str = None, sub_genre_id : int = None, 
               supplier_name : str = None, supplier_id : int = None, track_number : str = None, 
               was_ever_exclusive : bool = None, order_by : str = "name", type : str = None, 
               type_id : int = None, page: int=None, per_page:int = None):

        """
        
        :param artist_name: 	Filter on case-insensitive artist name containment.
                                Supports `OR` lookup:
                                `param=value1,value2`
            
        :type  artist_name: str

        :param artist_id: 	Filter on artist ID exact match.
                            Supports `OR` lookup:
                            `param=value1,value2`
            
        :type  artist_id: int

        :param available_worldwide: 	Filter on available worldwide boolean match.
        :type  available_worldwide:     bool

        :param bpm: 	Filter on exact, less/greater than equal and range.
        :type  bpm:     str

        :param catalog_number: 	Filter on case-insensitive catalog_number exact match.
                                Supports `OR` lookup:
                                `param=value1,value2`
            
        :type  catalog_number: str

        :param change_date: 	Filter on exact, less/greater than equal and range.
                                Supports slice syntax:
                                `date=1970-01-01` (exact)
                                `date=:1971-01-01` (less than equal)
                                `date=1970-01-01:` (greater than equal)
                                `date=1970-01-01:1971-01-01` (range)
            
        :type  change_date: str

        :param chord_type_id: 	Filter on exact key ID match.
                                Supports `OR` lookup:
                                `param=value1,value2`
            
        :type  chord_type_id: int

        :param current_status: 	Filter on current_status ID exact match.
                                Supports `OR` lookup:
                                `param=value1,value2`
            
        :type  current_status: int

        :param enabled: 	Filter on enabled boolean match.
        :type  enabled:     bool

        :param encode_status: 	Filter on case-insensitive encode status exact match.
                    Supports `OR` lookup:
                    `param=value1,value2`
            
        :type  encode_status: str

        :param encoded_date: 	Filter on exact, less/greater than equal and range.
                                Supports slice syntax:
                                `date=1970-01-01` (exact)
                                `date=:1971-01-01` (less than equal)
                                `date=1970-01-01:` (greater than equal)
                                `date=1970-01-01:1971-01-01` (range)
            
        :type  encoded_date: str

        :param exclusive_date: 	Filter on exact, less/greater than equal and range.
                                `Supports slice syntax:
                                `date=1970-01-01` (exact)
                                `date=:1971-01-01` (less than equal)
                                `date=1970-01-01:` (greater than equal)
                                `date=1970-01-01:1971`-01-01` (range)
            
        :type  exclusive_date: str

        :param exclusive_period: 	Filter on case-insensitive exclusive period exact match.
                                    Supports `OR` lookup:
                                    `param=value1,value2`
            
        :type  exclusive_period: str

        :param free_download_start_date: 	Filter on exact, less/greater than equal and range.
                                            Supports slice syntax:
                                            `date=1970-01-01` (exact)
                                            `date=:1971-01-01` (less than equal)
                                            `date=1970-01-01:` (greater than equal)
                                            `date=1970-01-01:1971-01-01` (range)
            
        :type  free_download_start_date: str

        :param free_download_end_date: 	Filter on exact, less/greater than equal and range.
                                        Supports slice syntax:
                                        `date=1970-01-01` (exact)
                                        `date=:1971-01-01` (less than equal)
                                        `date=1970-01-01:` (greater than equal)
                                        `date=1970-01-01:1971-01-01` (range)
            
        :type  free_download_end_date: str

        :param genre_enabled: 	Filter on enabled boolean match.
        :type  genre_enabled:   bool

        :param genre_name: 	Filter on case-insensitive genre exact match.
                            Supports `OR` lookup:
                            `param=value1,value2`
            
        :type  genre_name: str

        :param genre_id: 	Filter on genre ID exact match.
                            Supports `OR` lookup:
                            `param=value1,value2`
            
        :type  genre_id: int

        :param guid: 	filter on exact guid match
                        Supports `OR` lookup:
                        `param=value1,value2`
            
        :type  guid: str

        :param id: 	Filter on ID exact match.
                    Supports `OR` lookup:
                    `param=value1,value2`
            
        :type  id: int

        :param isrc: 	Filter on exact ISRC match.
                        Supports `OR` lookup:
                        `param=value1,value2`
            
        :type  isrc: str

        :param is_available_for_streaming: 	Filter on streaming available boolean match.
        :type  is_available_for_streaming:  bool

        :param is_classic: 	Filter on is_classic boolean match.
        :type  is_classic:  bool

        :param key_name: 	
                                Filter key. Denote sharp as #, flat as b with minor/major separated by a space.
                                Available Keys:
                                    "A Minor"
                                    "A Major"
                                    "Ab Minor"
                                    "Ab Major"
                                    "A# Minor"
                                    "A# Major"
                                    "B Minor"
                                    "B Major"
                                    "Bb Minor"
                                    "Bb Major"
                                    "C Minor"
                                    "C Major"
                                    "C# Minor"
                                    "C# Major"
                                    "D Minor"
                                    "D Major"
                                    "Db Minor"
                                    "Db Major"
                                    "D# Minor"
                                    "D# Major"
                                    "E Minor"
                                    "E Major"
                                    "Eb Minor"
                                    "Eb Major"
                                    "F Minor"
                                    "F Major"
                                    "F# Minor"
                                    "F# Major"
                                    "G Minor"
                                    "G Major"
                                    "Gb Minor"
                                    "Gb Major"
                                    "G# Minor"
                                    "G# Major"
                                
                    Supports `OR` lookup:
                    `param=value1,value2`
            
        :type  key_name: str

        :param key_id: 	Filter on exact key ID match.
                        Supports `OR` lookup:
                        `param=value1,value2`
            
        :type  key_id: int

        :param label_manager: 	Filter by case-insensitive Label Manager name containment.
        :type  label_manager:   str

        :param label_name: 	Filter on case-insensitive label name containment.
                            Supports `OR` lookup:
                            `param=value1,value2`
            
        :type  label_name: str

        :param label_id: 	Filter on label ID exact match.
                            Supports `OR` lookup:
                            `param=value1,value2`
            
        :type  label_id: int

        :param label_enabled: 	Filter on enabled boolean match.
        :type  label_enabled: 

        :param mix_name: 	Filter on case-insensitive remix name containment.
                    Supports `OR` lookup:
                    `param=value1,value2`
            
        :type  mix_name: str

        :param name: 	Filter on case-insensitive name containment.
                        Supports `OR` lookup:
                        `param=value1,value2`
            
        :type  name: 

        :param new_release_date: 	Filter on exact, less/greater than equal and range.
                                    Supports slice syntax:
                                    `date=1970-01-01` (exact)
                                    `date=:1971-01-01` (less than equal)
                                    `date=1970-01-01:` (greater than equal)
                                    `date=1970-01-01:1971-01-01` (range)
            
        :type  new_release_date: str

        :param pre_order_date: 	Filter on exact, less/greater than equal and range.
                                Supports slice syntax:
                                `date=1970-01-01` (exact)
                                `date=:1971-01-01` (less than equal)
                                `date=1970-01-01:` (greater than equal)
                                `date=1970-01-01:1971-01-01` (range)
            
        :type  pre_order_date: str

        :param publish_date: 	Filter on exact, less/greater than equal and range.
                                Supports slice syntax:
                                `date=1970-01-01` (exact)
                                `date=:1971-01-01` (less than equal)
                                `date=1970-01-01:` (greater than equal)
                                `date=1970-01-01:1971-01-01` (range)
            
        :type  publish_date: str

        :param publish_status: 	Filter on publish_status exact match
                                Supports `OR` lookup:
                                `param=value1,value2`
            
        :type  publish_status: str

        :param release_name: 	Filter on case-insensitive release name containment.
                                Supports `OR` lookup:
                                `param=value1,value2`
            
        :type  release_name: str

        :param release_id: 	Filter on exact release ID match.
                            Supports `OR` lookup:
                            `param=value1,value2`
            
        :type  release_id: int

        :param sale_type: 	Filter on case-insensitive sale type exact match.
                            Supports `OR` lookup:
                            `param=value1,value2`
            
        :type  sale_type: str

        :param sub_genre_id: 	Filter on case-insensitive sub-genre exact match.
                                Supports `OR` lookup:
                                `param=value1,value2`
            
        :type  sub_genre_id: str

        :param supplier_name: 	Filter on case-insensitive name containment.
                                Supports `OR` lookup:
                                `param=value1,value2`
            
        :type  supplier_name: str

        :param supplier_id: 	Filter on case-insensitive name containment.
                                Supports `OR` lookup:
                                `param=value1,value2`
                        
        :type  supplier_id: int

        :param track_number: 	Filter on exact track_number match.
                                Supports `OR` lookup:
                                `param=value1,value2`
                        
        :type  track_number: str

        :param was_ever_exclusive: 	Filter on was_ever_exclusive boolean match.
        :type  was_ever_exclusive: bool

        :param order_by: 	Order by a field. Choices: publish_date, genre, label, name.
                            Use -genre for descending order
        :type  order_by:    str

        :param type: 	Filter on track type. Either Release, Album or Mix
                        Supports `OR` lookup:
                        `param=value1,value2`
            
        :type  type: str

        :param type_id: 	Filter on track release type id
                            Supports `OR` lookup:
                            `param=value1,value2`
            
        :type  type_id: int


        """

        params = {

            "artist_name" : artist_name, "artist_id" : artist_id, "available_worldwide" : available_worldwide, 
            "bpm" : bpm, "catalog_number" : catalog_number, "change_date" : change_date, 
            "chord_type_id" : chord_type_id, "current_status" : current_status, "enabled" : enabled, 
            "encode_status" : encode_status, "encoded_date" : encoded_date, "exclusive_date" : exclusive_date, 
            "exclusive_period" : exclusive_period, "free_download_start_date" : free_download_start_date, 
            "free_download_end_date" : free_download_end_date, "genre_enabled" : genre_enabled, 
            "genre_name" : genre_name, "genre_id" : genre_id, "guid" : guid, "id" : id, "isrc" : isrc, 
            "is_available_for_streaming" : is_available_for_streaming, "is_classic" : is_classic, "key_name" : key_name, 
            "key_id" : key_id, "label_manager" : label_manager, "label_name" : label_name, 
            "label_id" : label_id, "label_enabled" : label_enabled, "mix_name" : mix_name, 
            "name" : name, "new_release_date" : new_release_date, "pre_order_date" : pre_order_date, 
            "publish_date" : publish_date, "publish_status" : publish_status, "release_name" : release_name, 
            "release_id" : release_id, "sale_type" : sale_type, "sub_genre_id" : sub_genre_id, 
            "supplier_name" : supplier_name, "supplier_id" : supplier_id, "track_number" : track_number, 
            "was_ever_exclusive" : was_ever_exclusive, "order_by" : order_by, "type" : type, "type_id" : type_id,
            "page":page, "per_page":per_page 
        }

        content = self.session.make_request(
            method='get',
            endpoint=self.endpoint,
            params = params
            
        )
        content['topic'] = 'beatport_tracks_requests'

        return content

    def similar(self, artist_name : str = None, artist_id : int = None, available_worldwide : bool = None, 
               bpm : str = None, catalog_number : str = None, change_date : str = None, 
               chord_type_id : int = None, current_status : int = None, enabled : bool = None, 
               encode_status : str = None, encoded_date : str = None, exclusive_date : str = None, 
               exclusive_period : str = None, free_download_start_date : str = None, free_download_end_date : str = None, 
               genre_enabled : bool = None, genre_name : str = None, genre_id : int = None, 
               guid : str = None, id : int = None, isrc : str = None, 
               is_available_for_streaming : bool = None, is_classic : bool = None, key_name : str = None, 
               key_id : int = None, label_manager : str = None, label_name : str = None, 
               label_id : int = None, label_enabled : str = None, mix_name : str = None, 
               name : str = None, new_release_date : str = None, pre_order_date : str = None, 
               publish_date : str = None, publish_status : str = None, release_name : str = None, 
               release_id : int = None, sale_type : str = None, sub_genre_id : int = None, 
               supplier_name : str = None, supplier_id : int = None, track_number : str = None, 
               was_ever_exclusive : bool = None, order_by : str = None, type : str = None, 
               type_id : int = None):

        """
        
        :param artist_name: 	Filter on case-insensitive artist name containment.
                                Supports `OR` lookup:
                                `param=value1,value2`
            
        :type  artist_name: str

        :param artist_id: 	Filter on artist ID exact match.
                            Supports `OR` lookup:
                            `param=value1,value2`
            
        :type  artist_id: int

        :param available_worldwide: 	Filter on available worldwide boolean match.
        :type  available_worldwide:     bool

        :param bpm: 	Filter on exact, less/greater than equal and range.
        :type  bpm:     str

        :param catalog_number: 	Filter on case-insensitive catalog_number exact match.
                                Supports `OR` lookup:
                                `param=value1,value2`
            
        :type  catalog_number: str

        :param change_date: 	Filter on exact, less/greater than equal and range.
                                Supports slice syntax:
                                `date=1970-01-01` (exact)
                                `date=:1971-01-01` (less than equal)
                                `date=1970-01-01:` (greater than equal)
                                `date=1970-01-01:1971-01-01` (range)
            
        :type  change_date: str

        :param chord_type_id: 	Filter on exact key ID match.
                                Supports `OR` lookup:
                                `param=value1,value2`
            
        :type  chord_type_id: int

        :param current_status: 	Filter on current_status ID exact match.
                                Supports `OR` lookup:
                                `param=value1,value2`
            
        :type  current_status: int

        :param enabled: 	Filter on enabled boolean match.
        :type  enabled:     bool

        :param encode_status: 	Filter on case-insensitive encode status exact match.
                    Supports `OR` lookup:
                    `param=value1,value2`
            
        :type  encode_status: str

        :param encoded_date: 	Filter on exact, less/greater than equal and range.
                                Supports slice syntax:
                                `date=1970-01-01` (exact)
                                `date=:1971-01-01` (less than equal)
                                `date=1970-01-01:` (greater than equal)
                                `date=1970-01-01:1971-01-01` (range)
            
        :type  encoded_date: str

        :param exclusive_date: 	Filter on exact, less/greater than equal and range.
                                `Supports slice syntax:
                                `date=1970-01-01` (exact)
                                `date=:1971-01-01` (less than equal)
                                `date=1970-01-01:` (greater than equal)
                                `date=1970-01-01:1971`-01-01` (range)
            
        :type  exclusive_date: str

        :param exclusive_period: 	Filter on case-insensitive exclusive period exact match.
                                    Supports `OR` lookup:
                                    `param=value1,value2`
            
        :type  exclusive_period: str

        :param free_download_start_date: 	Filter on exact, less/greater than equal and range.
                                            Supports slice syntax:
                                            `date=1970-01-01` (exact)
                                            `date=:1971-01-01` (less than equal)
                                            `date=1970-01-01:` (greater than equal)
                                            `date=1970-01-01:1971-01-01` (range)
            
        :type  free_download_start_date: str

        :param free_download_end_date: 	Filter on exact, less/greater than equal and range.
                                        Supports slice syntax:
                                        `date=1970-01-01` (exact)
                                        `date=:1971-01-01` (less than equal)
                                        `date=1970-01-01:` (greater than equal)
                                        `date=1970-01-01:1971-01-01` (range)
            
        :type  free_download_end_date: str

        :param genre_enabled: 	Filter on enabled boolean match.
        :type  genre_enabled:   bool

        :param genre_name: 	Filter on case-insensitive genre exact match.
                            Supports `OR` lookup:
                            `param=value1,value2`
            
        :type  genre_name: str

        :param genre_id: 	Filter on genre ID exact match.
                            Supports `OR` lookup:
                            `param=value1,value2`
            
        :type  genre_id: int

        :param guid: 	filter on exact guid match
                        Supports `OR` lookup:
                        `param=value1,value2`
            
        :type  guid: str

        :param id: 	Filter on ID exact match.
                    Supports `OR` lookup:
                    `param=value1,value2`
            
        :type  id: int

        :param isrc: 	Filter on exact ISRC match.
                        Supports `OR` lookup:
                        `param=value1,value2`
            
        :type  isrc: str

        :param is_available_for_streaming: 	Filter on streaming available boolean match.
        :type  is_available_for_streaming:  bool

        :param is_classic: 	Filter on is_classic boolean match.
        :type  is_classic:  bool

        :param key_name: 	
                                Filter key. Denote sharp as #, flat as b with minor/major separated by a space.
                                Available Keys:
                                    "A Minor"
                                    "A Major"
                                    "Ab Minor"
                                    "Ab Major"
                                    "A# Minor"
                                    "A# Major"
                                    "B Minor"
                                    "B Major"
                                    "Bb Minor"
                                    "Bb Major"
                                    "C Minor"
                                    "C Major"
                                    "C# Minor"
                                    "C# Major"
                                    "D Minor"
                                    "D Major"
                                    "Db Minor"
                                    "Db Major"
                                    "D# Minor"
                                    "D# Major"
                                    "E Minor"
                                    "E Major"
                                    "Eb Minor"
                                    "Eb Major"
                                    "F Minor"
                                    "F Major"
                                    "F# Minor"
                                    "F# Major"
                                    "G Minor"
                                    "G Major"
                                    "Gb Minor"
                                    "Gb Major"
                                    "G# Minor"
                                    "G# Major"
                                
                    Supports `OR` lookup:
                    `param=value1,value2`
            
        :type  key_name: str

        :param key_id: 	Filter on exact key ID match.
                        Supports `OR` lookup:
                        `param=value1,value2`
            
        :type  key_id: int

        :param label_manager: 	Filter by case-insensitive Label Manager name containment.
        :type  label_manager:   str

        :param label_name: 	Filter on case-insensitive label name containment.
                            Supports `OR` lookup:
                            `param=value1,value2`
            
        :type  label_name: str

        :param label_id: 	Filter on label ID exact match.
                            Supports `OR` lookup:
                            `param=value1,value2`
            
        :type  label_id: int

        :param label_enabled: 	Filter on enabled boolean match.
        :type  label_enabled: 

        :param mix_name: 	Filter on case-insensitive remix name containment.
                    Supports `OR` lookup:
                    `param=value1,value2`
            
        :type  mix_name: str

        :param name: 	Filter on case-insensitive name containment.
                        Supports `OR` lookup:
                        `param=value1,value2`
            
        :type  name: 

        :param new_release_date: 	Filter on exact, less/greater than equal and range.
                                    Supports slice syntax:
                                    `date=1970-01-01` (exact)
                                    `date=:1971-01-01` (less than equal)
                                    `date=1970-01-01:` (greater than equal)
                                    `date=1970-01-01:1971-01-01` (range)
            
        :type  new_release_date: str

        :param pre_order_date: 	Filter on exact, less/greater than equal and range.
                                Supports slice syntax:
                                `date=1970-01-01` (exact)
                                `date=:1971-01-01` (less than equal)
                                `date=1970-01-01:` (greater than equal)
                                `date=1970-01-01:1971-01-01` (range)
            
        :type  pre_order_date: str

        :param publish_date: 	Filter on exact, less/greater than equal and range.
                                Supports slice syntax:
                                `date=1970-01-01` (exact)
                                `date=:1971-01-01` (less than equal)
                                `date=1970-01-01:` (greater than equal)
                                `date=1970-01-01:1971-01-01` (range)
            
        :type  publish_date: str

        :param publish_status: 	Filter on publish_status exact match
                                Supports `OR` lookup:
                                `param=value1,value2`
            
        :type  publish_status: str

        :param release_name: 	Filter on case-insensitive release name containment.
                                Supports `OR` lookup:
                                `param=value1,value2`
            
        :type  release_name: str

        :param release_id: 	Filter on exact release ID match.
                            Supports `OR` lookup:
                            `param=value1,value2`
            
        :type  release_id: int

        :param sale_type: 	Filter on case-insensitive sale type exact match.
                            Supports `OR` lookup:
                            `param=value1,value2`
            
        :type  sale_type: str

        :param sub_genre_id: 	Filter on case-insensitive sub-genre exact match.
                                Supports `OR` lookup:
                                `param=value1,value2`
            
        :type  sub_genre_id: str

        :param supplier_name: 	Filter on case-insensitive name containment.
                                Supports `OR` lookup:
                                `param=value1,value2`
            
        :type  supplier_name: str

        :param supplier_id: 	Filter on case-insensitive name containment.
                                Supports `OR` lookup:
                                `param=value1,value2`
                        
        :type  supplier_id: int

        :param track_number: 	Filter on exact track_number match.
                                Supports `OR` lookup:
                                `param=value1,value2`
                        
        :type  track_number: str

        :param was_ever_exclusive: 	Filter on was_ever_exclusive boolean match.
        :type  was_ever_exclusive: bool

        :param order_by: 	Order by a field. Choices: publish_date, genre, label, name.
                            Use -genre for descending order
        :type  order_by:    str

        :param type: 	Filter on track type. Either Release, Album or Mix
                        Supports `OR` lookup:
                        `param=value1,value2`
            
        :type  type: str

        :param type_id: 	Filter on track release type id
                            Supports `OR` lookup:
                            `param=value1,value2`
            
        :type  type_id: int


        """

        params = {

            "artist_name" : artist_name, "artist_id" : artist_id, "available_worldwide" : available_worldwide, 
            "bpm" : bpm, "catalog_number" : catalog_number, "change_date" : change_date, 
            "chord_type_id" : chord_type_id, "current_status" : current_status, "enabled" : enabled, 
            "encode_status" : encode_status, "encoded_date" : encoded_date, "exclusive_date" : exclusive_date, 
            "exclusive_period" : exclusive_period, "free_download_start_date" : free_download_start_date, 
            "free_download_end_date" : free_download_end_date, "genre_enabled" : genre_enabled, 
            "genre_name" : genre_name, "genre_id" : genre_id, "guid" : guid, "id" : id, "isrc" : isrc, 
            "is_available_for_streaming" : is_available_for_streaming, "is_classic" : is_classic, "key_name" : key_name, 
            "key_id" : key_id, "label_manager" : label_manager, "label_name" : label_name, 
            "label_id" : label_id, "label_enabled" : label_enabled, "mix_name" : mix_name, 
            "name" : name, "new_release_date" : new_release_date, "pre_order_date" : pre_order_date, 
            "publish_date" : publish_date, "publish_status" : publish_status, "release_name" : release_name, 
            "release_id" : release_id, "sale_type" : sale_type, "sub_genre_id" : sub_genre_id, 
            "supplier_name" : supplier_name, "supplier_id" : supplier_id, "track_number" : track_number, 
            "was_ever_exclusive" : was_ever_exclusive, "order_by" : order_by, "type" : type, "type_id" : type_id, 
        }

        content = self.session.make_request(
            method='get',
            endpoint=self.endpoint+'/similar/',
            params = params
            
        )

        return content

    def beatbot(self, id):
        """
        Get a list of releases that are similar to the release with the given id.

        :param id: 	Filter by exact ID match.
                    Supports `OR` lookup:
                    `param=value1,value2`
        :type  int:

        
        """


        content = self.session.make_request(
            method='get',
            endpoint=self.endpoint + '{}/beatbot/'.format(id)
            
        )

        return content

    def get_top_tracks(self, num:int, enabled: bool = None,
                       page: int=None, per_page: int = None):

        """
        Returns top num tracks most popular rank
        
        :param release_id: Filter by genre id exact match.
                    Supports `OR` lookup:
                
                    `param=value1,value2`
                
        :type  genre_id: int
        
        :param num: limited between 1 and 100
                
        :type  num: int"""

    
        content = self.session.make_request(
            method='get',
            endpoint=self.endpoint + "/top/{num}".format(num=num)
            
        )

        return content


    def facets(self):

    
        content = self.session.make_request(
            method='get',
            endpoint=self.endpoint + "facets"
            
        )

        return content