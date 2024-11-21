import sys
import os
import time
import subprocess

print("[i] Press ctrl-c to exit")
print()
print("[+] Bits sending..")

def loading_bar():
    terminal_width = os.get_terminal_size().columns
    max_bar_length = terminal_width - 1
    progress = 0

    try:
        while True:
            sys.stdout.write("\r" + "#" * progress + " " * (max_bar_length - progress))
            sys.stdout.flush()

            if progress >= max_bar_length:
                sys.stdout.write("\n")
                progress = 0

            time.sleep(0.1)
            progress += 1
    except KeyboardInterrupt:
        sys.stdout.write("\n[!] Exiting...\n")
        sys.exit(0)

def run_cangen():
    command = ["cangen", "can0"]

    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    loading_bar()

    process.wait()

if __name__ == "__main__":
    try:
        run_cangen()
    except KeyboardInterrupt:
        sys.stdout.write("\n[!] Exiting...\n")
        sys.exit(0)
