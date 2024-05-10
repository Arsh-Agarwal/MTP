import subprocess
from utils import *
import heapq as hp

def mwpf():
    temp = readgraph()
    n, m = temp[0], temp[1]
    pq = []
    for i in range(2, len(temp), 3): hp.heappush(pq, (temp[i+2], [temp[i], temp[i+1]]))
    done = {}
    ans = []
    while pq:
        wt, a = hp.heappop(pq)
        x, y = a[0], a[1]
        if x not in done and y not in done:
            done[x] = 1
            done[y] = 1
            ans.append([x, y])

    return ans

# def mwpf():
#     # Command to run
#     command = "blossom\example.exe -f blossom\input.txt --minweight"
    
#     # Run the .exe file and capture its output
#     try:
#         output = subprocess.check_output(command, stderr=subprocess.STDOUT, shell=True, universal_newlines=True)
#         return output
#     except subprocess.CalledProcessError as e:
#         print("Error occurred:", e)
#         return ""