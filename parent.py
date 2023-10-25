import os
import sys
import random
import time


def child_process(child_num):

    sleep_time = random.randint(5, 10)
    pid = os.getpid()
    ppid = os.getppid()
    print(f"Child[{child_num}]: I am started. My PID {pid}. Parent PID {ppid}.")
    time.sleep(sleep_time)
    exit_status = random.choice([0, 1])
    print(f"Child[{child_num}]: I am ended. PID {pid}. Parent PID {ppid}.")
    sys.exit(exit_status)


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
            child_process(i)
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
                child_process(child_pid)

    print(f"Parent[{os.getpid()}]: All children have terminated.")