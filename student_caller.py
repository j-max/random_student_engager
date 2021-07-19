import numpy as np

def n_random_students(student_list, number_of_students=1,  question = None):
    """
    :param student_list: a list of students in any given class
    :return: a student to be called on
    """

    students =  np.random.choice(student_list, number_of_students)

    if question is not None:
        print(question)

    return students

class cohort_caller:

    def __init__(self, student_list):

        self.student_list = student_list
        self.mutable_student_list = self.student_list.copy()


    def n_random_students(self, number_of_students=1,  question = None):

        if len(self.mutable_student_list) < number_of_students:
            print(self.mutable_student_list)

            self.mutable_student_list = self.student_list.copy()


        choice =  np.random.choice(self.mutable_student_list, number_of_students)
        self.mutable_student_list = [student for student in self.mutable_student_list
                                     if student not in choice]

        return choice


