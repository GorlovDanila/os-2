import os
import sys
import time
import random

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python child.py <S>")
        sys.exit(1)

    sleep_time = int(sys.argv[1])
    pid = os.getpid()
    ppid = os.getppid()
    print(f"Child[{pid}]: I am started. My PID {pid}. Parent PID {ppid}.")
    time.sleep(sleep_time)
    exit_status = random.choice([0, 1])
    print(f"Child[{pid}]: I am ended. PID {pid}. Parent PID {ppid}.")
    sys.exit(exit_status)