import os
import subprocess
import sys
import platform
import can
from colorama import Fore, Style, init
from pyfiglet import figlet_format

init(autoreset=True)

xterm_processes = []


def execute_command(command):
    try:
        result = subprocess.run(command, capture_output=True, text=True)
        return result.returncode, result.stdout, result.stderr
    except Exception as e:
        return 1, "", str(e)


def main():
    while True:
        os.system("clear" if os.name != "nt" else "cls")
        print(f"{Fore.WHITE}{Style.BRIGHT}{figlet_format('  CarReader')}")
        print(f"{Fore.WHITE}{Style.BRIGHT}                                              Created by Syntax")

        print()
        print(f"{Fore.WHITE}{Style.BRIGHT}      [1] Car data read and dump (cansniffer,candump)")
        print(f"{Fore.WHITE}{Style.BRIGHT}      [2] Data play (canplay)")
        print(f"{Fore.WHITE}{Style.BRIGHT}      [3] Data send (cansend)")
        print(f"{Fore.WHITE}{Style.BRIGHT}      [4] Random send data (cangen)")
        print()
        print(f"{Fore.WHITE}{Style.BRIGHT}\n         [98] adapter configure(root)   [99] exit")
        print()

        choice = input(f"{Fore.WHITE}{Style.BRIGHT} [*] selection: ")


        if choice == '1':
            command1 = ['xterm', '-geometry', '130x56', '-e', 'python3', 'bin/cansniffer.py']
            process1 = subprocess.Popen(command1, stderr=subprocess.DEVNULL)

            command2 = ['xterm', '-geometry', '130x56', '-e', 'python3', 'bin/candump.py']
            process2 = subprocess.Popen(command2, stderr=subprocess.DEVNULL)

            xterm_processes.append(process1)
            xterm_processes.append(process2)


        elif choice == '2':
            command = ['xterm', '-geometry', '130x15', '-e', 'python3', 'bin/canplayer.py']
            process = subprocess.Popen(command, stderr=subprocess.DEVNULL)
            xterm_processes.append(process)


        elif choice == '3':
            command = ['xterm', '-geometry', '130x10', '-e', 'python3', 'bin/cansend.py']
            process = subprocess.Popen(command, stderr=subprocess.DEVNULL)
            xterm_processes.append(process)


        elif choice == '4':
            command = ['xterm', '-geometry', '130x15', '-e', 'python3', 'bin/cangen.py']
            process = subprocess.Popen(command, stderr=subprocess.DEVNULL)
            xterm_processes.append(process)


        elif choice == '98':
            command = ['xterm', '-geometry', '130x56', '-e', 'sudo', 'bash', 'bin/obd2configure.sh']
            process = subprocess.Popen(command)
            xterm_processes.append(process)



        elif choice == '99':
            print(f"{Fore.RED}{Style.BRIGHT}[!] Exiting..")
            for process in xterm_processes:
                process.terminate()
            break
        else:
            print(f"{Fore.RED} [-] Invalid selection!")



try:
    main()
except KeyboardInterrupt:
    print(f"{Fore.RED}{Style.BRIGHT}\n[!] ctrl-c detected! exiting..")
    for process in xterm_processes:
        try:
            process.terminate()
        except Exception as e:
            print(f"[!] Error terminating process: {e}")
    sys.exit()
