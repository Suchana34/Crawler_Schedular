#Twisted is a python framework that is used for input and output processes like HTTP requests for example. 
# Now it does this through what’s called a twister event reactor. Scrapy is built on top of twisted! 
# We won’t go into too much detail here but needless to say, the CrawlerProcess class imports a twisted reactor which listens for events like multiple HTTP requests. 
# This is at the heart of how scrapy works.




import scrapy

from scrapy.crawler import CrawlerProcess

class TestSpider(scrapy.Spider):
    name = 'test'
    custom_settings = { 'DOWNLOD_DELAY': 1 }
    headers = {} 
    params = {}

    def start_requests(self):
        yield scrapy.Requests(url, headers=headers, params=params,callback = self.parse)

   def parse(self,response):
       print(response.body)



if __name__ == "__main__":
  process = CrawlerProcess()
  process.crawl(TestSpider)
  process.start()