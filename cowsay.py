import sys
from heifer_generator import HeiferGenerator
from cow import Cow


def get_cows():
	if HeiferGenerator.cows is None:
		HeiferGenerator.cows = [None]*len(HeiferGenerator.cowImages)
		for index in range(len(HeiferGenerator.cows)):
			HeiferGenerator.cows[index] = Cow(HeiferGenerator.cowNames[index])
			HeiferGenerator.cows[index].image = HeiferGenerator.quoteLines + HeiferGenerator.cowImages[index]

	return HeiferGenerator.cows


def list_cows(cows):        # Displays the available cows from a python list of cow objects
    for i in cows:
        print(i)


def find_cow(name, cows):       # Return the cow object with the specified name, or return none
    count = 0
    for cow in cows:
        if name == cow:
            image = HeiferGenerator.cowImages[count]
            return image
        count += 1
    return None


def main():
    get_cows()

    if sys.argv[1] == '-l':
        print()
        print('Cows available: ', end="")
        list_cows(HeiferGenerator.cowNames)
    elif sys.argv[1] == '-n':
        if not find_cow(sys.argv[2], HeiferGenerator.cowNames):
            print('Could not find', sys.argv[2], 'cow!')
        else:
            print()
            for arg in sys.argv[3:]:
                print(arg, end=' ')
            print()
            print('    \\')
            print('     \\')
            print('      \\')
            print(find_cow(sys.argv[2], HeiferGenerator.cowNames))
    else:
        print()
        for arg in sys.argv[1:]:
            print(arg, end=' ')
        print()
        print('    \\')
        print('     \\')
        print('      \\')
        print(HeiferGenerator.cowImages[0])


if __name__ == '__main__':
    main()
