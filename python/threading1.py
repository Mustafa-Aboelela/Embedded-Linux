import threading
import time

# Function to be executed by each thread
def thread_function(name, delay):
    print(f"Thread {name} started")
    count = 0
    while count < 5:
        time.sleep(delay)
        count += 1
        print(f"Thread {name}: Count -> {count}")
    print(f"Thread {name} finished")
if __name__ == "__main__":
        
    # Creating threads
    # Arguments: (thread name, delay)
    thread1 = threading.Thread(target=thread_function, args=(1, 1))  
    thread2 = threading.Thread(target=thread_function, args=(2, 2))

    # Starting threads
    thread1.start()
    thread2.start()

    # Waiting for threads to complete
    thread1.join()
    thread2.join()

    print("Main thread finished")
