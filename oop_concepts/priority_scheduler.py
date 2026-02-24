import heapq

# Create empty heap
tasks = []

# Add tasks
heapq.heappush(tasks, (1, "High Priority Task"))
heapq.heappush(tasks, (3, "Low Priority Task"))
heapq.heappush(tasks, (2, "Medium Priority Task"))

print("Tasks Execution Order:")

while tasks:
    task = heapq.heappop(tasks)
    print(task)