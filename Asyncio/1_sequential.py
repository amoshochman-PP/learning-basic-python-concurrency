import time

from common import timer


@timer
def loop_wait():
    for i in range(5):
        time.sleep(1)
        print(f"Slept 1 sec")


loop_wait()
