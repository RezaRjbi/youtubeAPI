from YT_API import app
from flask import request, jsonify
from YT_API.get_info import YouTube

def send_res(req = None):
    if (req):
        response = req.fetch_data()
        return jsonify(response)
    return jsonify(message='invalid id/username')

@app.route('/info')
def info():
    form = request.form
    id = form.get('id')
    username = form.get('username')
    try:
        if id:
            req = YouTube(id=id)
        elif username:
            req = YouTube(username=username)
    except KeyError:
        pass
    return send_res()
