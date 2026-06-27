import os

print(os.path.exists('directories.py'))


# Different operationg systems has different path

# absolute path: The absolute path of a file/directory.
# relative path: The relative path mostly contains one or two parient directory.

# There are two modules which can be used 'os' and 'pathlib'. The different is os is string bassed and pathlib class based.

# os

print(os.listdir()) # listdir() will list the file and directories contain in the current directory
print(os.cwd()) # cwd() will print the absolute path of current directories
print(os.path.exists('filename.txt')) # exists() will return boolean data type and tell if the file exists or not.
os.mkdir('directoryName') # mdkir() will create a direcotry (folder) in the current directory.
os.chdir('directoryName') #chdir will allow to chanage directory from parent to child.
with open('name.txt','w') as file:
    print('File crated')
    file.write('Welcome to automated lessons')

