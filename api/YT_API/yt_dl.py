import youtube_dl

def link_cheker(link):
    bad_links = ['user', 'channel']
    for bad_link in bad_links:
        if bad_link in link:
            return False
    return True
def yt_link_finder(pagelink):
    if link_cheker(pagelink):
        ydl = youtube_dl.YoutubeDL({'outtmpl': '%(id)s.%(ext)s'})

        with ydl:
            try:
                result = ydl.extract_info(pagelink, download=False)
                download_links =list()
                for link in result['formats']:
                    links_dic = dict(url=link['url'],
                                     extention=link['ext'],
                                     format=link['format_note'])
                    download_links.append(links_dic)

                response_dic = dict(uploder=result.get('uploader'),
                                    uploder_url=result.get('uploader_url'),
                                    channel_url=result.get('channel_url'),
                                    upload_date=result.get('upload_date'),
                                    title=result.get('title'),
                                    thumbnail=result['thumbnails'][-1].get('url'),
                                    description=result.get('description'),
                                    views=result.get('view_count'),
                                    likes=result.get('like_count'),
                                    download_info=download_links
                                    )
                return response_dic
            except:
                return {'message': 'check your link again!'}
    return {'message': 'Send a video page link'}


if __name__ =='__main__':
    print(yt_link_finder('https://www.youtube.com/watch?v=0Q_8taHAuQQ'))
