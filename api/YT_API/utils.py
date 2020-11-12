from flask import jsonify


def send_res(req):
    if req:
        response = req.fetch_data()
        return jsonify(response)
    return jsonify(message='invalid id/username')


def link_type(link: str):
    try:
        if link[-1] == '/':
            index = -2
        else:
            index = -1
    except IndexError:
        return None, None
    link_info: list = link.split('/')
    if 'channel' in link_info:
        id = link_info[index]
        username = None
    elif 'user' in link_info:
        id = None
        username = link_info[index]
    else:
        id = None
        username = None
    return id, username


def link_checker(link):
    bad_links = ['user', 'channel', '/c/']
    for bad_link in bad_links:
        if bad_link in link:
            return False
    return True