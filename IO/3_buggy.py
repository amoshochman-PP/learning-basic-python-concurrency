import threading

from common import timer, print_title_from_url, urls

COUNTER = 0


def worker(url):
    global COUNTER
    COUNTER += 1
    print_title_from_url(url)


@timer
def print_titles():
    threads = []
    for url in urls:
        thread = threading.Thread(target=worker, args=(url,))
        threads.append(thread)
        thread.start()
    for thread in threads:
        thread.join()


print_titles()
print(COUNTER)
