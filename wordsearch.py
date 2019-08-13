import sys
import os.path
from copy import deepcopy


NUM_OF_ARGS = 4
ERROR_MSG_ARGS = "ERROR: The number of arguments is invalid"
ERROR_MSG_FILE_WORD = "ERROR: file for words list does not exist"
ERROR_MSG_FILE_MTR = "ERROR: file for matrix does not exist"
ERROR_MSG_DIRECTIONS = "ERROR: Invalid search direction"

WORDS_FILE_LOC = 0
MATRIX_FILE_LOC = 1
OUTPUT_FILE_LOC = 2
INPUT_DIRECTIONS_LOC = 3

EMPTY_STRING = ""

# Search directions-
UP = "u"
DOWN = "d"
RIGHT = "r"
LEFT = "l"

DOWN_RIGHT = "y"
DOWN_LEFT = "z"
UP_RIGHT = "w"
UP_LEFT = "x"

LEGAL_DIRECTIONS =\
    UP + DOWN + RIGHT + LEFT + DOWN_RIGHT + DOWN_LEFT + UP_RIGHT + UP_LEFT


def check_input_args(inp_args):
    """
    A function that checks the integrity of the input
    :param inp_args: A list contains the strings received from the user
    :return: If input is valid, None
             If input is invalid, string, error message
    """
    if len(inp_args) != NUM_OF_ARGS:
        return ERROR_MSG_ARGS

    if not os.path.isfile(inp_args[WORDS_FILE_LOC]):
        return ERROR_MSG_FILE_WORD

    if not os.path.isfile(inp_args[MATRIX_FILE_LOC]):
        return ERROR_MSG_FILE_MTR

    for direction in inp_args[INPUT_DIRECTIONS_LOC]:
        if direction not in LEGAL_DIRECTIONS:
            return ERROR_MSG_DIRECTIONS

    return None


def read_wordlist_file(filename):
    """
    A function that converts the word file to a list of words for review
    :param filename: String, word file name
    :return: List, word list for testing
    """
    words = []
    file_words = open(filename)
    for line in file_words:
        words.append(line.strip())
    file_words.close()
    return words


def read_matrix_file(filename):
    """
    A function that converts the matrix file to a list containing lists,
     which represents the matrix
    :param filename: String, matrix file name
    :return: list containing lists, representing the matrix
    """
    mtr = []
    open_file = open(filename)
    for line in open_file:
        one_line = []
        for char in line:
            if char != '\n' and char != ",":
                one_line.append(char)
        mtr.append(one_line)
    open_file.close()
    return mtr


def word_in_line(word, list_to_scan):
    """
    Function Counting how many times a string appears in a list
    :param word: String, search word
    :param list_to_scan: list, character for review
    :return: int, how often the word appears
    """
    counter = 0
    for i in range(len(list_to_scan)):
        if list_to_scan[i] == word[0] and len(list_to_scan) - i >= len(word):
            optional_word = EMPTY_STRING.join(list_to_scan[i:i+len(word)])
            if optional_word == word:
                counter += 1
    return counter


def scan_line(list_to_scan, words, straight, reverse):
    """
    A function that searches list of words in a specific list,
    according to the given direction
    :param list_to_scan: list, character for review
    :param words: List, strings, search words
    :param straight: Boolean, do check in a straight direction
    :param reverse: Boolean, do check in the opposite direction
    :return:
    """
    if straight:
        for word in words:
            words[word] += word_in_line(word, list_to_scan)
    if reverse:
        list_to_scan.reverse()
        for word in words:
            words[word] += word_in_line(word, list_to_scan)


def col_scan(word_counter, matrix, straight, reverse):
    """
    A function that scans the matrix columns for all words in the list.
    :param word_counter:Dictionary, collection of all words and their counters
    :param matrix: list containing lists, representing the matrix
    :param straight: Boolean, do check in a straight direction
    :param reverse: Boolean, do check in the opposite direction
    Updating the counters according to the search results
    """
    for col in range(len(matrix[0])):
        list_to_scan = []
        for row in range(len(matrix)):
            list_to_scan.append(matrix[row][col])

        scan_line(list_to_scan, word_counter, straight, reverse)


def left_done_scan(word_counter, matrix, straight, reverse):
    """
    A function that scans the diagonal of the matrix, in the right direction
     for all the words in the list.
    :param word_counter:Dictionary, collection of all words and their counters
    :param matrix: list containing lists, representing the matrix
    :param straight: Boolean, do check in a straight direction
    :param reverse: Boolean, do check in the opposite direction
    Updating the counters according to the search results
    """
    # Scan from the first-row diagonal
    for col in range(len(matrix[0])):
        list_to_scan = []
        row = 0
        while row < len(matrix) and col+row < len(matrix[0]):
            list_to_scan.append(matrix[row][col+row])
            row += 1
        scan_line(list_to_scan, word_counter, straight, reverse)

    # Scan the diagonal from the last column except the first
    for row in range(1, len(matrix)):
        list_to_scan = []
        col = 0
        while col < len(matrix[0]) and col + row < len(matrix):
            list_to_scan.append(matrix[col + row][col])
            col += 1
        scan_line(list_to_scan, word_counter, straight, reverse)


def matrix_transpose(original_mtr):
    """
    A function that transpose the matrix. replacing the rows and columns.
    :param original_mtr: list containing lists, the original matrix
    :return: list containing lists, the new matrix
    """
    new_mtr = []
    if len(original_mtr) > 0:
        for col in range(len(original_mtr[0])):
            list_to_add = []
            for row in range(len(original_mtr)):
                list_to_add.append(original_mtr[row][col])

            new_mtr.append(list_to_add)
    return new_mtr


def matrix_mirror(original_mtr):
    """
    Function reverses the order of the matrix rows
    :param original_mtr: list containing lists, the original matrix
    :return: list containing lists, the new matrix
    """
    new_mtr = deepcopy(original_mtr)
    for row in range(len(new_mtr)):
        new_mtr[row] = new_mtr[row][::-1]
    return new_mtr


REVERSE_DIRECTION_LOC = 0
STRAIGHT_DIRECTION_LOC = 1


def search_direction(directions, one_search):
    """
    function checks for search direction, whether to check straight or reverse
    :param directions: String, and data search directions
    :param one_search: String, specific direction for testing
    :return: Boolean Search Straight or Reverse
    """
    if one_search[REVERSE_DIRECTION_LOC] in directions:
        reverse = True
    else:
        reverse = False
    if one_search[STRAIGHT_DIRECTION_LOC] in directions:
        straight = True
    else:
        straight = False
    return reverse, straight


def find_words_in_matrix(word_list, matrix, directions):
    """
    A function that searches for words in a matrix,
     according to the directions given
    :param word_list: List, search words
    :param matrix: list containing lists, representing the matrix
    :param directions: String, letters representing search directions
    :return: list of tuples, found words, and number of times
    """
    # Handling the case of an empty matrix-
    if len(matrix) == 0:
        return []
    # Dictionary variable, collection of all words and their counters-
    word_counter = {one_word: 0 for one_word in word_list}

    # Checking the search directions, and scan in the appropriate directions-
    reverse, straight = search_direction(directions, UP+DOWN)
    if reverse or straight:
        col_scan(word_counter, matrix, straight, reverse)

    reverse, straight = search_direction(directions, LEFT+RIGHT)
    if reverse or straight:
        col_scan(word_counter, matrix_transpose(matrix), straight, reverse)

    reverse, straight = search_direction(directions, UP_LEFT+DOWN_RIGHT)
    if reverse or straight:
        left_done_scan(word_counter, matrix, straight, reverse)

    reverse, straight = search_direction(directions, UP_RIGHT+DOWN_LEFT)
    if reverse or straight:
        left_done_scan(word_counter, matrix_mirror(matrix), straight, reverse)

    # list of tuples, found words, and number of times-
    list_to_return = [(word, word_counter[word])
                      for word in word_counter if word_counter[word] != 0]

    return list_to_return


def write_output_file(results, output_filename):
    """
    A function that writes to a file the search results
    :param results: List, search results
    :param output_filename: String, file name to write results
    """
    file_to_write = open(output_filename, 'w')

    for pair in results:
        str_pair = pair[0] + ',' + str(pair[1]) + "\n"
        file_to_write.write(str_pair)

    file_to_write.close()


def main(inp_args):
    """
    main function,
    Checks the integrity of the input, runs the word search in the matrix,
    and writes the results to the file
    :param inp_args: List, input from the user
    """
    msg = check_input_args(inp_args)
    if msg is not None:
        return

    words = read_wordlist_file(inp_args[WORDS_FILE_LOC])
    mtr = read_matrix_file(inp_args[MATRIX_FILE_LOC])

    results = find_words_in_matrix(words, mtr, inp_args[INPUT_DIRECTIONS_LOC])
    write_output_file(results, inp_args[OUTPUT_FILE_LOC])


if __name__ == '__main__':
    """
    Receive input from the user and start the software
    """
    args = sys.argv[1:]  # Receiving variables from the user to a list
    main(args)
