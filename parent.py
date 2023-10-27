#!/usr/bin/python3
import os
import sys
import random


def child_process():
    sleep_time = random.randint(5, 10)
    child_script = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'child.py')
    args = [child_script, str(sleep_time)]
    os.execve(child_script, args, os.environ)
    print("Child process failed to execute child.py")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python parent.py <N>")
        sys.exit(1)

    N = int(sys.argv[1])
    print(f"Parent[{os.getpid()}]: I ran children processes.")

    child_processes = []
    for i in range(1, N + 1):
        pid = os.fork()
        if pid == 0:
            child_process()
        else:
            child_processes.append(pid)

    for child_pid in child_processes:
        _, status = os.waitpid(child_pid, 0)
        if os.WIFEXITED(status):
            exit_status = os.WEXITSTATUS(status)
            print(f"Parent[{os.getpid()}]: Child with PID {child_pid} terminated. Exit Status {exit_status}")
        else:
            print(f"Parent[{os.getpid()}]: Child with PID {child_pid} terminated. Restarting.")
            new_pid = os.fork()
            if new_pid == 0:
                child_process()

    print(f"Parent[{os.getpid()}]: All children have terminated.")
