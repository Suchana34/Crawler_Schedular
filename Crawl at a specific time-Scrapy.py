import datetime as dt

def schedule_next_crawl(null, hour, minute):
    tomorrow = (
        dt.datetime.now() + dt.timedelta(days=1)
        ).replace(hour=hour, minute=minute, second=0, microsecond=0)
    sleep_time = (tomorrow - dt.datetime.now()).total_seconds()
    reactor.callLater(sleep_time, crawl)

def crawl():
    d = crawl_job()
    # crawl everyday at 1pm
    d.addCallback(schedule_next_crawl, hour=13, minute=30)
