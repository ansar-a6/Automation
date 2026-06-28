#!/usr/bin/ven python3

def greeting(name):
    space = ' '
    print('Welcome' + space + name + '! to your first automated script')
    print('This code was executed by by ./greetings.py command')

name = str(input('Please enter you name: '))
greeting(name)


# shebands tell the os to run this script through python3.
# chmod +x fileName will save file as executable file.
# ./fileName on termianl will execute the file