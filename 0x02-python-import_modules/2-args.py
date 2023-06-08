#!/usr/bin/python3
import sys
n = 2
if len(sys.argv) == 1:
    print("0 arguments.")
elif len(sys.argv) == 2:
    print("1 argument:")
    print(f"1: {sys.argv[1]}")
else:
    print(f"{len(sys.argv)} arguments")
    while n <= len(sys.argv): 
        print(f"{n-1}: {sys.argv[n-1]}")
        n += 1
