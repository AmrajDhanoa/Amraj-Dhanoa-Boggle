from tkinter import *
import random
from tkinter import messagebox

###### GUI LOGIC ######
window = Tk()
window.title("Amraj's Boogle Game")
window.geometry('600x600')

###### GAME LOGIC ######
words = []
try:
    f = open("words.txt")
    for line in f:
        line = line.strip().upper()
        if line.isalpha():
            words.append(line)
    f.close()
except:
    print("Not found") 


def random_letters():
    '''() -> list
    Generates and returns a list of 16 random unique letters.
    >>> random_letters() -> [D, W, M, I, A, U, G, P, Y, N, O, T, E, R, K, F]'''
    random_letters = []
    letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    while len(random_letters) < 16:
        char = random.choice(letters)
        if char in random_letters:
            continue
        else:
            random_letters.append(char)
    return random_letters

def make_board(random_letters):
    '''(list) -> 2D list
    Takes in random letters and return a 2D list representing the board data.
    >>> make_board([D, W, M, I, A, U, G, P, Y, N, O, T, E, R, K, N])
    -> [[D, W, M, I], [A, U, G, P], [Y, N, O, T], [E, R, K, N]]'''
    board = []
    for i in range(0, len(random_letters), 4):
        board.append(random_letters[i:i+4])
    return board

def check_list_has_unique_words(user_word_list):
    '''(list) -> list
    Takes in the list of already guessed words,
    checks if one word has been guessed twice by the user,
    remove duplicates and returns the list of unique letters.
    >>> check_word_is_unique(['DUNE', 'GOT', 'DUNE', 'ROOT']) -> ['DUNE', 'GOT', 'ROOT']'''
    updated_user_word_list = []
    for item in user_word_list:
        if item not in updated_user_word_list:
            updated_user_word_list.append(item)
    return updated_user_word_list


def check_user_word_with_words(user_word, words):
    '''(str, list) -> Boolean
    Takes in one user word at a time, checks if the word exists in the word list provided 
    and returns True if it does, otherwise returns False.
    >>> check_user_word_with_words('DUNE', words) -> True'''
    if user_word in words:
        return True
    else:
        return False

def check_for_unique_letters(user_word):
    '''(str) -> Boolean
    Takes in one user word at a time, checks if all letters 
    are unique in the word and returns True if they are, otherwise returns False.
    >>> check_for_unique_letters('DUNE') -> True'''
    for char in user_word:
        if user_word.count(char) > 1:
            return False
    return True

def check_board_letters(user_word, board):
    '''(str, list) -> Boolean
    Takes in one user word at a time and the board, 
    checks if all the characters in the word appear on the board 
    and returns True if they do, otherwise returns False.
    >>> board = [[D, W, M, I], [A, U, G, P], [Y, N, O, T], [E, R, K, F]]
    check_board_letters('DUNE', board) -> True '''
    for char in user_word:
        valid = False
        for row in range(4):
            for col in range(4):
                if board[row][col] == char:
                    valid = True
                    break
            if valid == True:
                break
        if valid != True:
            return False
    return True

def get_coor(user_word, board):
    '''(str, 2D list) -> 2D list
    Takes in one user word and the board, 
    finds letter coordinate of the word on the board, stores it in a list 
    and returns the list.
    >>> board = [[D, W, M, I], [A, U, G, P], [Y, N, O, T], [E, R, K, F]]
    get_coor('DUNE', board) -> [[0, 0], [1, 1], [2, 1], [3, 0]]'''
    letter_coor = []
    for char in user_word:
        char_found = False
        for row in range(4):
            coor = []
            #coor.append(board.index(char))
            for col in range(4):
                if board[row][col] == char:
                    coor.append(row)
                    coor.append(col)
                    letter_coor.append(coor)
                    char_found = True
                    break
            if char_found:
                break
    return letter_coor


def check_coor(letter_coordinates):
    '''(list) -> Boolean 
    Takes in the list of letter coordinates, checks if there is a 
    relationship between one letters coordinates and the next letter coordinates 
    (if they are "touching" on the board) and returns True if there are, otherwise returns False.
    >>> letter_coordinates = [[0, 0], [1, 1], [2, 1], [0, 3]]
    check_coor(letter_coordinates) = True'''
    for i in range(len(letter_coordinates) -1):
        row1 = letter_coordinates[i][0]
        col1 = letter_coordinates[i][1]
        row2 = letter_coordinates[i+1][0]
        col2 = letter_coordinates[i+1][1]
        if (row1 + 1 == row2) and (col1 + 1 == col2): #digonial down right  
            continue
        elif (row1 + 1 == row2) and (col1 - 1 == col2):# diagonal down left
            continue
        elif (row1 - 1 == row2) and (col1 - 1 == col2):# diagonal up and left 
            continue
        elif (row1 - 1 == row2) and (col1 + 1 == col2):# diagonal up and right 
            continue
        elif (row1 == row2) and (col1+ 1 == col2): # beside right
            continue
        elif (row1 == row2) and (col1 -1 == col2): #beside left
            continue
        elif (row1 + 1 == row2) and (col1 == col2): # above
            continue
        elif (row1 -1 == row2) and (col1 == col2): # below
            continue
        else:
            return False
    return True 

def user_answer_validate(user_word_list, board):
    '''(list) -> list
    Calls all helper functions to check and validate user input,
    if all functions return True,
    validated words are added to a list which is then returned. 
    >>> user_answer_validate(['DUNE', 'GOT', 'DUNE', 'ROOT']) -> ['DUNE', 'GOT']'''
    updated_user_word_list = check_list_has_unique_words(user_word_list)
    validated_user_word_list = []
    for user_word in updated_user_word_list:
        if (check_user_word_with_words(user_word, words) == True) and (check_for_unique_letters(user_word) == True) and (check_board_letters(user_word, board)== True):
            coor = get_coor(user_word, board)
            if check_coor(coor) == True:
                validated_user_word_list.append(user_word)
    return validated_user_word_list


def score(validated_words, len_point_list):
    '''(list, list) -> list
    Takes in the list of the user's validated words and the list of the length in 
    relation to points and returns a list of the scores for each word.
    len_points_list = [[2, 1], [3, 2], [4, 5], [5, 7], [6, 10]]
    >>> score(['DUNE', 'GOT'], len_points_list) -> [5, 2]'''
    score = []
    for item in validated_words:
        for row in range(5):
            if len(item) == len_point_list[row][0]:
                score.append(len_point_list[row][1])
            elif len(item) > len_point_list[4][0]:
                    score.append(len_point_list[4][1])
    return score

###### GUI LOGIC ######
letters = random_letters()
board = make_board(letters)
guessed_words = []

board_frame = Frame(window)
board_frame.grid(row=0, column=0, columnspan=4)
Label(board_frame, text="Welcome to Amraj's Boogle", font=('Courier', 18)).grid(row=0, column=1, columnspan=4)

def create_board():
    for row in range(4):
        for col in range(4):
            block = Label(board_frame,text=board[row][col], width=8, height=5, font=('Courier', 16), borderwidth=2, relief='solid')
            block.grid(row=row+1, column=col+1)

create_board()

enter_word = Entry(board_frame, width=25)
enter_word.grid(row=5, column=1, columnspan=4, pady=10)

display_guessed_words = Listbox(board_frame, width=20, height=15, font=('Courier', 15))
display_guessed_words.grid(row=1, column=5, rowspan=4, padx=30, sticky='n')


def word_submission():
    word = enter_word.get().upper()
    enter_word.delete(0, END)
    guessed_words.append(word)
    display_guessed_words.insert(END, word)

def start_again():
    global board
    guessed_words.clear()
    display_guessed_words.delete(0, END)
    enter_word.delete(0, END)
    letters = random_letters()
    board = make_board(letters)
    create_board()


def display_user_score():
    validated_words = user_answer_validate(guessed_words, board)
    len_point_list = [[2, 1], [3, 2], [4, 5], [5, 7], [6, 10]]
    final_point_list = score(validated_words,len_point_list)
    final_score = 0
    for i in range(len(final_point_list)):
        final_score += final_point_list[i]
    all_words = ''
    for i in range(len(validated_words)):
        all_words += (f'{validated_words[i]}: {final_point_list[i]}\n')

    messagebox.showinfo(
        'Score', all_words + 'Total score: ' + str(final_score))
    play_again = messagebox.askyesno('Play Another Round','Would you like to play another round?')
    if play_again:
        start_again()
    else:
        window.destroy()

Button(board_frame, text='Sumbit', font=('Courier', 16), command=word_submission).grid(row=6,column=1, columnspan=4, pady =5)
Button(board_frame, text='Display My Score!', font=('Courier', 16), command=display_user_score).grid(row=7,column=1, columnspan=4, pady =5)

window.mainloop()