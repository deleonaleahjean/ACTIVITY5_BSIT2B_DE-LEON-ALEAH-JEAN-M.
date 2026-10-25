from stack_implementations import LinkedStack
from queue_implementations import LinkedQueue

def is_balanced(expression):
    stack = LinkedStack()
    matches = {')': '(', ']': '[', '}': '{'}
    for char in expression:
        if char in matches.values():
            stack.push(char)
        elif char in matches:
            if stack.is_empty() or stack.pop() != matches[char]:
                return False
    return stack.is_empty()

def print_queue_simulator():
    pq = LinkedQueue()
    print("\n===== PRINT QUEUE SIMULATOR =====")
    while True:
        print("\nCommands: a=Add Job | p=Process Next | l=List | q=Quit")
        cmd = input("Enter command: ").strip().lower()
        if cmd == 'a':
            job_id = input("Job ID: ").strip()
            pages = input("Number of pages: ").strip()
            job = f"Job {job_id} ({pages} pages)"
            pq.enqueue(job)
            print(f"Added: {job} | Queue: {pq}")
        elif cmd == 'p':
            if pq.is_empty():
                print("Queue is empty — no jobs to process")
            else:
                job = pq.dequeue()
                print(f"Printing: {job}")
        elif cmd == 'l':
            if pq.is_empty():
                print("Queue is empty")
            else:
                print(f"Pending jobs: {pq}")
        elif cmd == 'q':
            print("Exiting simulator...")
            break

if __name__ == "__main__":
    print("=== Parentheses Checker ===")
    expr = input("Enter expression: ")
    print("BALANCED" if is_balanced(expr) else "NOT BALANCED")
    print_queue_simulator()