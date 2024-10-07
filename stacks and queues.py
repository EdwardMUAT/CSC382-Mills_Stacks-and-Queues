class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.front = self.rear = None

    def enqueue(self, data):
        new_node = Node(data)
        if self.rear is None:
            self.front = self.rear = new_node
            return
        self.rear.next = new_node
        self.rear = new_node

    def dequeue(self):
        if self.front is None:
            return None
        dequeued_node = self.front
        self.front = dequeued_node.next
        if self.front is None:
            self.rear = None
        return dequeued_node.data

    def is_empty(self):
        return self.front is None

    def display(self):
        temp = self.front
        while temp:
            print(temp.data)
            temp = temp.next

def play_conversation(person1_queue, person2_queue):
    while not person1_queue.is_empty() or not person2_queue.is_empty():
        if not person1_queue.is_empty():
            print(f"Person 1: {person1_queue.dequeue()}")
        if not person2_queue.is_empty():
            print(f"Person 2: {person2_queue.dequeue()}")

def menu():
    person1_queue = Queue()
    person2_queue = Queue()

    # Sample 20 text messages between two people
    person1_messages = [
        "Hey, how are you?", "What's up?", "Did you finish the project?", "Let's meet at 6.", 
        "Do you want to grab coffee?", "I got a new job!", "The weather is amazing today.", 
        "I'll call you later.", "Can you send me the file?", "Thanks for helping me out!"
    ]
    
    person2_messages = [
        "I'm good, how about you?", "Not much, just relaxing.", "Yes, I finished it last night.",
        "Sure, 6 works for me.", "I'd love to!", "Congrats on the new job!", "Yeah, it's great!",
        "Okay, talk to you later.", "I'll send it over now.", "You're welcome!"
    ]

    # Enqueue Person 1's messages into the queue
    for msg in person1_messages:
        person1_queue.enqueue(msg)

    # Enqueue Person 2's messages into the queue
    for msg in person2_messages:
        person2_queue.enqueue(msg)

    while True:
        print("\nMenu:")
        print("1. Display the messages (as stored)")
        print("2. Play the conversation")
        print("3. Exit")
        choice = input("Choose an option (1-3): ")

        if choice == '1':
            print("\nPerson 1's Messages (Queue):")
            person1_queue.display()
            print("\nPerson 2's Messages (Queue):")
            person2_queue.display()
        elif choice == '2':
            print("\nPlaying the conversation:")
            play_conversation(person1_queue, person2_queue)
        elif choice == '3':
            print("Exiting...")
            break
        else:
            print("Invalid option. Please try again.")

# Run the menu
menu()
