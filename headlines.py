import feedparser
from flask import Flask
from flask import render_template

app=Flask(__name__)

RSS_FEEDS = {'bbc': 'http://feeds.bbci.co.uk/news/rss.xml',
			 'cnn': 'http://rss.cnn.com/rss/edition.rss',
			 'fox': 'http://feeds.foxnews.com/foxnews/latest',
			 'iol': 'http://www.iol.co.za/cmlink/1.640'}

@app.route("/")
@app.route("/<publication>")
def bbc(publication='bbc'):
	return get_news(publication)

def get_news(publication):
	feed = feedparser.parse(RSS_FEEDS[publication])
	if not feed['entries']:
		return "Entries get nothing from %s" % publication
	first_artical = feed['entries']

	return render_template("home.html", articals=first_artical)

if __name__ == '__main__':
	app.run(port=5000, debug=True)
