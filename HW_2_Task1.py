# Data Structures. Homework 2. Task 1.
from queue import Queue
import random

# randomization config
MIN_NEW_REQUESTS = 1
MAX_NEW_REQUESTS = 10

queue = Queue()

class Request:
    request_id = 0

    def __init__(self):
        Request.request_id += 1
        self.id = Request.request_id


def generate_request():
    num_requests = random.randint(MIN_NEW_REQUESTS, MAX_NEW_REQUESTS)
    for _ in range(num_requests):
        queue.put(Request())

def process_request():
    while not queue.empty():
        request = queue.get()
        print(f"Processed request ID {request.id}")
    print("Requests queue is empty.")

def main():
    while True:
        generate_request()
        process_request()

        cont = input("Do you want to continue? (y/n): ")
        if cont.lower() != 'y':
            break

if __name__ == "__main__":
    main()
