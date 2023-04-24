# NOTE: copy data from file and paste it to another file
print(30*'*', 'Copy Data', 30*'*')
file_ = open('students.txt', 'r')
new_file = open('students1.txt', 'w')
readed_data = file_.read()
content = new_file.write(readed_data)
print(content)
file_.close()
new_file.close()

