history=dict(Mark=100, Lisa=95, Danny=50, Johnny=20, Peter=80)
math=dict(Mark=90, Lisa=100, Danny=51, Johnny=15)

def compare_subjects_within_student(history, math):
    """
    Compare the two subjects with their students and print out the "preferred"
    subject for each student. Single-subject students shouldn't be printed.

    Choice for the data structure of the function's arguments is up to you.
    """
    
for keys in math:
    if math[keys] > history[keys]:
        print (keys, 'math', math[keys])
        
    else:
        print (keys, 'history', history[keys])