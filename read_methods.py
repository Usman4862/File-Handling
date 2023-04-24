"""
NOTE: 
    There are two methods for reading file in python, i-e SEEK and TELL
    TELL Method:
        is used to find the exact postion of the pointer or blinking cursor in the file.
    SEEK Method:
        is used to move the position of the blinking cursor in the file.

"""

# TELL METHOD:
print(30*'*', 'Tell Method', 30*'*')
f = open('students.txt', 'r')
print('Pointer Older Position', f.tell()) # this will tell the position of the blinking cursor 
content = f.read(5)
print(content)
print('Pointer New Position', f.tell())
f.close()

# SEEK METHOD:
print(30*'*', 'Seek Method', 30*'*')
new_f = open('students.txt', 'r')
print('Blinking Cursor Current Position', new_f.tell())
new_f.seek(10) # this will move cursor from 0 to 9 
print('Blinking Cursor New Position', new_f.tell())
data = new_f.read() # now this will start reading from the 9th postion
print(data)
print('Blinking Cursor After Reading File', new_f.tell())
new_f.close()


