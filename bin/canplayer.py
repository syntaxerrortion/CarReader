import subprocess

def run_canplayer():
    logfile = input("[*] Log file to play: ")
    numstart = input("[*] Playback value: ")

    command = ['canplayer', 'can0', logfile, '-v', '-l', numstart]

    process = subprocess.Popen(command)
    #xterm_processes.append(process)

    process.wait()


    if process.returncode == 0:
        print("[+] Command executed successfully.")
        while True:
            choice = input("[1] Run again\n[2] Exit\nChoose an option: ")
            if choice == '1':
                run_canplayer()
                break
            elif choice == '2':
                print("[*] Exiting...")
                break
            else:
                print("[!] Invalid option. Please choose 1 or 2.")
    else:
        print("[!] There was an error executing the command.")


#xterm_processes = []
run_canplayer()
