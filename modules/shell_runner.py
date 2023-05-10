import subprocess

def run(command):
    command = command.split(" ")
    return subprocess.check_output(command)

def run_no_out(command):
    command = command.split(" ")
    return subprocess.run(command)