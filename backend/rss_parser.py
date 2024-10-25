from rss_parser import RSSParser
import pprint as pp

def parse_rss(rss_feed):
    try:
        rss = RSSParser.parse(rss_feed)
        rss_json = rss.json_plain()
        print(type(rss_json))
    except Exception as e:
        print(f"Error parsing RSS Feed! Error: {e}")
    return rss