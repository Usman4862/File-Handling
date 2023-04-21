# NOTE: WRITELINES METHOD FILE HANDLING.

# here we are opening my_new_file, if this file exits it opens it, if not it'll create it

file_ = open('student.txt', mode='w')

# now if i have a random list, which have thousands of records

lst = ['Usman Malik\n', 'Adeel\n', 'Faisal\n', 'Muraad\n'] 

file_.writelines(lst)

file_.close()

print('Data Added Successfully!!!!!!')