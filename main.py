class ConstMatrix:
    def __init__(self):
        self.row = 16
        self.column = 16
        self.matrix = [
            [1, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0],
            [0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 1, 1, 1, 0, 0],
            [1, 1, 0, 1, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0],
            [1, 1, 0, 1, 1, 0, 0, 1, 1, 1, 1, 0, 0, 0, 1, 0],
            [0, 1, 1, 0, 1, 1, 0, 0, 0, 0, 1, 1, 0, 1, 0, 1],
            [1, 1, 0, 1, 0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 1, 1],
            [0, 0, 0, 1, 0, 1, 1, 1, 0, 0, 0, 1, 0, 1, 0, 0],
            [0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 1, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 1, 0, 1, 1, 0, 0, 0, 0, 1],
            [0, 1, 1, 0, 1, 1, 0, 1, 0, 0, 0, 0, 1, 1, 1, 1],
            [0, 1, 0, 0, 0, 1, 1, 0, 0, 1, 0, 1, 1, 1, 1, 1],
            [1, 0, 0, 1, 0, 1, 1, 1, 0, 1, 1, 0, 1, 0, 1, 0],
            [0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0],
            [1, 0, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 1],
            [1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1],
            [0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0]
        ]

    def get_value(self, row, col):
        return self.matrix[row][col]

    def set_value(self, row, col, new_value):
        self.matrix[row][col] = new_value

    def print_matrix(self):
        for i in range(self.row):
            for j in range(self.column):
                print(self.matrix[i][j], end=" ")
            print()

    def get_word_from_matrix(self, index):
        word = ""
        for i in range(self.column):
            x = (index + i) % self.column
            word += str(self.matrix[x][index])
        return word

    def get_address_row_word(self, index):
        row_word = ""
        for i in range(self.column):
            row_index = (index + i) % self.column
            row_word += str(self.matrix[row_index][i])
        return row_word

    def set_word(self, index, new_word):
        for i in range(16):
            value = int(new_word[i])
            self.matrix[i][index] = value

    def find_word_position(self, searched_word, condition):
        searched_num = int(searched_word, 2)

        min_num = float('inf')
        max_num = float('-inf')
        min_index = -1
        max_index = -1

        g = False
        l = False

        for i in range(self.row):
            word = self.get_word_from_matrix(i)
            word_num = int(word, 2)

            if condition and word_num > searched_num:
                if word_num < min_num:
                    min_num = word_num
                    min_index = i
                    g = True
            elif not condition and word_num < searched_num:
                if word_num > max_num:
                    max_num = word_num
                    max_index = i
                    l = True

        if g and min_index != -1:
            return min_index
        elif l and max_index != -1:
            return max_index

        return -1

    def f1_function(self, first_word, second_word):
        result = ""
        for i in range(len(first_word)):
            if first_word[i] == '1' and second_word[i] == '1':
                result += '1'
            else:
                result += '0'
        return result

    def f14_function(self, first_word, second_word):
        result = ""
        for i in range(len(first_word)):
            if first_word[i] == '1' and second_word[i] == '1':
                result += '0'
            else:
                result += '1'
        return result

    def f3_function(self, first_word, second_word):
        return first_word

    def f12_function(self, first_word, second_word):
        result = ""
        for i in range(len(first_word)):
            if first_word[i] == '1':
                result += '0'
            else:
                result += '1'
        return result

    def summ_ab(self, key):
        result = ""
        index = 0
        for i in range(self.row):
            word = self.get_word_from_matrix(i)
            if word.startswith(key):
                result += word + " "
                index = i
        if len(result) > 16:
            result = result[:16]

        V = result[:3]
        A = result[3:7]
        B = result[7:11]
        S = result[11:16]

        numA = int(A, 2)
        numB = int(B, 2)

        sum_ab = numA + numB

        S = format(sum_ab, '05b')
        result = V + A + B + S
        self.set_word(index, result)
        return result


cm = ConstMatrix()
cm.print_matrix()
print(cm.get_word_from_matrix(1))
print(cm.summ_ab('110'))
