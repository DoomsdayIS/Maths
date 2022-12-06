class SimplexMethod:
    def __init__(self, a: list, b: list, c: list, opt="max"):
        self.eps = 1e-6
        self.a = a
        self.b = b
        self.c = c
        self.opt = opt
        self.table = []
        self.variables = []
        if self.opt == 'min':
            for i in range(len(c)):
                c[i] = -c[i]

    def _artificial_basis_table(self):
        m = len(self.b)
        n = len(self.a[0])
        if m >= n:
            raise RuntimeError("M >= N")
        for i in range(m):
            if self.b[i] < 0:
                self.b[i] = -self.b[i]
                for j in range(n):
                    self.a[i][j] *= -1

        self.variables = [("f", i) for i in range(n)]
        for i in range(m):
            self.variables.append(("b", i))

        self.table = [[0] * (n + 1) for i in range(m + 1)]
        for i in range(m):
            self.table[i][-1] = self.b[i]
            for j in range(n):
                self.table[i][j] = -self.a[i][j]
        for i in range(n + 1):
            f = 0
            for j in range(m):
                f -= self.table[j][i]
            self.table[-1][i] = f

    def _table_relax(self):
        m = len(self.table) - 1
        n = len(self.table[-1]) - 1
        max_value = self.eps
        piv_column = -1
        for i, c in enumerate(self.table[-1][:-1]):
            if c > max_value:
                max_value = c
                piv_column = i
        if piv_column == -1:
            return False

        piv_row = -1
        min_val = 10 ** 8
        for i in range(m):
            if self.table[i][piv_column] < -self.eps:
                if abs(self.table[i][-1] / self.table[i][piv_column]) < min_val:
                    min_val = abs(self.table[i][-1] / self.table[i][piv_column])
                    piv_row = i
        print(piv_column, piv_row)
        if piv_row == -1:
            raise RuntimeError("No solution. Infinity space")

        piv_elem = self.table[piv_row][piv_column]
        new_table = [([0] * (n + 1)) for i in range(m + 1)]
        for i in range(m + 1):
            for j in range(n + 1):
                if i == piv_row:
                    if j == piv_column:
                        new_table[i][j] = 1 / piv_elem
                    else:
                        new_table[i][j] = (self.table[i][j] / piv_elem) * -1
                elif j == piv_column:
                    new_table[i][j] = self.table[i][j] / piv_elem
                else:
                    new_table[i][j] = self.table[i][j] - self.table[i][piv_column] * self.table[piv_row][j] / piv_elem
        for i in range(m + 1):
            for j in range(n + 1):
                self.table[i][j] = new_table[i][j]

        ind1 = self.variables.index(('f', piv_column))
        ind2 = self.variables.index(('b', piv_row))
        self.variables[ind1], self.variables[ind2] = self.variables[ind2], self.variables[ind1]
        return True

    def _solve_table(self):
        while self._table_relax():
            print(self.variables)
            for i in self.table:
                print(i)

    def _from_art_basis_to_original(self):
        m = len(self.table) - 1
        n = len(self.table[-1]) - 1
        finish_table = [[0] * (n - m + 1) for i in range(m + 1)]
        cnt = 0

        self.variables = self.variables[:n]
        for i in range(n):
            if self.variables[i][0] == "f":
                for j in range(m):
                    finish_table[j][cnt] = self.table[j][self.variables[i][1]]
                self.variables[i] = ('f', cnt)
                cnt += 1

        for j in range(m):
            finish_table[j][-1] = self.table[j][-1]
        for i in range(n):
            if self.variables[i][0] == 'b':
                for j in range(len(finish_table[-1])):
                    finish_table[-1][j] += finish_table[self.variables[i][1]][j] * self.c[i]
            else:
                finish_table[-1][self.variables[i][1]] += self.c[i]

        self.table = finish_table

        for i in self.table:
            print(i)

    def _print_optimum(self):
        opt_func = self.table[-1][-1]
        opt_point = [0] * len(self.variables)
        for i in range(len(self.variables)):
            if self.variables[i][0] == 'b':
                opt_point[i] = self.table[self.variables[i][1]][-1]
        if self.opt == "min":
            opt_func = -opt_func
        print(self.opt + " function value is", f"{opt_func:.2f}")
        print("In point:")
        for i in range(len(opt_point)):
            print(f"{opt_point[i]:.2f}", end=' ')

    def find_optimum(self):
        try:
            self._artificial_basis_table()
        except RuntimeError as re:
            print(re)
            return

        print(self.variables)
        for i in self.table:
            print(i)

        try:
            self._solve_table()
        except RuntimeError as re:
            print(re)
            return

        if abs(self.table[-1][-1]) > self.eps:
            print("Исходная система ограничений несовместна!")
            return

        self._from_art_basis_to_original()
        try:
            self._solve_table()
        except RuntimeError as re:
            print(re)
        else:
            self._print_optimum()
