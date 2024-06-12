#!/usr/bin/env python3

from urllib.parse import urlparse
import sys

# Read text from standard input (pipe)
text = sys.stdin.read()


def is_valid_url(text):
    # Try parsing the URL to check structure
    try:
        parsed = urlparse(text)
        return all([parsed.scheme, parsed.netloc])  # Check scheme and netloc
    except ValueError:
        return False


# Check if the URL is valid
if is_valid_url(text):
    sys.exit(0)  # Exit with code 0 (success)
else:
    sys.exit(1)  # Exit with code 1 (failure)
