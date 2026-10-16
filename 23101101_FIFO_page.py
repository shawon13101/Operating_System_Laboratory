n = int(input("Enter reference string length: "))
ref = list(map(int, input("Enter reference string: ").split()))
f = int(input("Enter frame size: "))

frame = []
pageFault = 0
pageHit = 0
next = 0

print("\nPage\tFrames\t\tStatus\tAction")

for page in ref:
    if page in frame:
        pageHit += 1
        status = "HIT"
        action = "No replacement"

    else:
        pageFault += 1

        if len(frame) < f:
            frame.append(page)
            action = f"Added {page}"
        else:
            removed = frame[next]
            frame[next] = page
            action = f"Removed {removed}, Added {page}"
            next = (next + 1) % f

        status = "FAULT"

    frames = frame + ["-"] * (f - len(frame))

    print(f"{page}\t{frames}\t{status}\t{action}")

print("\nTotal Page Faults =", pageFault)
print("Total Page Hits =", pageHit)

print("Page Fault Ratio =", pageFault, "/", len(ref),
      "=", round(pageFault / len(ref), 2))

print("Page Hit Ratio =", pageHit, "/", len(ref),
      "=", round(pageHit / len(ref), 2))