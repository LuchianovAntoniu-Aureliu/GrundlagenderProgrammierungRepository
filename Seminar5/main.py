def numar_perfect(matrix):
    for i in range()


def sum_diag(matrix):
    result = []
    for i in range(len(matrix)):
        sum_linie = 0
        for j in range(len(matrix[i])):
            if i != j:
                sum_linie += matrix[i][j]
        result.append(sum_linie == matrix[i][i])
    return result


def max_line_file(filename):
    f = open(filename, 'r')
    result = []
    for line in f:
        max_length = 0
        max_word = ''
        words = line.split(' ')
        for word in words:
            word = word.strip()
            if len(word) > max_length:
                max_word, max_length = word, len(word)
        result.append(max_length)
    f.close()
    return result


def test_max_line_file():
    assert max_line_file('data.input') == [4, 4]


def is_palindrom(word):
    return word == word[::-1]


def find_count(filename, word):
    f = open(filename, 'r')
    count = 0

    for line in f:
        words = line.split(' ')

        for w in words:
            if word == w.strip():
                count += 1

    f.close()
    return count

def count_pali(filename):
    f = open(filename, 'r')
    result = {}

    for line in f:
        word = line.split(' ')
        if is_palindrom(word):
            result[word] = find_count(filename, word.strip())

    f.close()
    return result


def test_count_pali():
    assert count_pali('data2.input') == {'anna': 2, 'abbcbba': 1, 'abba': 2}

def test_sum_diag():
    assert sum_diag([
        [4, 3, 1],
        [1, 2, 1],
        [0, 5, 1]
    ]) == [True, True, False]
    assert sum_diag([
        [1, 2, 3],
        [1, 2, 1],
        [0, 4, 0]
    ]) == [False, True, False]


def main(): pass


test_max_line_file()
test_sum_diag()
main()