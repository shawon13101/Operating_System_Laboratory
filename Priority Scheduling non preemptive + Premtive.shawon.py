n = int(input("Enter number of processes: "))

pid = []
AT = []
BT = []
Priority = []

for i in range(n):
    print("\nProcess", i + 1)

    pid.append(input("P_ID: "))
    AT.append(int(input("Arrival Time: ")))
    BT.append(int(input("Burst Time: ")))
    Priority.append(int(input("Priority: ")))

print("\nNON-PREEMPTIVE PRIORITY")

time = 0
finished = 0
visited = [0] * n

CT = [0] * n
TAT = [0] * n
WT = [0] * n

while finished < n:

    index = -1

    for i in range(n):

        if visited[i] == 0 and AT[i] <= time:

            if index == -1:
                index = i

            elif Priority[i] < Priority[index]:
                index = i

    if index == -1:
        time += 1
        continue

    time = time + BT[index]

    CT[index] = time
    TAT[index] = CT[index] - AT[index]
    WT[index] = TAT[index] - BT[index]

    visited[index] = 1
    finished += 1

print("\nP_ID\tAT\tBT\tPriority\tCT\tTAT\tWT")

sum_tat = 0
sum_wt = 0

for i in range(n):

    print(pid[i], "\t", AT[i], "\t", BT[i], "\t",
          Priority[i], "\t\t", CT[i], "\t", TAT[i], "\t", WT[i])

    sum_tat += TAT[i]
    sum_wt += WT[i]

print("\nAverage TAT =", sum_tat / n)
print("Average WT  =", sum_wt / n)

print("\nPREEMPTIVE PRIORITY")

remaining = BT.copy()
CT = [0] * n
TAT = [0] * n
WT = [0] * n

time = 0
finished = 0

while finished < n:

    index = -1

    for i in range(n):

        if remaining[i] > 0 and AT[i] <= time:

            if index == -1:
                index = i

            elif Priority[i] < Priority[index]:
                index = i

    if index == -1:
        time += 1
        continue

    remaining[index] -= 1
    time += 1

    if remaining[index] == 0:

        CT[index] = time

        TAT[index] = CT[index] - AT[index]

        WT[index] = TAT[index] - BT[index]

        finished += 1


print("\nP_ID\tAT\tBT\tPriority\tCT\tTAT\tWT")

sum_tat = 0
sum_wt = 0

for i in range(n):

    print(pid[i], "\t", AT[i], "\t", BT[i], "\t",
          Priority[i], "\t\t", CT[i], "\t", TAT[i], "\t", WT[i])

    sum_tat += TAT[i]
    sum_wt += WT[i]

print("\nAverage TAT =", sum_tat / n)
print("Average WT  =", sum_wt / n)