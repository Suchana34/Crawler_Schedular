#wrong code

#!/usr/bin/python3
#"""Scheduler for spiders."""
#import time

#from scrapy.crawler import CrawlerProcess
#from scrapy.utils.project import get_project_settings

#from my_project.spiders.deals import DealsSpider


#def crawl_job():
#    """Job to start spiders."""
#    settings = get_project_settings()
#    process = CrawlerProcess(settings)
#    process.crawl(DealsSpider)
#    process.start() # the script will block here until the end of the crawl


#if __name__ == '__main__':

 #   while True:
 #       crawl_job()
 #       time.sleep(30) # wait 30 seconds then crawl again
        
        
        
 # correct code
 #You're getting the ReactorNotRestartable error because the Reactor cannot be started multiple times in Twisted. Basically, each time process.start() is called, it will try to start the reactor.
 
from twisted.internet import reactor
from scrapy.crawler import CrawlerRunner
from scrapy.utils.project import get_project_settings

from my_project.spiders.deals import DealsSpider


def crawl_job():
    """
    Job to start spiders.
    Return Deferred, which will execute after crawl has completed.
    """
    settings = get_project_settings()
    runner = CrawlerRunner(settings)
    return runner.crawl(DealsSpider)

def schedule_next_crawl(null, sleep_time):
    """
    Schedule the next crawl
    """
    reactor.callLater(sleep_time, crawl)

def crawl():
    """
    A "recursive" function that schedules a crawl 30 seconds after
    each successful crawl.
    """
    # crawl_job() returns a Deferred
    d = crawl_job()
    # call schedule_next_crawl(<scrapy response>, n) after crawl job is complete
    d.addCallback(schedule_next_crawl, 30)
    d.addErrback(catch_error)

def catch_error(failure):
    print(failure.value)

if __name__=="__main__":
    crawl()
    reactor.run()
    
    
 #The reactor is directly called, substitute CrawlerProcess for CrawlerRunner, time.sleep has been removed so that the reactor doesn't block, the while loop has been replaced with a continuous call to the crawl function via callLater
 
