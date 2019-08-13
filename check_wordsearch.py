from wordsearch import *


def word_in_line_checker():
    flag = True

    if word_in_line("Pa", ['P','P','a','p','A','r']) != 1:
        flag = False

    elif word_in_line("DoG", ['P','P','a','p','A','r']) != 0:
        flag = False

    elif word_in_line("P", ['P','P','a','p','A','r']) != 2:
        flag = False

    elif word_in_line("hallo", ['h','a','l','l','o']) != 1:
        flag = False

    elif word_in_line("AAA", ['A','A','A','A','A','A']) != 4:
        flag = False

    elif word_in_line("XpX", ['X','p','X','p','X','g']) != 2:
        flag = False

    if flag:  # Check if everything is succeeded
        print('Function "word_in_line" test success')
    else:
        print('Function "word_in_line" test fail')

    return flag


if __name__ == '__main__':
    word_in_line_checker()
