import re
import time
from functools import wraps

import requests

urls = ["https://www.python.org", "https://docs.python.org/3/", "https://www.djangoproject.com",
        "https://www.github.com", "https://www.mozilla.org", "https://www.gnu.org", "https://www.nasa.gov",
        "https://www.pypi.org", "https://www.sqlite.org", "https://www.postgresql.org"]


def get_html_from_url(url):
    try:
        response = requests.get(url, timeout=2)
        if response.status_code != 200 or not response.text:
            return None
        return response.text
    except:
        return None


def print_title_from_url(url):
    html = get_html_from_url(url)
    if not html:
        return
    match = re.search(r"<title[^>]*>(.*?)</title>", html, re.I | re.S)
    title = match.group(1).strip() if match else "No title"
    print(title[:50] + "..." if len(title) > 50 else title)


def timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        print(f"\n{'=' * 40}")
        print(f"TOTAL EXECUTION TIME: {time.perf_counter() - start:.4f} seconds")
        print(f"{'=' * 40}")
        return result

    return wrapper


def count_primes(start, end):
    total = sum(
        all(x % d for d in range(2, int(x ** 0.5) + 1))
        for x in range(max(2, start), end)
    )
    print(f"Found {total} primes between {start:,} and {end:,}")
    return total
