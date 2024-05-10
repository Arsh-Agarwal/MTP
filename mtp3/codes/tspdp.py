from utils import *
import subprocess

def tspdp(edges):
    with open("tspdp\input.txt", "w") as file:
        n = len(edges)
        file.write(f"{n}\n")
        for i in range(n):
            for j in range(n): file.write(f"{edges[i][j]} ")
            file.write("\n")
    
    # Command to run
    command = "tspdp\\a.exe tspdp\\input.txt"
    
    # Run the .exe file and capture its output
    try:
        output = subprocess.check_output(command, stderr=subprocess.STDOUT, shell=True, universal_newlines=True)
        return getintlist(output)
    except subprocess.CalledProcessError as e:
        print("Error occurred:", e)
        return ""