import threading
from common import timer, count_primes, LOOPS_NUM


@timer
def loop_count_primes():
    threads = []

    for i in range(LOOPS_NUM):
        thread = threading.Thread(target=count_primes, args=(i * 1_000_000, (i + 1) * 1_000_000))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()


loop_count_primes()
