import numpy as np

class cohort_caller:

    def __init__(self, student_list):

        self.student_list = student_list
        self.mutable_student_list = self.student_list.copy()


    def n_random_students(self, number_of_students=1,  question = None):

        """TODO describe function

        :param number_of_students: 
        :param question: 
        :returns: 

        """
        if len(self.mutable_student_list) < number_of_students:
            print(self.mutable_student_list)

            self.mutable_student_list = self.student_list.copy()


        choice =  np.random.choice(self.mutable_student_list, number_of_students, replace=False)
        self.mutable_student_list = [student for student in self.mutable_student_list
                                     if student not in choice]

        return choice


