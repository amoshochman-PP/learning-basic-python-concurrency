from common import timer, count_primes, LOOPS_NUM


@timer
def loop_count_primes():
    for i in range(LOOPS_NUM):
        count_primes(i * 1_000_000, (i + 1) * 1_000_000)


loop_count_primes()