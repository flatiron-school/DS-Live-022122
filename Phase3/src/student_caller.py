import numpy as np



def one_random_student(student_list, question = None):
    '''
    :param student_list: a list of students in any given class
    :return: a student to be called on
    '''

    student =  np.random.choice(student_list, 1)[0]
    print(student)
    print(question)
