
# This is my todo app.

# keep track of todos using a list
todo_list = []

# print my todos
def print_todos():
    if len(todo_list) == 0:
        print("You have nothing to do!")
    else:
        for count, todo in enumerate(todo_list):
            print(f"{count}: {todo}")

# way to add todos 
def add_todo(todo_prompt):
    # We receive a todo which is a string
    todo_list.append(todo_prompt)

# print the empty todo list

# add a todo by calling our function

# make sure it was added

# need to be able to delete todos
def delete_todo(index):
    try:
        todo_list.pop(index)
    except IndexError:
        print("Sorry, no todo at that index.")

# show user the main menu
def main():
    menu = """
                    
    Todo List
================
0. quit
1. print todos
2. add a todo
3. complete a todo
                    
"""
    is_running = True
    while is_running:
        print(menu)
        choice = input("Choose one: ")
        if choice == "0":
            is_running = False
            print("Thank you for using the todo app.")
        elif choice == "1":
            print_todos()
        elif choice == "2":
            todo_prompt = input("Enter todo: ")
            add_todo(todo_prompt)
        elif choice == "3":
            index_to_complete = int(input("Complete which todo? "))
            delete_todo(index_to_complete)
        else:
            print("Please enter a number for your choice.")

main()




    




