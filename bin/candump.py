import subprocess

def run_candump():
    command = ['candump', 'can0']
    subprocess.run(command)

if __name__ == "__main__":
    run_candump()
