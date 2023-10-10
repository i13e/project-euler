from itertools import product


def main():
    with open("resources/0011_grid.txt") as file:
        grid = [[int(x) for x in line.split()] for line in file]

    R, C = range(len(grid)), range(len(grid[0]))
    def get_adjacent(r: int, c: int, dr: int, dc:int) -> int:
        product = 1
        for i in range(4):
            nr, nc = r + dr * i, c + dc * i
            if nr in R and nc in C:
                product *= grid[nr][nc]
        return product

    res = 0
    for r, c in product(R, C):
        for dr, dc in product([-1, 0, 1], repeat=2):
            if dr or dc:
                res = max(res, get_adjacent(r, c, dr, dc))
    return res


if __name__ == "__main__":
    print(main())
