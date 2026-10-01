count = int(input("Enter number of requests: "))

requests = list(map(int, input("Enter request sequence: ").split()))

current = int(input("Enter initial head position: "))

seek = 0
order = []

while len(requests) > 0:
    closest = min(requests, key=lambda r: abs(r - current))
    movement = abs(current - closest)

    seek += movement
    order.append(closest)
    current = closest

    requests.remove(closest)

print("\nSeek Sequence:", order)
print("Total Seek Time:", seek)