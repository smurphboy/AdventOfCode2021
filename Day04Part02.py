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
                cardlines.update({str(card).zfill(2)+'r'+str(row) : line.split()}) # create row
                for cell in range(5):
                    #print (idx, card, row, cell)
                    if row == 0:
                        cardlines.update({str(card).zfill(2)+'c'+str(cell) : [line.split()[cell]]})
                    else:
                        cardlines[str(card).zfill(2)+'c'+str(cell)].append(line.split()[cell])
#        now we find if our bingo card has a complete line
#        we make a set of first five bingo numbers and check all the rows and columns
#        when we find a line, we need to pop all the rows and columns of that card

        numbers = bingonumbers.split(',')
        for hand in range(len(numbers)):
            handnumbers = set(numbers[0:hand])
            if len(cardlines) > 1:
                for key in list(cardlines):
                        if handnumbers.issuperset(cardlines[key]):
                            for i in range(5):
                                del cardlines[key[:2]+'r'+ str(i)]
                                del cardlines[key[:2]+'c'+ str(i)]
                                print(key[:2]+'r'+ str(i))
                                print(key[:2]+'c'+ str(i))
        print(cardlines)     

if __name__ == '__main__':
    main()
