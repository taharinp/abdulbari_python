import priority_scheduler

# Create empty heap
tasks = []

# Adding tasks (priority, taskname)
heapq.heappush(tasks, (1, "High Priority Task"))
heapq.heappush(tasks, (3, "Low Priority Task"))
heapq.heappush(tasks, (2, "Medium Priority Task"))

print("Tasks Execution Order:")

# Removing tasks by priority
while tasks:
    task = heapq.heappop(tasks)
    print(task)