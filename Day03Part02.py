from pandas import DataFrame
headers = ('1', '2', '3', '4', '5', '6','7','8','9','10','11','12')
with open('input/daythreeinput.txt', 'rt') as file:
    x = 0
    y = 0
    aim = 0
    result = DataFrame(columns=(headers))
    for index, line in enumerate (file.readlines()):
        cols = [char for char in line.split()[0]]
        result.loc[index] = cols
    mostcommon = result.mode()
    gammalist = []
    epsilonlist = []
    for heading in headers:
        val = mostcommon.iloc[0][heading]
        gammalist.append(int(val))
        gamma = int("".join(str(i) for i in gammalist),2)
        epsilonlist.append(1-int(val))
        epsilon= int("".join(str(i) for i in epsilonlist),2)
    print (gamma * epsilon)