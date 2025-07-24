# A simple to-do list program
def main():
    tasks = []
    
    while True:
        print("Create Task/nView Tasks/nExit")
        choice = input("").lower().strip()

        if choice == "create task":
            todo = input("To Do: ")
            tasks.append(todo)
        elif choice == "view tasks":
            print("You have to do:")
            print(tasks)
        elif choice == "exit":
            break
        else:
            print("Not a valid option. Please try again.")