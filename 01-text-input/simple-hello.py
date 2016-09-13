#!/usr/bin/env python3

# `argv` is short for argument vector. This is a list that contains the
# "words" given on the command line. Since this information comes from
# the operating system it is in the `sys` package.
# The first element (`argv[0]`) is the name of the program,
# elements 1 to the end are the "words" that follow.
from sys import argv

# If there is no argument given, use a default value.
name = "Stranger"

# There is more than one element in `argv` so let's bind `name` to the first one.
if len(argv) > 1:
    name = argv[1]

# Strings can be concatenated with `+` just like in JavaScript
print("Hello, " + name + "!")
