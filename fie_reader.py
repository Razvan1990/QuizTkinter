import os
import constans
import random


class FileReader:

    def __init__(self):
        self.final_list = []

    def get_random_value(self, list_values):
        x = random.randrange(start=0, stop=len(list_values) - 1, step=2)
        return x

    def get_preliminary_list(self):
        global question_answer_file
        list_candidates = list()
        try:
            list_random_numbers = []
            path = os.getcwd()
            file = constans.FILENAME
            question_answer_file = open(file=os.path.join(path, file), mode="r", encoding="utf-8")
            # question_answer_file.seek(2)
            list_file = question_answer_file.readlines()
            modified_list = []
            for idx in range(0, len(list_file)):
                if idx == len(list_file) - 1:
                    modified_list.append(list_file[idx])
                else:
                    modified_list.append(list_file[idx][:-1])
            # get 5 values for game and put them as list
            number = 0
            while number < 5:
                list_question_answer = list()
                random_number = self.get_random_value(modified_list)
                # check if random number not in chosen already
                while random_number in list_random_numbers:
                    random_number = self.get_random_value(modified_list)
                # add question and answers for question
                list_random_numbers.append(random_number)
                list_question_answer.append(modified_list[random_number])
                list_question_answer.append(modified_list[random_number + 1])
                list_candidates.append(list_question_answer)
                number += 1
            return list_candidates
        except:
            raise FileNotFoundError
        finally:
            question_answer_file.close()

    '''
    @:return
    a list of dictionaries with questions, choices and correct answer
    '''

    def create_list_dictionary(self):
        candidates = self.get_preliminary_list()
        for list_candidate in candidates:
            dict_questions_answers = dict()
            dict_questions_answers.update({constans.KEY[0]: list_candidate[0]})
            # split the answers
            list_answers = list_candidate[1].split(",")
            # create the dictionary
            for idx in range(0, len(list_answers)):
                dict_questions_answers.update({constans.DICT_LETTERS[idx]: list_answers[idx]})
            self.final_list.append(dict_questions_answers)
        return self.final_list
