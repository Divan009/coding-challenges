import termios, tty, sys

def enable_raw_mode(fd):
    tty.setraw(fd)
    # values = termios.tcgetattr(fd)
    # values.cc
    # print(values)

    ...