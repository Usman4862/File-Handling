# Text File (Writing Mode)

# Making a file student.txt and with writing mode

my_file = open('student.txt', mode='w')

# now write something in that file 

my_file.write('Python Developer\n')
my_file.write('How are You ')

print(my_file.mode) # this is used to find the mode of file 
print(my_file.closed) # this will return True if file is close, otherwise False.

# now close this file 

my_file.close()

# this is used to check whether the file is closed or not.

if my_file.closed:
    print("Your File is Close")
else:
    print("Your File is not Closed, please close it.")

print('Writing Successfull')

# Text File (Reading Mode)

# Making a `student_reading.txt` with reading mode

my_file = open('student.txt', mode='r')

# now read above file `my_file`

reading_file = my_file.read()

# now printing the reading file

print(reading_file)

# now closing this my_file 

my_file.close()



"""
Text File Mode Options:
    `r` for reading file and start reading from the start
    `w` for the writing, if any data is present in the file it will override the data. if the file doesn't exit 
     it will create that file.
    `x` open file exclusive creation with write. the specified file must not be available, if the specified file is available it will show 
     error FileExistsError.
    `a` open for appending. The file pointer is positioned at the end of the file. It appends new data  at the end of the file. if file 
     doesn't exists it will create a new file for writing data.
    `r+` open for reading and writing.
    `w+` open for writing and then reading, it will override existing data.
    `a+` open for appending then reading, it won't overide existing data.
"""
# NOTE: Binary File modes are same as Text file modes, just we need to add `b` at the end for example: rb, wb, xb, ab, etc