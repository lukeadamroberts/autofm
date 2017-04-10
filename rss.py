import feedparser

################################################################################
## rss.py
## Contains all the functions related to rss collection. Maybe add some filtering
## or classification later?
################################################################################

############################
# Add rss feeds to this list
############################

rssList = ['http://feeds.bbci.co.uk/news/technology/rss.xml',
        'http://feeds.bbci.co.uk/news/rss.xml?edition=uk',
        'https://www.gamespot.com/feeds/news/',
        'http://feeds.bbci.co.uk/news/science_and_environment/rss.xml']

#Downloads the rss values
def collectRss():
    news = []
    for i in rssList:
        item = feedparser.parse(i)
        for x in item.entries:
            news.append(x.title)
    return news
