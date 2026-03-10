from collections import deque

queue = deque()

queue.append("Andi")
queue.append("Budi")
queue.append("Citra")

print("Antrian:", queue)

queue.popleft()

print("Setelah dilayani:", queue)