from collections import deque

tasks = deque()


# # Cant execute concurrently
# def countup(n):
#     for i in range(n):
#         print(f"Printing up {i}")


# def countdown(n):
#     for i in range(n):
#         print(f"Printing down {n - i}")


# Can execute concurrently
def countup(n):
    if n > 10:
        return
    print(f"Printing up {n}")
    tasks.append(lambda n=n: countup(n + 1))


def countdown(n):
    def _run(i):
        if i <= 0:
            return

        print(f"Printing down {i}")
        tasks.append(lambda i=i: _run(i - 1))

    _run(n)


tasks.append(lambda: countup(5))
tasks.append(lambda: countdown(5))


# tasks.append(task1)
# tasks.append(task2)


if __name__ == "__main__":
    # At its core, the Event Loop is a while loop that iterates
    # through the tasks (queue) and executes them.

    while tasks:
        tsk = tasks.popleft()
        tsk()
