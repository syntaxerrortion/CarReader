import subprocess

def run_cansend():
    canid = input("[*] Send ID: ")

    command = ['cansend', 'can0', canid]

    process = subprocess.Popen(command)
    #xterm_processes.append(process)

    process.wait()


    if process.returncode == 0:
        print("[+] ID sent!")
        while True:
            choice = input("[1] Send again\n[2] Exit\nChoose an option: ")
            if choice == '1':
                run_cansend()
                break
            elif choice == '2':
                print("[*] Exiting...")
                break
            else:
                print("[!] Invalid option. Please choose 1 or 2.")
    else:
        print("[!] There was an error executing the command.")


#xterm_processes = []
run_cansend()
