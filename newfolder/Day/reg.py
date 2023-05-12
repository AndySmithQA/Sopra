import re

line = "The quick brown fox jumps over the lazy dog"

m = re.search(r"(quick)", line)

if m:
    print("Matched at:", m.start())