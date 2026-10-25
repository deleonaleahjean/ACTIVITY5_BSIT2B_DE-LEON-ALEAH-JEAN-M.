from stack_implementations import ArrayStack, LinkedStack, OverflowError, UnderflowError
from queue_implementations import ArrayQueue, LinkedQueue, FullQueueError, EmptyQueueError
from applications_exercise import is_balanced, print_queue_simulator

def display_menu():
    print("\n" + "="*45)
    print("   STACKS & QUEUES — MAIN MENU")
    print("="*45)
    print(" 1. Array Stack")
    print(" 2. Linked Stack")
    print(" 3. Circular Array Queue")
    print(" 4. Linked Queue")
    print(" 5. App: Parentheses Checker")
    print(" 6. App: Print Queue Simulator")
    print(" 0. Exit")
    print("="*45)
    return input("Enter choice: ").strip()

def stack_menu(s):
    while True:
        print("\n--- Stack Operations ---")
        print(" p=Push | o=Pop | k=Peek | s=Status | b=Back")
        op = input("Command: ").strip().lower()
        if op == 'p':
            val = input("Value to push: ")
            try:
                s.push(val)
                print(f"Pushed → State: {s}")
            except OverflowError as e:
                print(f"Error: {e}")
        elif op == 'o':
            try:
                print(f"Popped {s.pop()} → State: {s}")
            except UnderflowError as e:
                print(f"Error: {e}")
        elif op == 'k':
            try:
                print(f"Peek: {s.peek()}")
            except UnderflowError as e:
                print(f"Error: {e}")
        elif op == 's':
            full = s.is_full() if hasattr(s, 'is_full') else "N/A"
            print(f"Empty? {s.is_empty()} | Full? {full} | State: {s}")
        elif op == 'b':
            break

def queue_menu(q):
    while True:
        print("\n--- Queue Operations ---")
        print(" e=Enqueue | d=Dequeue | k=PeekFront | s=Status | b=Back")
        op = input("Command: ").strip().lower()
        if op == 'e':
            val = input("Value to enqueue: ")
            try:
                q.enqueue(val)
                print(f"Enqueued → State: {q}")
            except FullQueueError as e:
                print(f"Error: {e}")
        elif op == 'd':
            try:
                print(f"Dequeued {q.dequeue()} → State: {q}")
            except EmptyQueueError as e:
                print(f"Error: {e}")
        elif op == 'k':
            try:
                print(f"Front: {q.peek_front()}")
            except EmptyQueueError as e:
                print(f"Error: {e}")
        elif op == 's':
            print(f"Empty? {q.is_empty()} | Full? {q.is_full()} | State: {q}")
        elif op == 'b':
            break

def main():
    while True:
        c = display_menu()
        if c == '0':
            print("Bye!")
            break
        elif c == '1':
            stack_menu(ArrayStack(int(input("Capacity: "))))
        elif c == '2':
            stack_menu(LinkedStack())
        elif c == '3':
            queue_menu(ArrayQueue(int(input("Capacity: "))))
        elif c == '4':
            queue_menu(LinkedQueue())
        elif c == '5':
            expr = input("Expression: ")
            print("BALANCED" if is_balanced(expr) else "NOT BALANCED")
        elif c == '6':
            print_queue_simulator()

if __name__ == "__main__":
    main()