
from beatport.session import BeatportSession

class Auxiliary(object):

    def __init__(self, session: object):
        self.session: BeatportSession = session
        self.endpoint = "auxiliary"
        pass

    def artist_types(self, page: int=None, per_page: int = None):
        """"""

        params = {
                  'page':page,
                  'per_page':per_page,
                    }

        content = self.session.make_request(
            method='get',
            endpoint=self.endpoint + "/artist-types/",
            params=params
            
        )

        return content