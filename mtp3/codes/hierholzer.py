import subprocess

def mod_input(x):
    ans = {}
    for a in x:
        if a[0] not in ans: ans[a[0]] = []
        if a[1] not in ans: ans[a[1]] = []
        ans[a[0]].append(a[1])
        ans[a[1]].append(a[0])
    return ans
    
def hierholzer(adj):
    adj = mod_input(adj)
    edge_count = {}
    for node, neigh in adj.items():
        edge_count[node] = len(neigh)
    if len(adj) == 0: return []
    
    curr_path = []
    circuit = []
    
    start = list(adj.keys())[0]
    curr_path.append(start)
    curr_v = start

    while len(curr_path):
        if edge_count[curr_v]:
            curr_path.append(curr_v)
            next_v = adj[curr_v][-1]
            
            edge_count[curr_v] -= 1
            edge_count[next_v] -= 1
            adj[curr_v].pop()
            adj[next_v].remove(curr_v)
            curr_v = next_v

        else:
            circuit.append(curr_v)
            curr_v = curr_path[-1]
            curr_path.pop()

    return circuit[:-1]
    