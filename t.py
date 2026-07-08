#!/usr/bin/env python

import os

def greeting(name):
    space=' '
    print('Welcome' + space + name + '!' + space + 'to your Linux first Auotmated Script')
    print('This codewas started by ./t.py command.')

def name_check(file_name):
    name=''
    if os.path.exists(file_name):
        with open(file_name) as file:
            name = file.readline().strip()
    else:
        with open(file_name,'w') as file:
            name = input('Please enter your name: ')
            file.write(str(name))
    return str(name)

def main():
    name = name_check('name.txt')
    greeting(name)

if __name__ == '__main__':
    main()
