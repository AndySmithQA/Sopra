import warnings
import sys

warnings.warn("Oops\n")
something_nasty = True
if something_nasty:
    sys.stderr.write("There was a problem")
    exit(1)

