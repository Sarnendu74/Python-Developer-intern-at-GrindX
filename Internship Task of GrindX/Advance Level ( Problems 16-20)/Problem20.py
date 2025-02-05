# Write a program to simulate the behavior of a stack using lists, including push, pop, and peek operations
class Stack:
    def __init__(self):
        """Initialize an empty stack"""
        self.stack = []

    def push(self, item):
        """Push an item onto the stack"""
        self.stack.append(item)
        print(f"Pushed: {item}")

    def pop(self):
        """Pop an item from the stack"""
        if self.is_empty():
            return "Stack is empty! Cannot pop."
        return f"Popped: {self.stack.pop()}"

    def peek(self):
        """Peek at the top item without removing it"""
        if self.is_empty():
            return "Stack is empty! No top element."
        return f"Top element: {self.stack[-1]}"

    def is_empty(self):
        """Check if the stack is empty"""
        return len(self.stack) == 0

    def display(self):
        """Display the current stack"""
        if self.is_empty():
            return "Stack is empty!"
        return f"Stack (top to bottom): {self.stack[::-1]}"

# Main function with a menu-driven while loop
def main():
    stack = Stack()

    while True:
        print("\n" + "=" * 30)
        print("Stack Operations Menu")
        print("1. Push")
        print("2. Pop")
        print("3. Peek")
        print("4. Display Stack")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            item = input("Enter the item to push: ")
            stack.push(item)
        elif choice == "2":
            print(stack.pop())
        elif choice == "3":
            print(stack.peek())
        elif choice == "4":
            print(stack.display())
        elif choice == "5":
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice! Please enter a number between 1 and 5.")

# Run the main function
if __name__ == "__main__":
    main()
