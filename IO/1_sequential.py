from common import urls, timer, print_title_from_url


@timer
def print_titles():
    for url in urls:
        print_title_from_url(url)


print_titles()
