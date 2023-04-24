# NOTE: 'with' statement is used while opening a file, there is no need to close file when you are using 'with' statement

with open('students.txt') as L:
    data = L.read()
    print(data)

print('File closed:', L.closed)
