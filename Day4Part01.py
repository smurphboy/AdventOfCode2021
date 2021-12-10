#!/usr/bin/python3

def main():
    with open('input/dayfourinput.txt', 'rt') as file:
        lines = file.readlines()
        cardlines = {}
        for idx, line in enumerate(lines):
            card = int((idx-1)/6)
            row = (idx-1) % 6
            if idx == 0:
                bingonumbers = line
            if idx == 1:
                pass
            else:
                cardlines.update({str(card)+'r'+str(row) : [line.split()]})
#        print (bingonumbers)
#        print (len(lines))
        print(cardlines)

if __name__ == '__main__':
    main()
