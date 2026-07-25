import numpy as np

# Parameters
filename = "keyfob_pulses.dat"
sample_rate = 500000  # Hz (must match your GNU Radio flowgraph)
threshold = 0.5

# Read float32 samples
x = np.fromfile(filename, dtype=np.float32)

# Convert to binary
bits = (x > threshold).astype(np.uint8)

# Remove consecutive duplicates and measure pulse lengths
runs = []
current = bits[0]
length = 1

for b in bits[1:]:
    if b == current:
        length += 1
    else:
        runs.append((current, length))
        current = b
        length = 1
runs.append((current, length))

print("Pulse runs:")
for level, n in runs:
    print(level, n, f"{n/sample_rate*1e6:.0f} us")
