from flask import Blueprint, render_template, request
from urllib.parse import urlparse
import requests
from backend.rss_parser import parse_rss


feed_router = Blueprint('feed', __name__)

def check_feed_url(feed_url):
    print("Recd:", feed_url)
    min_attr = ('scheme' , 'netloc')
    tokens = urlparse(feed_url)
    return all(getattr(tokens, qattrs) for qattrs in min_attr)

def fetch_rss_from_feed(feed_list):
    for feed in feed_list:
        rss_response = requests.get(url=feed)
        if rss_response.status_code == 200:
            parse_rss(rss_response.text)


@feed_router.route('/add_feed', methods=['POST'])
def add_feed():
    data = request.get_json()
    print(data)
    listOfFeedsToShow = []
    isValidFeed = check_feed_url(feed_url=data["feed_url"])
    print(isValidFeed)
    if isValidFeed:
        listOfFeedsToShow.append(data["feed_url"])
        rss = fetch_rss_from_feed(listOfFeedsToShow)
        print(f'Feed has been fetched from {data["feed_url"]}')
        return render_template('index.html',articles_data = rss)
    else:
        return {"response":"Invalid URL, not added to list of valid feeds"}
