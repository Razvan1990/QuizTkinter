import constans


class Helper:
    ''''
     the answers will mimic in fact the checkboxes ticked value
     we will add in separate list all values for a question and check if the list contains the correct answer
     it will basically contain a list with all var_get [ "",checked,"",""]
     '''

    def get_quiz_score(self, list_items, list_checkboxes1, list_checkboxes2, list_checkboxes3, list_checkboxes4,
                       list_checkboxes5):
        result = 0
        if list_items[0][constans.DICT_LETTERS[4]] in list_checkboxes1:
            result += 20
        if list_items[1][constans.DICT_LETTERS[4]] in list_checkboxes2:
            result += 20
        if list_items[2][constans.DICT_LETTERS[4]] in list_checkboxes3:
            result += 20
        if list_items[3][constans.DICT_LETTERS[4]] in list_checkboxes4:
            result += 20
        if list_items[4][constans.DICT_LETTERS[4]] in list_checkboxes5:
            result += 20
        return result

    def get_number_correct_answer_questions(self, result):
        if result == 100:
            return 5, constans.LIST_MESSAGES[0]
        elif result == 80:
            return 4, constans.LIST_MESSAGES[1]
        elif result == 60:
            return 3, constans.LIST_MESSAGES[2]
        elif result == 40:
            return 2, constans.LIST_MESSAGES[3]
        elif result == 20:
            return 1, constans.LIST_MESSAGES[4]
        else:
            return 0, constans.LIST_MESSAGES[5]
