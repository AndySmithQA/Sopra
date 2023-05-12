import subprocess
import sys

proc = subprocess.run([sys.executable, 'hello.py'],
                      input = b"You got my Message",
                      stdout=subprocess.PIPE,
                      stderr=subprocess.PIPE
                      )

if proc.stderr:
    print("error:", proc.stderr.decode())

print('Output', proc.stdout.decode())

