# This code creates the todo.txt file for you to test with.
# You can change what gets written to test various scenarios!


def main():
    '''
    This is the main function!
    It handles the command loop logic, and calls the other functions when necessary.
    '''
    command = ''
    while command != 'exit':
        command = input('show, add, remove, or exit? ')
        if command == 'show':
            show_todo_list()
        elif command == 'add':
            task = input('What task needs to be added? ')
            add_to_todo_list(task)
        elif command == 'remove':
            number = int(input('What item number should be removed? '))
            remove_from_todo_list(number)
    print('Goodbye!')


f = open('todo.txt', 'w')
f.write('do laundry\ngo to gym\n')
f.close()

def show_todo_list():

    try:
        with open("todo.txt", 'r') as f:
            content = f.read()
            if content.strip():  # Boşlukları silerek içeriği kontrol eder
                print(content, end='')
            else:
                print("Nothing in the list!")
    except FileNotFoundError:
        print("File not found!")


def add_to_todo_list(item):
    try:
        with open("todo.txt", 'a') as f:
            f.write(item)
            
    except FileNotFoundError:
        print("File not found!")


def remove_from_todo_list(number):
    f = open("todo.txt",'r')
    lines = f.readlines()
    with open("todo.txt", 'w') as f:
            for index, line in enumerate(lines, start=1):
                if index != number:
                    f.write(line)

    

f = open('todo.txt', 'w')
f.write('do laundry\ngo to gym\n')
f.close()
main()

