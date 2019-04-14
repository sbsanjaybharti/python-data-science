class matrix:
    def shape(self, a):
        num_rows =len(a)
        num_cols =len(a[0])
        return num_rows, num_cols
    def get_row(self, a, i):
        return a[i]

    def get_column(self, a, j):
        return [a_i[j] for a_i in a]

    def make_matrix(self, num_rows, num_cols, entry_fn):
        return [[entry_fn(i,j) for j in range(num_cols)] for i in range(num_rows)]

    def is_diagonal(self, i, j):
        return 1 if i == j else 0
# pyplot.show()
