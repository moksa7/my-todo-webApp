FILEPATH = 'todos.txt'

def getTodos(filepath=FILEPATH):
    """ Read a text file and return the list of to-do items """
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return  todos_local


def writeTodos(target, filepath=FILEPATH):
    """ Write the to-do item list in the text file."""
    with open(filepath, "w") as file:
        file.writelines(target)


print(__name__)
if __name__ == "__main__":
    print("Hello!")
    print(help(getTodos))