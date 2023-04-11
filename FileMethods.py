new_file = open('teacher.txt', 'w')

new_file.write('I am writting\n')
new_file.write('in my new file with new line.')

print('Readable: ', new_file.readable()) # this method checks whether the file is readable 
print('Writeable: ', new_file.writable()) # this method checks whether the file is writable
print('FileName: ', new_file.name) # this method checks the name of the file
print('FileMode: ', new_file.mode) # this will check the mode of the file
print('FileClosed: ', new_file.closed) # this will check the file is closed or not.


new_file.close()