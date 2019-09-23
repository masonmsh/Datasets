import numpy as np


if __name__ == '__main__':
    inpath = '../../data/amazon/rating/info/info.txt'
    outpath = '../../data/amazon/rating/info/info.csv'
    with open(outpath, 'w') as f:
        f.write('dataset,u,i,density,inter\n')
    info = open(inpath)
    row = 0
    d = [0, 0, 0]
    for line in info.readlines():
        if row < 4:
            row += 1
            continue
        if row % 4 == 0:
            row += 1
            with open(outpath, 'a') as f:
                f.write(line[:-1] + ',')
        elif row % 4 == 2:
            row += 1
            sp = line.split(']')
            d[0] = sp[0][3:]
            d[1] = sp[1][3:]
            d[2] = sp[2][9:]
            with open(outpath, 'a') as f:
                f.write(d[0] + ',' + d[1] + ',' + d[2] + ',' +
                        str(round(int(d[0])*int(d[1])*float(d[2])*0.01)) + '\n')
        else:
            row += 1
