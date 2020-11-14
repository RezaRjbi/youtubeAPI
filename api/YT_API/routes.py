from YT_API import app
from flask import request, jsonify
from YT_API.get_info import YouTube
from YT_API.utils import send_res
from YT_API.yt_dl import VideoObj


@app.route('/info', methods=['POST'])
def info():
    form = request.form
    pagelink = form.get('pagelink')
    _playlists = form.get('_playlists')
    req = YouTube(pagelink)
    response = req.fetch_data()
    if _playlists:
        response = req.get_playlis()
    return jsonify(response)


@app.route('/youtube/download', methods=['POST'])
def download():
    pagelink = request.form.get('pagelink')
    video = VideoObj(pagelink)
    _info = video.yt_link_finder()
    response_dict = VideoObj.as_dict(_info)
    return jsonify(response_dict)


@app.route('/test')
def test():
    return jsonify(message='OK', response=200)
