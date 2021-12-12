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
#        print (bingonumbers)
#        print (len(lines))
#        print(cardlines)
#        now we find if our bingo card has a complete line
#        we make a set of first five bingo numbers and check all the rows and columns

        numbers = bingonumbers.split(',')
        done = False
        for hand in range(len(numbers)):
            if done == False:
                handnumbers = set(numbers[0:hand])
                for key in cardlines:
                    if done == False:
                        if handnumbers.issuperset(cardlines[key]):
                            winningcard = key[:2]
                            winninghand = numbers[0:hand]
                            done = True
#        we have the winning line, now we score the card
        score = 0
        for key in cardlines:
            if key[0:2] == winningcard:
                if key[2] == 'r': # we don't want to double count rows and columns
                    for num in cardlines[key]:
                        if num not in winninghand:
                            score += int(num)
        finalscore = (score * int(winninghand[-1]))
        print (finalscore)



        

if __name__ == '__main__':
    main()
