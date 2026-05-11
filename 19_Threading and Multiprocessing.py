#Threading
#Threading is a way to run multiple tasks concurrently within a single program.
import threading
import time

def task(name):
    print(f"Task {name} starting...")
    time.sleep(2)  # Simulating a long I/O operation
    print(f"Task {name} finished!")

# Create threads
t1 = threading.Thread(target=task, args=("A",))
t2 = threading.Thread(target=task, args=("B",))

# Start them
t1.start()
t2.start()

# Wait for them to finish before continuing
t1.join()
t2.join()

print("All tasks complete.")