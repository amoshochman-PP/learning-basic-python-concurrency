import threading

from common import timer, print_title_from_url, urls


COUNTER = 0

@timer
def print_titles():
    threads = []
    for url in urls:
        thread = threading.Thread(target=print_title_from_url, args=(url,))
        threads.append(thread)
        thread.start()
    for thread in threads:
        thread.join()


print_titles()
