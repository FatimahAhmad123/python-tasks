#!/usr/bin/python3
def find_divisibles(inrange, div_by):
    print("Finding numbers in range {} divisible by {}".format(inrange, div_by))
    located = []
    for i in range(inrange):
        if i % div_by == 0:
            located.append(i)
    print("Done with numbers in range {} divisible by {}".format(inrange, div_by))
    return located


def main():
    divs1 = find_divisibles(508000, 34113)
    divs2 = find_divisibles(100052, 3210)
    divs3 = find_divisibles(500, 3)
    return divs1, divs2, divs3


if __name__ == "__main__":
    try:
        d1, d2, d3 = main()
        # print(d1)
    except Exception as e:
        # Handle exceptions if necessary
        pass