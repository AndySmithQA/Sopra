import subprocess
import sys

print(sys.executable)

proc = subprocess.run([sys.executable, 'stuff.py'],
                      input = b"You got my message",
                      stdout=subprocess.PIPE,
                      stderr=subprocess.PIPE
                      )

if proc.stderr:
    print(proc.stderr.decode())
print(proc.stdout.decode())

