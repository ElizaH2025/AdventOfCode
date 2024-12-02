# ownerproof-4494691-1733145466-ebe48907f1a2
# write a FUNCTION for each day's puzzle
def day01():
    print('Day #1')
    # set up empty list
    left = []
    right = []
    # Read TXT file
    file = open('day1input.txt', 'r')
    data = file.read()
    print(data)

    split = [line.strip() for line in file]
    for line in split:
        left.append(line.split('   ')[0])
        right.append(line.split('   ')[1])
    # Pair smallest number in LEFT with smallest number in RIGHT list
    sorted_left = sorted(left)
    sorted_right = sorted(right)
    # iterate from smallest in each to largest
    for (l, r) in zip(sorted_left, sorted_right ):
        print(l, r)



def main():
    # UPDATE this function call for each puzle
    day01()

if __name__ == "__main__":
   main()