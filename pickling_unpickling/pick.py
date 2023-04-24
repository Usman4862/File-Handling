import students
import pickle

number = int(input('Enter number of students: '))
with open('teachers.dat', 'wb') as f:
    for n in range(number):
        name = input('Enter name: ')
        age = int(input('Enter age: '))
        roll = int(input('Enter roll number: '))
        # creating object 
        stu = students.Student(name, age, roll)
        # now serialize or pickling this entered data
        pickle.dump(stu, f)

print('Pickling Done!!!!!!!!!')


