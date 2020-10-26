from YT_API import app
from flask import request, jsonify
from YT_API.get_info import YouTube


@app.route('/api/')
def info():
    args = request.args
    id = args.get('id')
    username = args.get('username')
    print(args)
    if id:
        try:
            req = YouTube(id=id)
            response = req.fetch_data()
            return jsonify(response)
        except KeyError:
            return jsonify(message='invalid id/username')
    elif username:
        try:
            req = YouTube(username=username)
            response = req.fetch_data()
            return jsonify(response)
        except KeyError:
            return jsonify(message='invalid id/username')
    else:
        return jsonify(message='no valid id or username provided')

@app.route('/')
def home():
    return 'hi'