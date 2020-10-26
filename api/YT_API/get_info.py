from googleapiclient.discovery import build

class YouTube:

    API_KEY = 'AIzaSyA20aP7050g9V8ufXKn755gY7ym8oyTbKs'
    youtube = build('youtube', 'v3', developerKey=API_KEY)

    def __init__(self, id=None, username=None):
        """

        :type id: str
        :type username: str
        """
        self.id = id
        self.username = username
        self.response = None

    def fetch_data(self):

        request = self.youtube.channels().list(
            part='statistics,snippet',
            id=self.id,
            forUsername=self.username
        )

        response = request.execute()

        first_item = response['items'][0]
        snippet = first_item['snippet']
        statistics = first_item['statistics']

        response_dic = dict(
            title=snippet['title'],
            description=snippet['description'],
            account_created=snippet['publishedAt'],
            profile_pic=snippet['thumbnails']['high']['url'],
            channel_country=snippet.get('country'),
            total_views=statistics['viewCount'],
            subscribers=statistics['subscriberCount'],
            total_videos=statistics['videoCount']
        )

        return response_dic
