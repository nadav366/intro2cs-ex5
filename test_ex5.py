from wordsearch import *


def test_find_words_in_matrix():
    word_list1 = ['tY', 'mOm', 'jjm', 'mfu', 'j', 'jj']
    mtr1 = [['m', 't', 'Y'], ['f', 'O', 'h'], ['u', 'f', 'm'], ['u', 't', 'j'], ['j', 'Y', 'j'], ['j', 'j', 'm'], ['t', 'Y', 't']]

    results1u = find_words_in_matrix(word_list1, mtr1, 'u')
    results1d = find_words_in_matrix(word_list1, mtr1, 'd')

    results1r = find_words_in_matrix(word_list1, mtr1, 'r')
    results1l = find_words_in_matrix(word_list1, mtr1, 'l')

    results1w = find_words_in_matrix(word_list1, mtr1, 'w')
    results1z = find_words_in_matrix(word_list1, mtr1, 'z')

    results1x = find_words_in_matrix(word_list1, mtr1, 'x')
    results1y = find_words_in_matrix(word_list1, mtr1, 'y')

    assert ('tY', 2) in results1r
    assert ('jjm', 1) in results1r
    assert ('j', 5) in results1r
    assert ('jj', 1) in results1r
    assert len(results1r) == 4

    assert ('tY', 1) in results1l
    assert ('mfu', 1) in results1l
    assert ('j', 5) in results1l
    assert ('jj', 1) in results1l
    assert len(results1l) == 4

    assert ('jjm', 1) in results1u
    assert ('jj', 2) in results1u
    assert ('j', 5) in results1u
    assert len(results1u) == 3

    assert ('tY', 1) in results1d
    assert ('mfu', 1) in results1d
    assert ('j', 5) in results1d
    assert ('jj', 2) in results1d
    assert ('jjm', 1) in results1d
    assert len(results1d) == 5

    assert ('jj', 1) in results1w
    assert ('j', 5) in results1w
    assert len(results1w) == 2

    assert ('jj', 1) in results1z
    assert ('j', 5) in results1z
    assert len(results1z) == 2

    assert ('jj', 1) in results1x
    assert ('j', 5) in results1x
    assert ('mOm', 1) in results1x
    assert len(results1x) == 3

    assert ('jj', 1) in results1y
    assert ('j', 5) in results1y
    assert ('mOm', 1) in results1y
    assert len(results1y) == 3

    results1udx = find_words_in_matrix(word_list1, mtr1, 'udx')
    results1wwd = find_words_in_matrix(word_list1, mtr1, 'wwd')

    results1rly = find_words_in_matrix(word_list1, mtr1, 'rly')
    results1yx = find_words_in_matrix(word_list1, mtr1, 'yx')

    results1zduyl = find_words_in_matrix(word_list1, mtr1, 'zduyl')
    results1rlu = find_words_in_matrix(word_list1, mtr1, 'rlu')

    results1rxwz = find_words_in_matrix(word_list1, mtr1, 'rxwz')
    results1udrlwxyz = find_words_in_matrix(word_list1, mtr1, 'udrlwxyz')

    assert ('tY', 1) in results1udx
    assert ('jjm', 2) in results1udx
    assert ('j', 15) in results1udx
    assert ('jj', 5) in results1udx
    assert ('mfu', 1) in results1udx
    assert ('mOm', 1) in results1udx
    assert len(results1udx) == 6

    assert ('tY', 1) in results1wwd
    assert ('jjm', 1) in results1wwd
    assert ('j', 10) in results1wwd
    assert ('jj', 3) in results1wwd
    assert ('mfu', 1) in results1wwd
    assert len(results1wwd) == 5

    assert ('tY', 3) in results1rly
    assert ('jjm', 1) in results1rly
    assert ('j', 15) in results1rly
    assert ('jj', 3) in results1rly
    assert ('mfu', 1) in results1rly
    assert ('mOm', 1) in results1rly
    assert len(results1rly) == 6

    assert ('jj', 2) in results1yx
    assert ('j', 10) in results1yx
    assert ('mOm', 2) in results1yx
    assert len(results1yx) == 3

    assert ('tY', 2) in results1zduyl
    assert ('jjm', 2) in results1zduyl
    assert ('j', 25) in results1zduyl
    assert ('jj', 7) in results1zduyl
    assert ('mfu', 2) in results1zduyl
    assert ('mOm', 1) in results1zduyl
    assert len(results1zduyl) == 6

    assert ('tY', 3) in results1rlu
    assert ('jjm', 2) in results1rlu
    assert ('j', 15) in results1rlu
    assert ('jj', 4) in results1rlu
    assert ('mfu', 1) in results1rlu
    assert len(results1rlu) == 5

    assert ('tY', 2) in results1rxwz
    assert ('jjm', 1) in results1rxwz
    assert ('j', 20) in results1rxwz
    assert ('jj', 4) in results1rxwz
    assert ('mOm', 1) in results1rxwz
    assert len(results1rxwz) == 5

    assert ('tY', 4) in results1udrlwxyz
    assert ('jjm', 3) in results1udrlwxyz
    assert ('j', 40) in results1udrlwxyz
    assert ('jj', 10) in results1udrlwxyz
    assert ('mfu', 2) in results1udrlwxyz
    assert ('mOm', 2) in results1udrlwxyz
    assert len(results1udrlwxyz) == 6


from wordsearch import *


def test_find_words_in_matrix_2():
    word_list1 = ['tY', 'mOm', 'jjm', 'mfu', 'j', 'jj']
    mtr1 = []
    results1u = find_words_in_matrix(word_list1, mtr1, 'u')
    results1d = find_words_in_matrix(word_list1, mtr1, 'd')

    results1r = find_words_in_matrix(word_list1, mtr1, 'r')
    results1l = find_words_in_matrix(word_list1, mtr1, 'l')

    results1w = find_words_in_matrix(word_list1, mtr1, 'w')
    results1z = find_words_in_matrix(word_list1, mtr1, 'z')

    results1x = find_words_in_matrix(word_list1, mtr1, 'x')
    results1y = find_words_in_matrix(word_list1, mtr1, 'y')



