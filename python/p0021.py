from collections import Counter


def main(n: int = 10_000) -> int:
    graph = Counter()
    for i in range(1, n // 2):
        for j in range(i * 2, n, i):
            graph[j] += i

    res = 0
    for k, v in graph.items():
        if graph[v] == k and k != v:
            res += k
    return res


if __name__ == "__main__":
    print(main())
