import time
import sys
print "\n\n\nImports completed successfully.\n\n\nInitializing...\n"

start = 0

while True:
    print("Initializing for " + str(start) + " seconds.")
    start = start + 1
    time.sleep(1)
