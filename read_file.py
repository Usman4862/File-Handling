# now i am reading students.txt that will be mandatory to exists

read_file = open('students.txt', mode='r')

data = read_file.read()

print(data)

print('Data readed')

read_file.close()
# now read a file with your desired size
print(30*'*', 'Read File with Size', 30*'*')

size_read_file = open('students.txt', 'r')

sized_data = size_read_file.read(10) # NOTE: this means i need to show only first ten characters

print(sized_data)

print('Sized Data Printed')

size_read_file.close()

# Read Line in the file 
print(30*'*', 'Read Line', 30*'*')

new_file = open('students.txt', 'r')

new_data = new_file.readline()

print(new_data)

new_file.close()


# Read Lines in the file
# this function will print all the lines in the files if empty return None
print(30*'*', 'Read Lines', 30*'*')
file_ = open('students.txt', 'r')
data = file_.readlines() # this will return a list, we need to access each line that's why i use for looop.
for line in data:
    print(line, end='')
file_.close()


