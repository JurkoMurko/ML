from random import randint, seed
# seed(0)

class Matrix:
    def __init__(self, rows, columns):
        self.rows = rows
        self.columns = columns

        self.values = []
        for i in range(self.rows):
            self.values.append([None for i in range(self.columns)])

        for i in range(self.rows):
            for j in range(self.columns):
                self.values[i][j] = 0

# -----------------------------------------------------------------------------------------------
# Special Functions

    def randomize(self):
        for i in range(self.rows):
            for j in range(self.columns):
                self.values[i][j] = randint(-10, 10) / 10  # random number between -1 and 1

    @ staticmethod
    def transpose(mate):
        result = Matrix(mate.columns, mate.rows)

        for i in range(result.rows):
            for j in range(result.columns):
                result.values[i][j] = mate.values[j][i]

        return result

    @staticmethod
    def convert(arr):
        m = Matrix(len(arr), 1)

        for i in range(m.rows):
            m.values[i][0] = arr[i]

        return m

    def convert_2(self):
        arr = []

        for i in range(self.rows):
            arr.append(self.values[i][0])

        return arr

    def map(self, fn):
        for i in range(self.rows):
            for j in range(self.columns):
                self.values[i][j] = fn(self.values[i][j])

    @staticmethod
    def map_static(mate, fn):
        m = Matrix(mate.rows, mate.columns)
        for i in range(mate.rows):
            for j in range(mate.columns):
                m.values[i][j] = fn(mate.values[i][j])

        return m

    def equals(self, mate):
        try:
            for i in range(mate.rows):
                for j in range(mate.columns):
                    self.values[i][j] = mate.values[i][j]
        except IndexError:
            print("you need the same size matrices stupid")

# -----------------------------------------------------------------
# Adding and Subtracting functions

    def matrix_plus_number(self, n):
        for i in range(self.rows):
            for j in range(self.columns):
                self.values[i][j] = self.values[i][j] + n

    def add(self, m):
        for i in range(self.rows):
            for j in range(self.columns):
                self.values[i][j] += m.values[i][j]

    @ staticmethod
    def add_matrices(m1, m2):
        m = Matrix(m1.rows, m1.columns)

        for i in range(m1.rows):
            for j in range(m1.columns):
                m.values[i][j] += m2.values[i][j]

        return m

    @staticmethod
    def subtract_matrices(m1, m2):
        m = Matrix(m1.rows, m1.columns)

        for i in range(m1.rows):
            for j in range(m1.columns):
                m.values[i][j] = m1.values[i][j] - m2.values[i][j]

        return m

# --------------------------------------------------------------------------
# Multiplication functions

    @staticmethod
    def multiply_static(a, b):
        if a.columns != b.rows:
            print('static', "can't do matrix multiplication if the rows of a don't match the columns of b")
        else:
            result = Matrix(a.rows, b.columns)

            for i in range(result.rows):
                for j in range(result.columns):

                    for h in range(b.rows):
                        result.values[i][j] = a.values[i][h] * b.values[h][j] + result.values[i][j]

            return result

    def multiply_normal(self, mate):
        if self.columns != mate.rows:
            print('normal', "can't do matrix multiplication if the rows of a don't match the columns of b")
        else:
            for i in range(self.rows):
                for j in range(mate.columns):

                    for h in range(b.rows):
                        self.values[i][j] = self.values[i][h] * mate.values[h][j] + self.values[i][j]

    def multiply_by_num(self, n):
        # if isinstance(n, int) or isinstance(n, float):  # redundant but its a cool new line that I learned so im keeping it
        for i in range(self.rows):
            for j in range(self.columns):
                self.values[i][j] *= n

        # else:
        #     print("hi")
        #     for i in range(self.rows):
        #         for j in range(self.columns):
        #             self.values[i][j] = round(self.values[i][j] * n.values[i][j], 5)

    def element_multiply_matrices(self, mate):
        for i in range(self.rows):
            for j in range(self.columns):
                self.values[i][j] *= mate.values[i][j]


# m1 = Matrix(2, 1)
# m2 = Matrix(1, 2)
# m1.randomize()
# m2.randomize()


