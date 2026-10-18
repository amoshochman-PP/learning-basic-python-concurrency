from common import timer, wait


@timer
def loop_wait():
    for i in range(5):
        wait()


loop_wait()
