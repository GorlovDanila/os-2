import os
import sys
import signal


def handle_sigusr1(signum, frame):
    print(f"Produced: {produced}")
    sys.stdout.flush()


pipe1_to_0 = os.pipe()
pipe0_to_2 = os.pipe()
pipe2_to_0 = os.pipe()

signal.signal(signal.SIGUSR1, handle_sigusr1)

p1 = os.fork()
if p1 == 0:
    os.close(pipe1_to_0[0])
    os.dup2(pipe1_to_0[1], sys.stdout.fileno())

    # Запускаем программу producer
    producer_script = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'producer.py')
    os.execve(producer_script, ["producer"], {})

    os._exit(1)

p2 = os.fork()
if p2 == 0:
    os.close(pipe0_to_2[1])
    os.dup2(pipe0_to_2[0], sys.stdin.fileno())
    os.close(pipe2_to_0[0])
    os.dup2(pipe2_to_0[1], sys.stdout.fileno())

    os.execve("/usr/bin/bc", ["bc"], {})

    os._exit(1)


os.close(pipe1_to_0[1])
os.close(pipe0_to_2[0])
os.close(pipe2_to_0[1])

produced = 0

while True:
    arithmetic_expression = os.read(pipe1_to_0[0], 1024).decode("utf-8")
    if not arithmetic_expression:
        break

    os.write(pipe0_to_2[1], arithmetic_expression.encode("utf-8"))

    result = os.read(pipe2_to_0[0], 1024).decode("utf-8")
    print(f"{arithmetic_expression.strip()} = {result.strip()}")
    produced += 1

os.kill(p1, signal.SIGTERM)
os.kill(p2, signal.SIGTERM)
