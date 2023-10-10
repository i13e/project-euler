from collections import Counter

def main(n: int = 28_123) -> int:
    graph = Counter()
    for i in range(1, n // 2):
        for j in range(i * 2, n, i):
            graph[j] += i

    abundant = [k for k, v in graph.items() if v > k]
    expressible = [0] * n
    for i in abundant:
        for j in abundant:
            if i + j < n:
                expressible[i + j] = 1
    return sum(i for i, x in enumerate(expressible) if not x)


if __name__ == "__main__":
    print(main())
