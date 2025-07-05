import sys
import tty
import termios


class TerminalMode:
    """Context manager that sets the terminal to raw mode and restores it."""

    def __enter__(self):
        self.fd = sys.stdin.fileno()
        self.old_settings = termios.tcgetattr(self.fd)

        new_settings = self.old_settings[:]
        iflag_idx = 0
        oflag_idx = 1
        cflag_idx = 2
        lflag_index = 3  # termios.LFLAG is index 3 in the list
        cc = -1

        new_settings[iflag_idx] &= ~(
              termios.IXON
            | termios.ICRNL
            | termios.BRKINT
            | termios.INPCK
            | termios.ISTRIP
        )
        new_settings[oflag_idx] &= ~(termios.OPOST)

        new_settings[cflag_idx] |= termios.CS8

        # Disable ECHO and ICANON and SIGNINT signals and Ctrl+V
        new_settings[lflag_index] &= ~(
            termios.ECHO | termios.ICANON | termios.ISIG | termios.IEXTEN
        )

        new_settings[cc][termios.VMIN] = 0
        new_settings[cc][termios.VTIME] = 1

        # Apply the new settings immediately
        termios.tcsetattr(self.fd, termios.TCSAFLUSH, new_settings)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        termios.tcsetattr(self.fd, termios.TCSAFLUSH, self.old_settings)


def is_control(char) -> bool:
    if not char:
        return False
    return ord(char) < 32 or ord(char) == 127


def safe_ord(ch):
    return ord(ch) if ch else -1
