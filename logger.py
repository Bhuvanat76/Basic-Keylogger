#!/usr/bin/env python3

import datetime

LOG_FILE = "keylog.txt"

def write_log(text: str) -> None:
    """Append a line with timestamp to the log file."""
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(f"[{timestamp}] {text}\n")

def main() -> None:
    print("=== Terminal Typing Logger Demo ===")
    print("Everything you type here will be saved to keylog.txt")
    print("Type EXIT on a new line to quit.\n")

    while True:
        try:
            user_input = input("> ")
        except (EOFError, KeyboardInterrupt):
            print("\nExiting...")
            break

        if user_input.strip().upper() == "EXIT":
            print("Goodbye! Log saved in keylog.txt")
            break

        write_log(user_input)

if __name__ == "__main__":
    main()
