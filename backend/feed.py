from operator import methodcaller
from xml.dom.minidom import Attr
from flask import Blueprint, request
from urllib.parse import urlparse

feed_router = Blueprint('feed', __name__)

def check_feed_url(feed_url):
    print("Recd:", feed_url)
    min_attr = ('scheme' , 'netloc')
    tokens = urlparse(feed_url)
    return all(getattr(tokens, qattrs) for qattrs in min_attr)

@feed_router.route('/add_feed', methods=['POST'])
def add_feed():
    data = request.get_json()
    print(data)
    listOfFeedsToShow = []
    isValidFeed = check_feed_url(feed_url=data["feed_url"])
    print(isValidFeed)
    if isValidFeed:
        listOfFeedsToShow.append(data["feed_url"])
        return {"response":"Added URL to list of Valid Feeds"}
    else:
        return {"response":"Invalid URL, not added to list of valid feeds"}
