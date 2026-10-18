from common import timer, count_primes


@timer
def loop_count_primes():
    for i in range(5):
        count_primes(i * 1_000_000, (i + 1) * 1_000_000)


loop_count_primes()