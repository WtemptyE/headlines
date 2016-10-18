import feedparser
from flask import Flask

app=Flask(__name__)

RSS_FEEDS = {'bbc': 'http:http://feeds.bbci.co.uk/news/rss.xml',
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
	first_artical = feed['entries'][0]
	return """<html>
		<body>
			<h1>Headlines</h1></ br>
			<b>{0}</b></ br>
			<i>{1}</i></ br>
			<p>{2}</p></ br>
		</body>
	</html>""".format(first_artical.get('title'),first_artical.get('published'),first_artical.get('summary'))

if __name__ == '__main__':
	app.run(port=5000, debug=True)
