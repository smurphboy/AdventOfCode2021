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
    ohtwo = result
    seeohtwo = result
    for heading in headers: # for each column we find the counts, filter and repeat
        ohtwoones = ohtwo[heading].value_counts().to_dict()['1']
        ohtwoohes = ohtwo[heading].value_counts().to_dict()['0']
        if ohtwoones >= ohtwoohes:
            ohtwo = ohtwo[ohtwo[heading] == '1']
        else:
            ohtwo = ohtwo[ohtwo[heading] == '0']
        if seeohtwo.shape[0] > 1:
            seetwoones = seeohtwo[heading].value_counts().to_dict()['1']
            seetwoohes = seeohtwo[heading].value_counts().to_dict()['0']
            if seetwoohes <= seetwoones:
                seeohtwo = seeohtwo[seeohtwo[heading] == '0']
            else:
                seeohtwo = seeohtwo[seeohtwo[heading] == '1']
    ohtwolist = []
    seeohtwolist = []
    for heading in headers:
        ohtwolist.append(int(ohtwo.iloc[0][heading]))
        seeohtwolist.append(int(seeohtwo.iloc[0][heading]))
    ohtworesult = int("".join(str(i) for i in ohtwolist),2)
    seeohtworesult = int("".join(str(i) for i in seeohtwolist),2)
    print (ohtworesult * seeohtworesult)