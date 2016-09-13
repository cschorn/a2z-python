#!/usr/bin/env python3

# The standard input is something else the OS provides for us.
# We can use it just like any other file as long as we just read from it,
# one thing after another.
from sys import stdin

# A `list` is a built-in data structure and `list()` is its constructor function.
# This function takes as an argument anything a list can be build out of, in
# this case something like a file.
# (Ed: Is this sufficiently vague?)
# Anyway, we will end up with a list of all the lines that can be read from
# `sys.stdin`.
lines = list(stdin)

# `reversedi()` takes anything that is like a list and reverses it.
# (Actually it returns a generator but that is not important right now.)
# So `reversed_lines` will give us `lines` in reversed order. Wow!
reversed_lines = reversed(lines)

# Output every item in `reversed_lines`.
# The `end=''` part tells `print()` not to add a newline after printing since
# the newlines are still attached to the strings.
for line in reversed_lines:
    print(line, end='')
