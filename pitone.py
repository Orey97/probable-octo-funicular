# ...existing code...
"""
Simple terminal utility.
Choose an action from the menu: greet, fibonacci, list files, show time, or exit.
"""
import os
import getpass
from datetime import datetime
from typing import List


def greet() -> None:
    user = getpass.getuser()
    print(f"Hello, {user}! This is a tiny Python utility.\n")


def fibonacci(n: int) -> List[int]:
    if n <= 0:
        return []
    seq = [0]
    if n == 1:
        return seq
    seq.append(1)
    while len(seq) < n:
        seq.append(seq[-1] + seq[-2])
    return seq


def list_files() -> None:
    entries = os.listdir(".")
    if not entries:
        print("No files or folders in the current directory.\n")
        return
    print("Files and folders in current directory:")
    for name in sorted(entries):
        try:
            size = os.path.getsize(name)
            print(f" - {name} ({size} bytes)")
        except OSError:
            print(f" - {name} (size unknown)")
    print()


def show_time() -> None:
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"Current time: {now}\n")


def main() -> None:
    actions = {
        "1": ("Greet me", greet),
        "2": ("Fibonacci sequence", None),
        "3": ("List files in current directory", list_files),
        "4": ("Show current time", show_time),
        "5": ("Exit", None),
    }

    while True:
        print("Choose an action:")
        for k, (desc, _) in actions.items():
            print(f" {k}) {desc}")
        choice = input("Enter choice [1-5]: ").strip()

        if choice == "1":
            greet()
        elif choice == "2":
            try:
                n = int(input("How many Fibonacci numbers? ").strip())
            except ValueError:
                print("Please enter a valid integer.\n")
                continue
            seq = fibonacci(n)
            print("Fibonacci:", ", ".join(str(x) for x in seq) + "\n")
        elif choice == "3":
            list_files()
        elif choice == "4":
            show_time()
        elif choice == "5":
            print("Goodbye.")
            break
        else:
            print("Invalid choice. Try again.\n")


if __name__ == "__main__":
    main()
