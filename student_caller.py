import numpy as np

class CohortCaller:

    def __init__(self, student_list):

        self.student_list = student_list
        self.mutable_student_list = self.student_list.copy()


    def call_n_students(self, number_of_students=1):

        """
        Instruct n_random_students to select a given number of students
        from the class list. 

        :param number_of_students: The number of students to choose in each call
        :returns: 

        """
        if len(self.mutable_student_list) < number_of_students:
            print(self.mutable_student_list)

            self.mutable_student_list = self.student_list.copy()


        choice =  np.random.choice(self.mutable_student_list, number_of_students, replace=False)
        self.mutable_student_list = [student for student in self.mutable_student_list
                                     if student not in choice]
 
        return choice


