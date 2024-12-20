import sys

events = []
for line in sys.stdin:
    ts, event = line.strip().lstrip('[').split('] ')
    date,time = ts.split()
    date = tuple(map(int,date.split('-')))
    time = tuple(map(int,time.split(':')))
    events.append((date + time, event))

events.sort()

guard_id = None
mins_asleep = {}
for ts, event in events:
    if event.startswith('Guard'):
        guard_id = int(event.split()[1][1:])
    elif event == 'falls asleep':
        assert ts[-2] == 0
        fall_asleep_minute = ts[-1]
    elif event == 'wakes up':
        assert ts[-2] == 0
        wake_up_minute = ts[-1]
        if guard_id not in mins_asleep: mins_asleep[guard_id] = []
        mins_asleep[guard_id].append((fall_asleep_minute, wake_up_minute))

guard_id, mins = max(mins_asleep.items(), key = lambda x : sum(y[1] - y[0] for y in x[1]))

maxm = None
maxctr = 0
for m in range(60):
    ctr = 0
    for l,u in mins:
        if l <= m < u:
            ctr += 1
    if ctr > maxctr:
        maxctr = ctr
        maxm = m
print(maxm * guard_id)