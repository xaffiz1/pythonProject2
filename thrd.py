import threading
import time
from datetime import timedelta

import httpx
import redis


def get_website_data(url):
    response = httpx.get(url).read()
    response.decode('utf-8')
    con = redis.Redis(host="localhost", port=6379, decode_responses=True)
    con.set(name=url , value=response , ex=timedelta(60))



websites = [
"https://www.google.com",
    "https://www.wikipedia.org" ,
    "https://www.openai.com" ,
    "https://www.github.com" ,
    "https://www.amazon.com" ,
    "https://www.nytimes.com" ,
    "https://www.reddit.com" ,
    "https://www.instagram.com" ,
    "https://www.twitter.com" ,
    "https://www.linkedin.com"
]

threads = []
for website in websites:
    start = time.time()
    thread = threading.Thread(target=get_website_data, args=(website,))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()