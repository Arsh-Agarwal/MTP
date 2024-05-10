import pickle
import string
import random
import math
import re
import time

def rand_str(length=30):
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(length))

def save(data, config, name = ""):
    if name == "": name = rand_str()
    with open(name + ".dat", "wb") as f:
        pickle.dump(data, f)
    with open(name + "_cfg.dat", "wb") as f:
        pickle.dump(config, f)

def load(name = "bin.dat"):
    X = None
    try:
        with open(name, 'rb') as f:
            X = pickle.load(f)
    except Exception as e:
        X = []
        print(f"error loading file {name}", e)
    return X

def dist(x1, y1, x2, y2):
    return math.sqrt((x1-x2)**2 + (y1-y2)**2)

def pdist(a, b):
    return dist(a.x, a.y, b.x, b.y)

def readgraph():
    name = "blossom\input.txt"
    ans = []
    with open(name, 'r') as file:
        lines = file.readlines()
        for line in lines:
            nums = line.split()
            temp = list(map(float, nums))
            if len(ans) >= 2:
                temp[0] = int(temp[0])
                temp[1] = int(temp[1])
            else:
                for i in range(len(temp)): temp[i] = int(temp[i])
            ans.extend(temp)
    return ans        

def cyclelist(x, start = 0, rev = False):
    ans = []
    n = len(x)
    for i in range(n): ans.append(x[(i+start+1)%n])
    if rev: ans.reverse()
    return ans

def getintlist(string):
    pattern = r'\b\d+\b'

    # Find all matches of integers in the string
    integers = re.findall(pattern, string)

    # Convert the matched strings to integers
    integers = [int(num) for num in integers]
    return integers

def pathlen(a):
    totdist = 0
    for i in range(len(a)-1): totdist += pdist(a[i], a[i+1])
    return totdist

def curtime():
    return round(time.time() * 1000)