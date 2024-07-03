import feedparser

def fetch_rss_feed(url):
    feed = feedparser.parse(url)
    headlines = [{'title': entry.title, 'link': entry.link} for entry in feed.entries]
    return headlines

# Test the RSS feed
rss_url = 'https://www.moneycontrol.com/rss/MCtopnews.xml'
news_headlines = fetch_rss_feed(rss_url)

# Print the headlines
for headline in news_headlines:
    print(f"Title: {headline['title']}")
    print(f"Link: {headline['link']}\n")