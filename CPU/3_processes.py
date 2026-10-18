import multiprocessing
from common import timer, count_primes


@timer
def loop_count_primes():
    processes = []

    for i in range(3):
        process = multiprocessing.Process(target=count_primes, args=(i * 1_000_000, (i + 1) * 1_000_000))
        processes.append(process)
        process.start()

    for process in processes:
        process.join()


if __name__ == "__main__":
    loop_count_primes()
