import random
import urllib3
import time


endpoints = [
    "http://app:9292/",
    "http://app:9292/ingest",
    "http://app:9292/search",
    "http://app:9292/delete",
    "http://app:9292/update",
    "http://app:9292/error",
]


def main():
    http = urllib3.PoolManager()
    while True:
        url = random.choice(endpoints)
        try:
            http.request("GET", url, preload_content=True)
        except Exception:
            pass
        time.sleep(1)


main()