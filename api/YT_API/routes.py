from YT_API import app
from flask import request, jsonify
from YT_API.get_info import YouTube
from YT_API.yt_dl import yt_link_finder

def send_res(req):
    if req:
        response = req.fetch_data()
        return jsonify(response)
    return jsonify(message='invalid id/username')


@app.route('/info')
def info():
    form = request.form
    id = form.get('id')
    username = form.get('username')
    try:
        req = YouTube(id=id, username=username)
    except:
        pass
    return send_res(req)

@app.route('/youtube/download')
def download():
    pagelink = request.form.get('pagelink')
    return jsonify(yt_link_finder(pagelink))