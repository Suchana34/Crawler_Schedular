import schedule
import time

def crawl():
    print("cralwer is running")

schedule.every(10).seconds.do(crawl)
schedule.every().wednesday.at('1:00').do(crawl)

while l:
    schedule.run_pending()
    time.sleep(1)

    