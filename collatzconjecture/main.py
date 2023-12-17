from cc import collatz_conjecture
import matplotlib.pyplot as plt
import sys

if len(sys.argv) != 2:
    raise ValueError("Usage: python3 main.py <int>")

#contstructing the plot
seq = collatz_conjecture(int(sys.argv[1]))
plt.plot([x+1 for x in range(len(seq))], seq)
plt.axis((1, len(seq), 0, max(seq)))
plt.ylabel("value")
plt.xlabel("step")

#some information about the sequence
print(f"Highest value in the sequence: {max(seq)}")
print(f"Number of steps: {len(seq)-1}")

plt.show()