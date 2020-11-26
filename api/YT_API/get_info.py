from googleapiclient.discovery import build
from YT_API.utils import link_type


class YouTube:
    API_KEY = ''
    youtube = build('youtube', 'v3', developerKey=API_KEY)
    channel_id = None
    response_dic = None

    def __init__(self, pagelink):
        self.id, self.username = link_type(pagelink)

    def fetch_data(self):
        if any((self.id, self.username)):
            request = self.youtube.channels().list(
                part='statistics,snippet',
                id=self.id,
                forUsername=self.username
            )

            response = request.execute()
        try:
            first_item = response['items'][0]
            snippet = first_item['snippet']
            statistics = first_item['statistics']
        except:
            return dict(message='check your link again', response=404)

        self.channel_id = first_item.get('id')
        self.response_dic = dict(
            title=snippet.get('title'),
            description=snippet.get('description'),
            channel_id=first_item.get('id'),
            account_created=snippet.get('publishedAt'),
            profile_pic=snippet.get('thumbnails')['high']['url'],
            channel_country=snippet.get('country'),
            total_views=statistics.get('viewCount'),
            subscribers=statistics.get('subscriberCount'),
            total_videos=statistics.get('videoCount')
        )
        return self.response_dic

    def get_playlis(self):
        request = self.youtube.playlists().list(
            part='snippet,status',
            channelId=self.channel_id,
            maxResults=50
        )
        response = request.execute()
        all_playlists = list()
        items = response['items']
        if items:
            for item in items:
                dic = dict(
                    published_date=item['snippet'].get('publishedAt')[:10],
                    title=item['snippet'].get('title'),
                    description=item['snippet'].get('description'),
                    thumbnail=item['snippet'].get('thumbnails').get('high')['url']
                )

                all_playlists.append(dic)
            all_playlists.append({'total_playlist': response['pageInfo']['totalResults']})
        self.response_dic['playlists'] = all_playlists

        return self.response_dic
