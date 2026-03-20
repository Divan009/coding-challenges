import time
from collections import deque
import random


def schedule_task(task, delay):
    deadline = time.time() + delay
    sleeping.append((deadline, task))


def optimised_el():
    while ready or sleeping:
        now = time.time()
        sleeping.sort(key=lambda x: x[0])

        if not ready:

            deadline, task = sleeping[0]
            delta = deadline - now

            if delta > 0:  # sleep until its ready
                time.sleep(delta)
            else:
                sleeping.pop()
                ready.append(task)

        # execute task
        while ready:
            task = ready.popleft()
            task()


def unoptimised_el():
    while ready or sleeping:
        if not ready:
            deadline, task = sleeping.pop()
            delta = deadline - time.time()
            if delta > 0:  # check if deadline is over
                time.sleep(delta)

            ready.append(task)

        # execute task
        while ready:
            task = ready.popleft()
            task()


if __name__ == "__main__":
    sleeping = []
    ready = deque()
    random.seed(42)
    total_time = 0

    for _ in range(10):
        delay_s = random.randint(1, 10)
        total_time += delay_s
        schedule_task(lambda: print("Printing after delay"), delay_s)

    start_time = time.time()
    unoptimised_el()
    print("unoptimised", end="\n")
    print(f"total time taken: {time.time() - start_time}")
    print(f"total time expected: {total_time}s")

    total_time = 0
    for _ in range(10):
        delay_s = random.randint(1, 10)
        total_time += delay_s
        schedule_task(lambda: print("Printing after delay"), delay_s)

    print("optimised")
    start_time = time.time()
    optimised_el()
    print(f"total time taken: {time.time() - start_time}")
    print(f"total time expected: {total_time}s")
