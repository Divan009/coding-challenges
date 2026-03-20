import time
from collections import deque
import random

sleeping = []
ready = deque()


def schedule_task(task, delay):
    deadline = time.time() + delay
    sleeping.append((deadline, task))


total_time = 0
for _ in range(10):
    delay_s = random.randint(1, 10)
    total_time += delay_s
    schedule_task(lambda: print("Printing after delay"), 5)


start_time = time.time()

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

print(f"total time taken: {time.time() - start_time}")
print(f"total time expected: {total_time}s")
