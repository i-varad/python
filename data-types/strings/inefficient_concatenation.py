import time

s = ""
start = time.perf_counter()

for i in range(100_000):
    s += "a"   # new string each time

end = time.perf_counter()
print("Length:", len(s))
print("Time with += :", end - start)
