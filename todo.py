
# This is my todo app.

# keep track of todos using a list
todo_list = []

# way to add todos 
def add_todo(todo):
    # We receive a todo which is a string
    todo_list.append(todo)

# print the empty todo list
print(todo_list)
# add a todo by calling our function
add_todo("feed the cat")
# make sure it was added
print(todo_list)

# need to be able to delete todos
def delete_todo(index):
    try:
        todo_list.pop(index)
    except IndexError:
        print("Sorry, no todo at that index.")


# delete_todo(0)

print(todo_list)
# print my todos
for count, todo in enumerate(todo_list, 1):
    print(f"{count}. {todo}")
    
# show user the main menu


