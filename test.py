maxLen = 0
with open("train.txt") as fi:
    for line in fi.readlines():
        if line.strip().split(',')[1] == 'notdga' and len(line.strip().split(',')[0])>maxLen:
            maxLen = len(line.strip().split(',')[0])
wr = open("result.txt",'w')
with open("test.txt") as ft:
    for line in ft.readlines():
        if len(line.strip().split(',')[0])>maxLen:
            wr.write(line.strip()+",dga\n")
        else:
            wr.write(line.strip()+",notdga\n")
wr.close()
