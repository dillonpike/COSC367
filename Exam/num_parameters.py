def num_parameters(unit_counts):
    num = 0
    for i in range(1, len(unit_counts)):
        num += unit_counts[i] + unit_counts[i] * unit_counts[i-1]
    return num

def main():
    print(num_parameters([2, 4, 2]))
    print(num_parameters([4, 5, 3]))

if __name__ == '__main__':
    main()