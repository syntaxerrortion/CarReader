import subprocess

def run_cansniffer():
    command = ['cansniffer', 'can0']
    subprocess.run(command)

if __name__ == "__main__":
    run_cansniffer()
