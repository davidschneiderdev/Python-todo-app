
# This is my todo app.

# keep track of todos using a list
todo_list = []

# print my todos
def print_todos():
    for count, todo in enumerate(todo_list, 1):
        print(f"{count}. {todo}")

# way to add todos 
def add_todo(todo):
    # We receive a todo which is a string
    todo_list.append(todo)

# print the empty todo list

# add a todo by calling our function
add_todo("feed the cat")
add_todo("take out trash")
add_todo("pay bill")
# make sure it was added

# need to be able to delete todos
def delete_todo(index):
    try:
        todo_list.pop(index)
    except IndexError:
        print("Sorry, no todo at that index.")

# show user the main menu
def show_menu():
    print("            ")
    print("   Todo List")
    print("================")
    print("0. quit")
    print("1. print todos")
    print("2. add a todo")
    print("3. complete a todo")

status = True
while status:
    show_menu()
    user_choice = int(input("Choose one: "))
    if user_choice == 0:
        status = False
    elif user_choice == 1:
        print_todos()
    elif user_choice == 2:
        todo_prompt = input("Enter todo: ")
        

    




