import pickle, students

with open('teachers.dat', 'rb') as f:
    while True:
        try:
            obj = pickle.load(f)
            obj.show()
        except EOFError:
            print('Done')
            break



