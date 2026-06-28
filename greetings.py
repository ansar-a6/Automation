#!/usr/bin/ven python3

import os

def greeting(name):
    space = ' '
    print('Welcome' + space + name + '! to your first automated script')
    print('This code was executed by by ./greetings.py command')

def name_chk(file_name):
    if os.path.exists(file_name):
        name = ''
        with open(file_name) as file:
            name = file.readline()
    else:
        with open(file_name, 'w') as file:
            name = str(input('Please enter your name: '))
            file.write(name)
        return name
def main():
    name = name_chk('name.txt')
    greeting(str(name))
    return

if __name__ == '__main__':
    main()

# shebands tell the os to run this script through python3.
# chmod +x fileName will save file as executable file.
# ./fileName on termianl will execute the file