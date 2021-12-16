from p1 import Solution as _Solution, Tile


def make_tile(val):
    while val > 9:
        val -= 9
    return Tile(val)


class Solution(_Solution):

    def expand(self):
        ax, ay = self.end
        mx, my = ax, ay

        # expand across x
        updates = {}
        for (x, y), t in self.matrix.items():
            v = t.h_cost
            for i in range(1, 5):
                updates[(x+((ax+1)*i), y)] = make_tile(v+i)
            mx = max(mx, x+((ax+1)*i))
        self.matrix.update(updates)

        # expand down y
        updates = {}
        for (x, y), t in self.matrix.items():
            v = t.h_cost
            for i in range(1, 5):
                updates[(x, y+((ay+1)*i))] = make_tile(v+i)
            my = max(my, y+((ay+1)*i))
        self.matrix.update(updates)
        self.end = (mx, my)

    def solve(self, data) -> int:
        self.load(data)
        self.expand()
        return self.find_best_cost(self.start, self.end)


if __name__ == '__main__':
    Solution.run(source='input.txt')
