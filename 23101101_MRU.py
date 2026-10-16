n = int(input("Enter reference string length: "))
ref = list(map(int, input("Enter reference string: ").split()))
f = int(input("Enter frame size: "))
frame = []
pageFault = 0
pageHit = 0
recent = {}
print("\nPage\tFrames\t\tStatus\tAction")
for i, page in enumerate(ref):
    if page in frame:
        pageHit += 1
        status = "HIT"
        action = "No replacement"
        recent[page] = i
    else:
        pageFault += 1
        if len(frame) < f:
            frame.append(page)
            action = f"Added {page}"
        else:
            # Find the most recently used page
            mruPage = max(frame, key=lambda p: recent[p])

            frame[frame.index(mruPage)] = page
            del recent[mruPage]
            action = f"Removed {mruPage}, Added {page}"
        status = "FAULT"
        recent[page] = i
    frames = frame + ["-"] * (f - len(frame))
    print(f"{page}\t{frames}\t{status}\t{action}")

print("\nTotal Page Faults =", pageFault)
print("Total Page Hits =", pageHit)
print("Page Fault Ratio =", pageFault, "/", len(ref),
      "=", round(pageFault / len(ref), 2))
print("Page Hit Ratio =", pageHit, "/", len(ref),
      "=", round(pageHit / len(ref), 2))