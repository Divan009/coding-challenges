import sys
from unix_modes import TerminalMode, is_control, safe_ord
import os

if __name__ == "__main__":
    print("Press keys q quit)…")
    with TerminalMode():
        try:
            while True:
                
                ch = '\0'
                ch = sys.stdin.read(1)
                if ch == "q":
                    sys.exit(1)

                if is_control(ch):
                    # print("this is a control char ", ord(ch), end='', flush=True)
                    print("this is a control char ", safe_ord(ch))
                else:
                    if safe_ord(ch) == -1:
                        print(ch)
                    else:
                        print(f"ASCII: {ch}, {ch} \r\n")

        except KeyboardInterrupt:
            pass
    print("\nTerminal settings restored.")
