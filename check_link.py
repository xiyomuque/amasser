#!/usr/bin/env python3

import sys
from validators import url


def main():
    # Read text from standard input (pipe)
    text = sys.stdin.read().strip()
    if url(text):
        sys.exit(0)
    else:
        sys.exit(1)


main()
