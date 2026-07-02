#! /usr/bin/env python3
# Author: DCameron
# Version: 1.0
# Description: This script will demo HOWTO match strings/data using
# str testing and pattern matching using the RE module
"""
    DocString
"""
import re
import sys

def search_pattern(pattern=r"^.{19}$", file=r"f:\labs\words"):
    try:
        fh_in = open(file, mode="rt")
    except FileNotFoundError as err:
        print(f"{err.args}, {err.filename}", file=sys.stderr)
        sys.exit(1)
    except PermissionError as err:
        print(f"{err.args}, {err.filename}", file=sys.stderr)
        sys.exit(2)
    except Exception as err:
        print(f"Some other ERROR occurred, Investigate", file=sys.stderr)
        sys.exit(3)
    else:
        # Execute if try block succeeds
        lines = 0
        reobj = re.compile(pattern) # Compile PATTERN only ONCE

        for line in fh_in:
            m = reobj.search(line)  # Match Compiled pattern against line
            if m:
                lines =+ 1
                print(f"Matched {m.group()}")
        fh_in.close()
    finally:
        # Always executes
        print("And now for something completely different")

    return lines

def main():
    print(f"Lines returned = {search_pattern()}")
    num_lines = search_pattern(r"^([A-Z]).*\1$", r"f:\labs\words")
    print(f"Matched {num_lines}")
    return None

# Namespace Trick
if __name__ == "__main__":
    main()
    sys.exit(0)