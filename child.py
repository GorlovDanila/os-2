#!/usr/bin/python3
import os
import sys
import time
import random

child_pid = os.getpid()
parent_pid = os.getppid()

print(f'Child[{child_pid}]: I am started. My PID {child_pid}. Parent PID {parent_pid}')

sleep_time = int(sys.argv[1])
time.sleep(sleep_time)

print(f'Child[{child_pid}]: I am ended. My PID {child_pid}. Parent PID {parent_pid}')
exit_status = random.choice([0, 1])
os._exit(exit_status)