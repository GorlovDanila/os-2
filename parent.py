#!/usr/bin/python3
import os
import sys
import random


def child_process():
    child = os.fork()
    if child == 0:
        # Executes by child
        sleep_time = random.randint(5, 10)
        os.execve('/usr/bin/python3', ['/usr/bin/python3', 'child.py', str(sleep_time)], os.environ)
    else:
        # Executes by parent
        print(f'Parent[{os.getpid()}]: I ran children process with PID {child}')


n = int(sys.argv[1])

for _ in range(n):
    child_process()

counter = 0

while counter != n:
    child_pid, exit_status = os.wait()
    print(f'Parent[{os.getpid()}]: Child with PID {child_pid} terminated. Exit status {os.WEXITSTATUS(exit_status)}')

    if exit_status != 0:
        child_process()
    else:
        counter += 1

os._exit(0)