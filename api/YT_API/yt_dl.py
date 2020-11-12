import os
import sys

PATH = os.path.join(os.getcwd())
sys.path.append(PATH)

import youtube_dl
from YT_API.utils import link_checker


class VideoObj:

    def __init__(self, pagelink):
        self.pagelink = pagelink

    def yt_link_finder(self):
        if link_checker(self.pagelink):
            ydl = youtube_dl.YoutubeDL({'outtmpl': '%(id)s.%(ext)s'})

            with ydl:
                try:
                    result = ydl.extract_info(self.pagelink, download=False)
                    return result
                except:
                    pass

        return dict(message='Send a video page link')

    @classmethod
    def as_dict(cls, data):
        try:
            download_links = list()
            for link in data['formats']:
                links_dic = dict(url=link['url'],
                                 extention=link['ext'],
                                 format=link['format_note'])
                download_links.append(links_dic)
        except KeyError:
            return dict(message='something went wrong!', response=404)

        response_dic = dict(uploder=data.get('uploader'),
                            uploder_url=data.get('uploader_url'),
                            channel_url=data.get('channel_url'),
                            upload_date=data.get('upload_date'),
                            title=data.get('title'),
                            thumbnail=data['thumbnails'][-1].get('url'),
                            description=data.get('description'),
                            views=data.get('view_count'),
                            likes=data.get('like_count'),
                            download_info=download_links
                            )
        return response_dic
