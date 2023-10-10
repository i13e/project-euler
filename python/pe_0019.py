# https://en.wikipedia.org/wiki/Zeller's_congruence
def zeller(day, month, year):
    if month < 3:
        month += 12
        year -= 1
    K = year % 100
    J = year // 100
    day_of_week = (day + 13*(month+1)//5 + K + K//4 + J//4 - 2*J) % 7
    return day_of_week


def main():
    sundays = 0
    for year in range(1901, 2001):
        for month in range(1, 13):
            sundays += not zeller(1, month, year)
    return sundays



if __name__ == "__main__":
    print(main())
