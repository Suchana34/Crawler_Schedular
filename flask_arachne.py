#https://arachne.readthedocs.io/en/latest/

#Arachne provides a wrapper around your scrapy Spider object to run them through a flask app. 
# All you have to do is customize SPIDER_SETTINGS in the settings file.

#pip install Arachne

# settings.py file
SPIDER_SETTINGS = [
        {
                'endpoint': 'dmoz',
                'location': 'spiders.DmozSpider',
                'spider': 'DmozSpider'
        }
]

#It looks very similar to a flask app but since Scrapy depends on the python twisted package, we need to run our flask app with twisted:

from twisted.web.wsgi import WSGIResource
from twisted.web.server import Site
from twisted.internet import reactor
from arachne import Arachne

app = Arachne(__name__)

resource = WSGIResource(reactor, reactor.getThreadPool(), app)
site = Site(resource)
reactor.listenTCP(8080, site)

if __name__ == '__main__':
        reactor.run()