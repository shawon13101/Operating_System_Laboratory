n = int(input("enter_num_pro: "))

p = []

for i in range(n):
    name = input("Pro: ")
    at = int(input("AT: "))
    bt = int(input("BT: "))
    p.append([name, at, bt])

p.sort(key=lambda x: x[1])

time = 0
total_wt = 0
total_tat = 0

print("\nP\tAT\tBT\tCT\tWT\tTAT")

for i in p:
    if time < i[1]:
        time = i[1]

    ct = time + i[2]
    tat = ct - i[1]
    wt = tat - i[2]

    total_wt += wt
    total_tat += tat

    print(i[0], "\t", i[1], "\t", i[2], "\t", ct, "\t", wt, "\t", tat)

    time = ct

print("\nTTT =", total_tat)
print("AWT =", total_wt / n)
print("ATT =", total_tat / n)