from concurrent.futures import ThreadPoolExecutor
from common import timer, print_title_from_url, urls


@timer
def print_titles():
    with ThreadPoolExecutor(max_workers=10) as executor:
        for url in urls:
            executor.submit(print_title_from_url, url)


print_titles()