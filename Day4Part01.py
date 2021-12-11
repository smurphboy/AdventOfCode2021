#!/usr/bin/python3

def main():
    with open('input/dayfourinput.txt', 'rt') as file:
        lines = file.readlines()
        cardlines = {}
        for idx, line in enumerate(lines):
            card = int((idx-1)/6)
            row = (idx-2) % 6
            if idx == 0:
                bingonumbers = line
            elif idx == 1:
                pass
            elif row == 5:
                pass
            else:
                cardlines.update({str(card)+'r'+str(row) : line.split()}) # create row
                for cell in range(5):
                    print (idx, card, row, cell)
                    if row == 0:
                        cardlines.update({str(card)+'c'+str(cell) : [line.split()[cell]]})
                    else:
                        cardlines[str(card)+'c'+str(cell)].append(line.split()[cell])
#        print (bingonumbers)
#        print (len(lines))
        print(cardlines)

if __name__ == '__main__':
    main()
