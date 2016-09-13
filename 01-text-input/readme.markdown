# Getting text from the user

The files in this directory correspond to the video [1.3 Getting Text from User](https://youtu.be/uNQSVU0IKec?list=PLRqwX-V7Uu6YrbSJBg32eTzUU50E2B8Ch).

Since I will be using the command line instead of a web page I will cover a few different options for getting user input.

One of the reasons I do not use a web page is composability: The UNIX command line makes it possible to chain all kinds of
programs together which seems to open some interesting possibilities when working with text. This is why I will not cover
interactive input here.

## Simple argument

Sometimes all you need is one simple string, nothing else. The script `simple-hello.py` shows how read a single argument
from the command supplied when the script is called.

    python3 simple-hello.py Christian

Will print

    Hello Christian!

