import tkinter
from helper import Helper
from fie_reader import FileReader
from tkinter import *
from tkinter import messagebox
import os
import constans


class GameInterface:

    def __init__(self):
        self.reader = FileReader()
        self.width_frame = 750
        self.height_frame = 750
        self.helper = Helper()

   

    def destroy(self, window_place):
        window_place.destroy()

    '''
    @:param
    The function will take as parameters the list, with its index, which contains the dictionary
    Because we have 5 keys, then it will contain the question label and the 4 checkboxes for the label
    '''

    def check_game(self, dictionary_list):
        global message_game
        list_question1 = list()
        list_question1.append(varA1.get())
        list_question1.append(varA2.get())
        list_question1.append(varA3.get())
        list_question1.append(varA4.get())
        list_question2 = list()
        list_question2.append(varB1.get())
        list_question2.append(varB2.get())
        list_question2.append(varB3.get())
        list_question2.append(varB4.get())
        list_question3 = list()
        list_question3.append(varC1.get())
        list_question3.append(varC2.get())
        list_question3.append(varC3.get())
        list_question3.append(varC4.get())
        list_question4 = list()
        list_question4.append(varD1.get())
        list_question4.append(varD2.get())
        list_question4.append(varD3.get())
        list_question4.append(varD4.get())
        list_question5 = list()
        list_question5.append(varE1.get())
        list_question5.append(varE2.get())
        list_question5.append(varE3.get())
        list_question5.append(varE4.get())
        # see now the result
        result_game = self.helper.get_quiz_score(dictionary_list, list_question1, list_question2, list_question3,
                                                 list_question4, list_question5)
        number_points, message_quiz_game = self.helper.get_number_correct_answer_questions(result_game)

        title_quiz = "QUIZ SCORE"

        correct_answer_1 = dictionary_list[0][constans.DICT_LETTERS[4]]
        correct_answer_2 = dictionary_list[1][constans.DICT_LETTERS[4]]
        correct_answer_3 = dictionary_list[2][constans.DICT_LETTERS[4]]
        correct_answer_4 = dictionary_list[3][constans.DICT_LETTERS[4]]
        correct_answer_5 = dictionary_list[4][constans.DICT_LETTERS[4]]

        final_message = message_quiz_game + str(
            result_game) + " points" + "\n" + "Correct answers are\n" + "\t" + correct_answer_1 + "\n\t" + correct_answer_2 + "\n\t" + correct_answer_3 + "\n\t" + correct_answer_4 \
                        + "\n\t" + correct_answer_5

        message_game = tkinter.messagebox.showinfo(title=title_quiz, message=final_message)
        # make the new game button now enabled
        new_game_button["state"] = tkinter.NORMAL

    def create_new_game(self, dictionary_game_new):
        # delete the previous dictionary
        dictionary_game_new.clear()
        # delete the labels
        label_question1.pack_forget()
        label_question2.pack_forget()
        label_question3.pack_forget()
        label_question4.pack_forget()
        label_question5.pack_forget()
        # delete the existing checkboxes
        # use a for loop to pack_forget all at once
        list_checkboxes = list()
        list_checkboxes.append(checkboxA1)
        list_checkboxes.append(checkboxA2)
        list_checkboxes.append(checkboxA3)
        list_checkboxes.append(checkboxA4)

        list_checkboxes.append(checkboxB1)
        list_checkboxes.append(checkboxB2)
        list_checkboxes.append(checkboxB3)
        list_checkboxes.append(checkboxB4)

        list_checkboxes.append(checkboxC1)
        list_checkboxes.append(checkboxC2)
        list_checkboxes.append(checkboxC3)
        list_checkboxes.append(checkboxC4)

        list_checkboxes.append(checkboxD1)
        list_checkboxes.append(checkboxD2)
        list_checkboxes.append(checkboxD3)
        list_checkboxes.append(checkboxD4)

        for chbox in list_checkboxes:
            chbox.pack_forget()
        # recreate dictionary and put all on grid
        dictionary_game_new = self.reader.create_list_dictionary()
        self.create_quiz_buttons(dictionary_game_new, 0, label_question1, checkboxA1, checkboxA2, checkboxA3,
                                 checkboxA4)
        self.create_quiz_buttons(dictionary_game_new, 1, label_question2, checkboxB1, checkboxB2, checkboxB3,
                                 checkboxB4)
        self.create_quiz_buttons(dictionary_game_new, 2, label_question3, checkboxC1, checkboxC2, checkboxC3,
                                 checkboxC4)
        self.create_quiz_buttons(dictionary_game_new, 3, label_question4, checkboxD1, checkboxD2, checkboxD3,
                                 checkboxD4)
        self.create_quiz_buttons(dictionary_game_new, 4, label_question5, checkboxE1, checkboxE2, checkboxE3,
                                 checkboxE4)
        checkboxA1.deselect()
        checkboxA2.deselect()
        checkboxA3.deselect()
        checkboxA4.deselect()
        checkboxB1.deselect()
        checkboxB2.deselect()
        checkboxB3.deselect()
        checkboxB4.deselect()
        checkboxC1.deselect()
        checkboxC2.deselect()
        checkboxC3.deselect()
        checkboxC4.deselect()
        checkboxD1.deselect()
        checkboxD2.deselect()
        checkboxD3.deselect()
        checkboxD4.deselect()
        # put everything on grid
        label_question1.grid(row=1, columnspan=2, sticky=W + E)
        checkboxA1.grid(row=2, column=0, sticky=W)
        checkboxA2.grid(row=2, column=1, sticky=E)
        checkboxA3.grid(row=3, column=0, sticky=W)
        checkboxA4.grid(row=3, column=1, sticky=E)

        label_question2.grid(row=4, columnspan=2, sticky=W + E)
        checkboxB1.grid(row=5, column=0, sticky=W)
        checkboxB2.grid(row=5, column=1, sticky=E)
        checkboxB3.grid(row=6, column=0, sticky=W)
        checkboxB4.grid(row=6, column=1, sticky=E)

        label_question3.grid(row=7, columnspan=2, sticky=W + E)
        checkboxC1.grid(row=8, column=0, sticky=W)
        checkboxC2.grid(row=8, column=1, sticky=E)
        checkboxC3.grid(row=9, column=0, sticky=W)
        checkboxC4.grid(row=9, column=1, sticky=E)

        label_question4.grid(row=10, columnspan=2, sticky=W + E)
        checkboxD1.grid(row=11, column=0, sticky=W)
        checkboxD2.grid(row=11, column=1, sticky=E)
        checkboxD3.grid(row=12, column=0, sticky=W)
        checkboxD4.grid(row=12, column=1, sticky=E)

        label_question5.grid(row=13, columnspan=2, sticky=W + E)
        checkboxE1.grid(row=14, column=0, sticky=W, )
        checkboxE2.grid(row=14, column=1, sticky=E, )
        checkboxE3.grid(row=15, column=0, sticky=W, )
        checkboxE4.grid(row=15, column=1, sticky=E, )

        check_button.grid(row=16, column=0, pady=5, padx=2, columnspan=2)
        check_button.columnconfigure(1, weight=1)
        check_button.rowconfigure(1, weight=1)

    def create_quiz_buttons(self, dict_values, index, label, check1, check2, check3, check4):
        label["text"] = dict_values[index][constans.DICT_LETTERS[5]]
        check1["text"] = dict_values[index][constans.DICT_LETTERS[0]]
        check1["onvalue"] = dict_values[index][constans.DICT_LETTERS[0]]
        check2["text"] = dict_values[index][constans.DICT_LETTERS[1]]
        check2["onvalue"] = dict_values[index][constans.DICT_LETTERS[1]]
        check3["text"] = dict_values[index][constans.DICT_LETTERS[2]]
        check3["onvalue"] = dict_values[index][constans.DICT_LETTERS[2]]
        check4["text"] = dict_values[index][constans.DICT_LETTERS[3]]
        check4["onvalue"] = dict_values[index][constans.DICT_LETTERS[3]]

    def create_interface(self, window_place):
        dictionary_game = self.reader.create_list_dictionary()
        global new_game_button
        global close_button
        # we have 5 labels and 20 checkboxes
        global label_question1
        global label_question2
        global label_question3
        global label_question4
        global label_question5

        global checkboxA1
        global varA1
        global checkboxA2
        global varA2
        global checkboxA3
        global varA3
        global checkboxA4
        global varA4

        global checkboxB1
        global varB1
        global checkboxB2
        global varB2
        global checkboxB3
        global varB3
        global checkboxB4
        global varB4

        global checkboxC1
        global varC1
        global checkboxC2
        global varC2
        global checkboxC3
        global varC3
        global checkboxC4
        global varC4

        global checkboxD1
        global varD1
        global checkboxD2
        global varD2
        global checkboxD3
        global varD3
        global checkboxD4
        global varD4

        global checkboxE1
        global varE1
        global checkboxE2
        global varE2
        global checkboxE3
        global varE3
        global checkboxE4
        global varE4

        global check_button

        varA1 = StringVar()
        varA2 = StringVar()
        varA3 = StringVar()
        varA4 = StringVar()

        varB1 = StringVar()
        varB2 = StringVar()
        varB3 = StringVar()
        varB4 = StringVar()

        varC1 = StringVar()
        varC2 = StringVar()
        varC3 = StringVar()
        varC4 = StringVar()

        varD1 = StringVar()
        varD2 = StringVar()
        varD3 = StringVar()
        varD4 = StringVar()

        varE1 = StringVar()
        varE2 = StringVar()
        varE3 = StringVar()
        varE4 = StringVar()

        # create first frame

        game_frame = LabelFrame(window_place, text="GAME", bg="#A9B866", fg="#DC526D",
                                font=("Comic Sans", 20, "bold"), labelanchor="n", width=self.width_frame / 2,
                                cursor="man",
                                height=self.height_frame / 3, padx=100, pady=25)
        game_frame.grid(row=0, column=0)
        game_frame.rowconfigure(0, weight=1)
        game_frame.columnconfigure(0, weight=1)

        quiz_frame = LabelFrame(window_place, text="QUIZ", bg="#A9B866", fg="#DC526D",
                                font=("Comic Sans", 20, "bold"), labelanchor="n", width=self.width_frame, cursor="trek",
                                height=self.height_frame)
        quiz_frame.grid(padx=70 / 2, pady=200 / 3, row=0, column=1, )  # put it in the middle
        quiz_frame.grid_rowconfigure(0, weight=1)
        quiz_frame.grid_columnconfigure(0, weight=1)

        # put buttons on first frame
        new_game_button = Button(game_frame, text="NEW GAME", fg="#F4F4F2", bg="#8DC6D5",
                                 font=("Arial", 14, "bold"), bd=3, cursor="target", width=12, pady=5,
                                 state=tkinter.DISABLED, command=lambda: self.create_new_game(dictionary_game))
        close_button = Button(game_frame, text="CLOSE GAME", fg="#F4F4F2", bg="#D17743",
                              font=("Arial", 14, "bold"), bd=3, cursor="target", width=12, pady=5,
                              command=lambda: self.destroy(window_place))
        new_game_button.grid(row=0, column=0)
        close_button.grid(row=1, column=0)
        # put things on second frame
        label_question1 = Label(quiz_frame, fg="#EAF2F0", bg="#105C44", font=("Comic Sans", 9, "bold"),
                                justify="center", bd=3, )
        label_question2 = Label(quiz_frame, fg="#EAF2F0", bg="#105C44", font=("Comic Sans", 9, "bold"),
                                justify="center", bd=3, )
        label_question3 = Label(quiz_frame, fg="#EAF2F0", bg="#105C44", font=("Comic Sans", 9, "bold"),
                                justify="center", bd=3, )
        label_question4 = Label(quiz_frame, fg="#EAF2F0", bg="#105C44", font=("Comic Sans", 9, "bold"),
                                justify="center", bd=3, )
        label_question5 = Label(quiz_frame, fg="#EAF2F0", bg="#105C44", font=("Comic Sans", 9, "bold"),
                                justify="center", bd=3, )
        check_button = Button(quiz_frame, text="CHECK SCORE", bg="#105C44", fg="#D52350", font=("Arial", 14, "bold"),
                              bd=3, width=12, pady=5, cursor="star", padx=-6,
                              command=lambda: self.check_game(dictionary_game))
        '''
        create the checkboxes
        '''
        # question1

        checkboxA1 = Checkbutton(quiz_frame, variable=varA1, offvalue="", padx=10, pady=6, justify="center")
        checkboxA2 = Checkbutton(quiz_frame, variable=varA2, offvalue="", padx=10, pady=6, justify="center")
        checkboxA3 = Checkbutton(quiz_frame, variable=varA3, offvalue="", padx=10, pady=6, justify="center")
        checkboxA4 = Checkbutton(quiz_frame, variable=varA4, offvalue="", padx=10, pady=6, justify="center")
        self.create_quiz_buttons(dictionary_game, 0, label_question1, checkboxA1, checkboxA2, checkboxA3, checkboxA4)
        # we do this to avoid the checkbox tkinter bug
        checkboxA1.deselect()
        checkboxA2.deselect()
        checkboxA3.deselect()
        checkboxA4.deselect()

        # question2

        checkboxB1 = Checkbutton(quiz_frame, variable=varB1, offvalue="", padx=10, pady=6, justify="center")
        checkboxB2 = Checkbutton(quiz_frame, variable=varB2, offvalue="", padx=10, pady=6, justify="center")
        checkboxB3 = Checkbutton(quiz_frame, variable=varB3, offvalue="", padx=10, pady=6, justify="center")
        checkboxB4 = Checkbutton(quiz_frame, variable=varB4, offvalue="", padx=10, pady=6, justify="center")
        self.create_quiz_buttons(dictionary_game, 1, label_question2, checkboxB1, checkboxB2, checkboxB3, checkboxB4)
        # we do this to avoid the checkbox tkinter bug
        checkboxB1.deselect()
        checkboxB2.deselect()
        checkboxB3.deselect()
        checkboxB4.deselect()

        # question3

        checkboxC1 = Checkbutton(quiz_frame, variable=varC1, offvalue="", padx=10, pady=6, justify="center")
        checkboxC2 = Checkbutton(quiz_frame, variable=varC2, offvalue="", padx=10, pady=6, justify="center")
        checkboxC3 = Checkbutton(quiz_frame, variable=varC3, offvalue="", padx=10, pady=6, justify="center")
        checkboxC4 = Checkbutton(quiz_frame, variable=varC4, offvalue="", padx=10, pady=6, justify="center")
        self.create_quiz_buttons(dictionary_game, 2, label_question3, checkboxC1, checkboxC2, checkboxC3, checkboxC4)
        # we do this to avoid the checkbox tkinter bug
        checkboxC1.deselect()
        checkboxC2.deselect()
        checkboxC3.deselect()
        checkboxC4.deselect()

        # question4

        checkboxD1 = Checkbutton(quiz_frame, variable=varD1, offvalue="", padx=10, pady=6, justify="center")
        checkboxD2 = Checkbutton(quiz_frame, variable=varD2, offvalue="", padx=10, pady=6, justify="center")
        checkboxD3 = Checkbutton(quiz_frame, variable=varD3, offvalue="", padx=10, pady=6, justify="center")
        checkboxD4 = Checkbutton(quiz_frame, variable=varD4, offvalue="", padx=10, pady=6, justify="center")
        self.create_quiz_buttons(dictionary_game, 3, label_question4, checkboxD1, checkboxD2, checkboxD3, checkboxD4)
        # we do this to avoid the checkbox tkinter bug
        checkboxD1.deselect()
        checkboxD2.deselect()
        checkboxD3.deselect()
        checkboxD4.deselect()

        # question5

        checkboxE1 = Checkbutton(quiz_frame, variable=varE1, offvalue="", padx=10, pady=6, justify="center")
        checkboxE2 = Checkbutton(quiz_frame, variable=varE2, offvalue="", padx=10, pady=6, justify="center")
        checkboxE3 = Checkbutton(quiz_frame, variable=varE3, offvalue="", padx=10, pady=6, justify="center")
        checkboxE4 = Checkbutton(quiz_frame, variable=varE4, offvalue="", padx=10, pady=6, justify="center")
        self.create_quiz_buttons(dictionary_game, 4, label_question5, checkboxE1, checkboxE2, checkboxE3, checkboxE4)
        # we do this to avoid the checkbox tkinter bug
        checkboxE1.deselect()
        checkboxE2.deselect()
        checkboxE3.deselect()
        checkboxE4.deselect()

        # put everything in grid

        label_question1.grid(row=1, columnspan=2, sticky=W + E)
        checkboxA1.grid(row=2, column=0, sticky=W)
        checkboxA2.grid(row=2, column=1, sticky=E)
        checkboxA3.grid(row=3, column=0, sticky=W)
        checkboxA4.grid(row=3, column=1, sticky=E)

        label_question2.grid(row=4, columnspan=2, sticky=W + E)
        checkboxB1.grid(row=5, column=0, sticky=W)
        checkboxB2.grid(row=5, column=1, sticky=E)
        checkboxB3.grid(row=6, column=0, sticky=W)
        checkboxB4.grid(row=6, column=1, sticky=E)

        label_question3.grid(row=7, columnspan=2, sticky=W + E)
        checkboxC1.grid(row=8, column=0, sticky=W)
        checkboxC2.grid(row=8, column=1, sticky=E)
        checkboxC3.grid(row=9, column=0, sticky=W)
        checkboxC4.grid(row=9, column=1, sticky=E)

        label_question4.grid(row=10, columnspan=2, sticky=W + E)
        checkboxD1.grid(row=11, column=0, sticky=W)
        checkboxD2.grid(row=11, column=1, sticky=E)
        checkboxD3.grid(row=12, column=0, sticky=W)
        checkboxD4.grid(row=12, column=1, sticky=E)

        label_question5.grid(row=13, columnspan=2, sticky=W + E)
        checkboxE1.grid(row=14, column=0, sticky=W, )
        checkboxE2.grid(row=14, column=1, sticky=E, )
        checkboxE3.grid(row=15, column=0, sticky=W, )
        checkboxE4.grid(row=15, column=1, sticky=E, )

        check_button.grid(row=16, column=0, pady=5, padx=2, columnspan=2)
        check_button.columnconfigure(1, weight=1)
        check_button.rowconfigure(1, weight=1)

    def create_outerframe(self, window_place):
        window_place.geometry("1100x900")
        icon = os.path.join(os.getcwd(), "milionaire.ico")
        window_place.iconbitmap(icon)
        window_place.configure(background="#C9EAD4")

    def start_gui(self):
        root = Tk()
        root.title("WANT TO BE MILLIONAIRE?")
        self.create_outerframe(root)
        self.create_interface(root)
        root.mainloop()
