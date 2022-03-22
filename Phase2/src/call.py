
def call_on_students(
    n_students, 
    students_list_loc="src/students.txt", 
    output_list_loc="src/output_students.txt"
    ):
    """
    Inputs:
        n_students : int, number of students to call
        students_list_loc : str, relative location of student list txt file
        output_list_loc : str, relative location of already-called-upon students txt file
    """

    import numpy as np

    with open(students_list_loc) as input_file:
        students = input_file.read().split("\n")

    with open(output_list_loc) as output_file:
        already_called = output_file.read().split(",")

    can_be_called = [s for s in students if s not in already_called]

    # Handles what happens if the number of students to call is greater than
    # the number of students left on the student list (can_be_called)
    if n_students > len(can_be_called):
        n_needed = n_students - len(can_be_called)
        restart_list = [s for s in students if s not in can_be_called]
        restart_output = np.random.choice(restart_list, n_needed, replace=False)
        output = [*can_be_called, *list(restart_output)]

    else: 
        output = np.random.choice(can_be_called, n_students, replace=False)

    print(output)

    with open(output_list_loc, mode="w") as output_file:
        if already_called[0] == '':
            output_file.write(",".join(output))
        elif n_students > len(can_be_called):
            output_file.truncate(0)
            output_file.write(",".join([*output]))
        else:
            output_file.truncate(0)
            output_file.write(",".join([*already_called, *output]))
