#!/usr/bin/python3

def main():
    with open('input/dayfourinput.txt', 'rt') as file:
        lines = file.readlines()

        for idx, line in enumerate(lines):
            if idx == 0:
                bingonumbers = line
            else:
                if (idx-1) % 6 == 1:
                    print (idx, 'line 1 of card', int(idx / 6), line)

        print (bingonumbers)
        print (len(lines))


if __name__ == '__main__':
    main()
