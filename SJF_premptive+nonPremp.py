n = int(input("Enter number of processes: "))

p = []

for i in range(n):
    name = input("Process: ")
    at = int(input("Arrival Time: "))
    bt = int(input("Burst Time: "))
    p.append([name, at, bt])

p.sort(key=lambda x: x[1])

time = 0
completed = []
sequence = []

while len(completed) < n:

    ready = []

    for x in p:
        found = False

        for c in completed:
            if c[0] == x[0]:
                found = True
                break

        if not found and x[1] <= time:
            ready.append(x)

    if len(ready) == 0:
        time = time + 1
        continue

    ready.sort(key=lambda x: x[2])

    current = ready[0]

    name = current[0]
    at = current[1]
    bt = current[2]

    time = time + bt
    ct = time

    tat = ct - at
    wt = tat - bt

    completed.append([name, at, bt, ct, tat, wt])
    sequence.append(name)


print("Execution Sequence:", " ".join(sequence))

print("\nP\tAT\tBT\tCT\tTAT\tWT")

for x in sorted(completed, key=lambda x: x[0]):
    print(
        x[0], "\t",
        x[1], "\t",
        x[2], "\t",
        x[3], "\t",
        x[4], "\t",
        x[5]
    )

np_total_tat = 0
np_total_wt = 0

for x in completed:
    np_total_tat = np_total_tat + x[4]
    np_total_wt = np_total_wt + x[5]

np_avg_tat = np_total_tat / n
np_avg_wt = np_total_wt / n

print("\nTotal TAT =", np_total_tat)
print("Total WT  =", np_total_wt)

print("Average TAT =", np_avg_tat)
print("Average WT =", np_avg_wt)

remaining = []

for x in p:
    remaining.append([x[0], x[1], x[2], x[2], 0])

time = 0
finished = 0
sequence = []

while finished < n:

    ready = []

    for x in remaining:
        if x[1] <= time and x[3] > 0:
            ready.append(x)

    if len(ready) == 0:
        time = time + 1
        continue

    ready.sort(key=lambda x: x[3])

    current = ready[0]

    if len(sequence) == 0 or sequence[-1] != current[0]:
        sequence.append(current[0])

    current[3] = current[3] - 1
    time = time + 1

    if current[3] == 0:
        current[4] = time
        finished = finished + 1

pre_completed = []

for x in remaining:

    name = x[0]
    at = x[1]
    bt = x[2]
    ct = x[4]

    tat = ct - at
    wt = tat - bt

    pre_completed.append([
        name, at, bt, ct, tat, wt
    ])

print("Execution Sequence:", " ".join(sequence))

print("\nP\tAT\tBT\tCT\tTAT\tWT")

for x in sorted(pre_completed, key=lambda x: x[0]):
    print(
        x[0], "\t",
        x[1], "\t",
        x[2], "\t",
        x[3], "\t",
        x[4], "\t",
        x[5]
    )

pre_total_tat = 0
pre_total_wt = 0

for x in pre_completed:
    pre_total_tat = pre_total_tat + x[4]
    pre_total_wt = pre_total_wt + x[5]

pre_avg_tat = pre_total_tat / n
pre_avg_wt = pre_total_wt / n

print("\nTotal TAT =", pre_total_tat)
print("Total WT  =", pre_total_wt)

print("Average TAT =", pre_avg_tat)
print("Average WT =", pre_avg_wt)

print("\nAverage Waiting Time:")
print("Non-Preemptive SJF = {:.2f}".format(np_avg_wt))
print("Preemptive SJF     = {:.2f}".format(pre_avg_wt))

print("\nAverage Turnaround Time:")
print("Non-Preemptive SJF = {:.2f}".format(np_avg_tat))
print("Preemptive SJF     = {:.2f}".format(pre_avg_tat))