import sys

Gf = {}
Gb = {}
for line in sys.stdin:
    l = line.strip().split()
    u = l[1]
    v = l[7]
    if u not in Gf: Gf[u] = set()
    if v not in Gf: Gf[v] = set()
    Gf[u].add(v)

    if u not in Gb: Gb[u] = set()
    if v not in Gb: Gb[v] = set()
    Gb[v].add(u)

# Parameter setting
num_workers = 5

# Set up the data structures
available = set([v for v,d in Gb.items() if not d])
for v in available: del Gb[v]
worker_times = [0]*num_workers
worker_activities = [None]*num_workers
workers_available = set(range(num_workers))

# Start the iteration
t = 0
while Gb or len(workers_available) < num_workers:

    # print("Timestep:", t)
    
    # Find the tasks that are finished at this time
    finished = set()
    for j in range(num_workers):
        if j in workers_available: continue
        if worker_times[j] == t:
            finished.add(worker_activities[j])
            workers_available.add(j)
    # print("Finished:", finished)
    
    # Update the dependency graph and find newly-available tasks
    for a in finished:
        for v in Gf[a]:
            Gb[v].remove(a)
            if not Gb[v]:
                del Gb[v]
                available.add(v)
    # print("Graph:", Gb)
    # print("Tasks available:", available)
    
    # Assign the newly-available tasks
    for a in sorted(available):
        if not workers_available: break
        j = min(workers_available)
        worker_times[j] = t + ord(a) - ord('A') + 61
        worker_activities[j] = a
        workers_available.remove(j)
        available.remove(a)
    
    # Check if we're done
    if len(workers_available) == num_workers:
        break

    # Update the time to the next event
    t = min(worker_times[j] for j in range(num_workers) if j not in workers_available)

# Print the final timestep
print(t)