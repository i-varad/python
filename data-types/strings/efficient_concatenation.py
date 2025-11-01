import time

parts = []
start = time.perf_counter()

for i in range(100_000):
    parts.append("a")   # just appending references, O(1)

s = "".join(parts)      # one allocation, one copy pass

end = time.perf_counter()
print("Length:", len(s))
print("Time with join:", end - start)
