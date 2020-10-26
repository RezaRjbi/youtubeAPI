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
        response_dic = dict(title=response['items'][0]['snippet']['title'],
                            description=response['items'][0]['snippet']['description'],
                            account_created=response['items'][0]['snippet']['publishedAt'],
                            profile_pic=response['items'][0]['snippet']['thumbnails']['high']['url'],
                            channel_country=response['items'][0]['snippet'].get('country'),
                            total_views=response['items'][0]['statistics']['viewCount'],
                            subscribers=response['items'][0]['statistics']['subscriberCount'],
                            total_videos=response['items'][0]['statistics']['videoCount'])
        return response_dic
