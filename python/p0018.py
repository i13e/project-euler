def main():
    triangle = []
    with open("resources/0018_triangle.txt") as file:
        for line in file:
            triangle.append(list(map(int, line.split())))

    for row in reversed(range(len(triangle) - 1)):
        for col in range(len(triangle[row])):
            # Add the maximum of the two adjacent numbers in the row below
            triangle[row][col] += max(triangle[row + 1][col], triangle[row + 1][col + 1])
    
    # The top of the triangle now contains the maximum path sum
    return triangle[0][0]


if __name__ == "__main__":
    print(main())
