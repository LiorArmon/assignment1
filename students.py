history=dict(Mark=[100,50], Lisa=[95,80], Danny=[50,65], Johnny=[20,15])
math=dict(Mark=[90,80], Lisa=[100,95], Danny=[51,45], Johnny=[15,16], Peter=[80,70])

def compare_subjects_within_student(history, math):
    """
    Compare the two subjects with their students and print out the "preferred"
    subject for each student. Single-subject students shouldn't be printed.

    Choice for the data structure of the function's arguments is up to you.
    """
math_keys=set(math.keys())
history_keys=set(history.keys())
shared_students=math_keys & history_keys
for keys in shared_students:
    if max(math[keys]) > max(history[keys]):
        print (keys, 'math', max(math[keys]))
        
    else:
        print (keys, 'history', max(history[keys]))