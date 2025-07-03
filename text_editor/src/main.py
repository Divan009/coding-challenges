import sys
import tty
import termios


class TerminalMode:
    """Context manager that sets the terminal to raw mode and restores it."""

    def __enter__(self):
        self.fd = sys.stdin.fileno()
        self.old_settings = termios.tcgetattr(self.fd)

        new_settings = self.old_settings[:]
        lflag_index = 3  # termios.LFLAG is index 3 in the list

        
# this prints only after I press enter
        # new_settings[lflag_index] &= ~termios.ECHO

# this echos it as soon as i type
        # new_settings[lflag_index] &= ~termios.ICANON

        # Disable ECHO and ICANON
        new_settings[lflag_index] &= ~(termios.ECHO | termios.ICANON)
        

        # Apply the new settings immediately
        termios.tcsetattr(self.fd, termios.TCSAFLUSH, new_settings)
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        termios.tcsetattr(self.fd, termios.TCSAFLUSH, self.old_settings)

if __name__ == "__main__":
    print("Press keys (Ctrl-C or Enter to quit)…")
    with TerminalMode():
        try:
            while True:
                ch = sys.stdin.read(1)      # 1 byte at a time, no buffering
                if ch in ("\n", "\r", "\x03"):  # Enter or Ctrl-C
                    break
                print(f"Got byte: {repr(ch)}")
        except KeyboardInterrupt:
            pass
    print("\nTerminal settings restored.")
