import numpy as np
from itertools import permutations
from student_list import avocoder_toasters

class CohortCaller:

    def __init__(self, student_list):

        self.student_list = student_list
        self.mutable_student_list = self.student_list.copy()
        self.all_pairs = list(permutations(self.student_list, 2))
        self.mutable_pairs = None

    def call_n_students(self, number_of_students=1):

        """
        Instruct n_random_students to select a given number of students
        from the class list. 

        :param number_of_students: The number of students to choose in each call
        :returns:

        """

        # Reset the list if there are not enough students to be called
        if len(self.mutable_student_list) < number_of_students:
            print(self.mutable_student_list)

            self.mutable_student_list = self.student_list.copy()

        choice =  np.random.choice(self.mutable_student_list,
                                   number_of_students, replace=False)

        self.mutable_student_list = [student for student in
                                     self.mutable_student_list if
                                     student not in choice]

        return choice

    def generate_pairs(self):


        '''
        Pairs of students are generated from the student list using itertools
        combinations.

        After each pair activities, the used pairs are removed
        from the mutable pairs list
        '''

        if self.mutable_pairs == None:
            # np.random.choice doesn't work when choosing tuples from a list
            # so pair tupples are converted to strings
            self.all_pairs = [pair[0] +' '+ pair[1] for pair in self.all_pairs]
            self.mutable_pairs = self.all_pairs.copy()

        '''The number of pairs should be the total number of students
         divided by 2 rounded down.
         If there is an odd number of students, the odd student will
         be added to the last group'''

        # if the class has an odd number of students
        if len(self.student_list)%2:
            number_of_pairs = len(self.student_list)//2
            # Choose a random pair from the available pairs

            activity_pairs = []
            pair_choices_remaining = self.mutable_pairs.copy()

            while len(activity_pairs) < number_of_pairs:
                pair_choice = np.random.choice(pair_choices_remaining)
                activity_pairs.append(pair_choice)

                # make a copy of mutable pairs. This is a temporary list of pairs to choose from.
                pairs_to_remove = pair_in_list(pair_choice, pair_choices_remaining)
                pair_choices_remaining = [pair for pair in pair_choices_remaining
                                          if pair not in pairs_to_remove]


            print(activity_pairs)

            for pair,group in zip(activity_pairs, list(range(1,number_of_pairs+1))):
                print('Group ' + str(group) + ': Driver --> ' + pair + ' <--Navigator')

            selected_students = []

            for pair in activity_pairs:
                selected_students.extend(pair.split(' '))

            student_not_selected = [student for student in self.student_list
                                    if student not in selected_students]

            print('Group ' + str(group) + ': ' + student_not_selected[0])




        # if the class has an even number of students
        else:

            number_of_pairs = len(self.student_list)//2

            activity_pairs = np.random.choice(self.mutable_pairs, number_of_pairs,
                                            replace=False)

            # Determine which students were randomly selected
            selected_students = set([student for pair in activity_pairs
                                for student in pair.split(' ')])

            # if not all students were selected, recreate the pairs
            while len(selected_students) != len(self.student_list):
                activity_pairs = np.random.choice(self.mutable_pairs, number_of_pairs,
                                            replace=False)
                selected_students = set([student for pair in activity_pairs
                                for student in pair.split(' ')])

            if not len(self.student_list)%2:
                for pair, group in zip(activity_pairs, range(1,len(activity_pairs)+1)):
                    print('Group ' + str(group) + ': Driver --> ' + pair + ' <--Navigator')
                    self.mutable_pairs.remove(pair)

def pair_in_list(chosen_pair, possible_pairs):

    ''' Given a chosen tuple of students
        find all remaining pairs that include
        either of the students

    params:
    chosen_pair: a string of students in a pair
    possible_pairs: a list of strings representing student pairs

    '''
    pairs_to_remove = []
    student_1, student_2 = chosen_pair.split(' ')
    for pair in possible_pairs:
        pair_1, pair_2 = pair.split(' ')

        if pair_1 == student_1:
            pairs_to_remove.append(pair)
        elif pair_1 == student_2:
            pairs_to_remove.append(pair)
        elif pair_2 == student_1:
            pairs_to_remove.append(pair)
        elif pair_2 == student_2:
            pairs_to_remove.append(pair)
        else:
            continue

    return pairs_to_remove

# Test pair_in_list
test_cohort = CohortCaller(avocoder_toasters)
test_cohort.generate_pairs()
remove_pair_test = pair_in_list('Raylin Ronak', test_cohort.mutable_pairs)

