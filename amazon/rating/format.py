import numpy as np
import pandas as pd
import argparse


def parse_args():
    parser = argparse.ArgumentParser(description="Amazon")
    parser.add_argument('--dataset', nargs='?', default='', help='Input data')
    return parser.parse_args()


if __name__ == '__main__':
    args = parse_args()
    filename = args.dataset
    inpath = '../../data/amazon/rating/csv/' + filename + '.csv'
    outpath = '../../data/amazon/rating/alpha/' + filename[8:] + '.csv'
    infopath = '../../data/amazon/rating/info/info.txt'

    dat = pd.read_csv(inpath, ',', names=['u', 'i', 'r', 't'], engine='python')

    dat.sort_values(by=['u'], inplace=True)
    dat = dat.values
    [rows, cols] = dat.shape

    datu = [['0', '0', 0.0, 0] for i in range(rows)]
    dati = [['0', '0', 0.0, 0] for i in range(rows)]

    uindex = -1
    ustr = 'null'
    for i in range(rows):
        if ustr != dat[i, 0]:
            uindex += 1
            ustr = dat[i, 0]
        datu[i] = [uindex, dat[i, 1], dat[i, 2], dat[i, 3]]
        print('u:', i, '/', rows-1, '[', filename, ']')

    datu = pd.DataFrame(datu, columns=['u', 'i', 'r', 't'])
    datu.sort_values(by=['i'], inplace=True)
    datu = datu.values
    [rows, cols] = datu.shape

    iindex = -1
    istr = 'null'
    for i in range(rows):
        if istr != datu[i, 1]:
            iindex += 1
            istr = datu[i, 1]
        dati[i] = [datu[i, 0], iindex, datu[i, 2], datu[i, 3]]
        print('i:', i, '/', rows-1, '[', filename, ']')

    dati = pd.DataFrame(dati, columns=['u', 'i', 'r', 't'])
    dati.sort_values(by=['u', 'i'], inplace=True)
    dati.to_csv(outpath, sep=',', header=0, index=0)
    nu = max(np.array(dati['u'])) + 1
    ni = max(np.array(dati['i'])) + 1

    fin = str(filename) + '\n[u:' + str(nu) + '][i:' + \
        str(ni) + '][density:' + str(100*rows/(nu*ni)) + ']\n'
    with open(infopath, 'a') as f:
        f.write(fin)
    print('dataset:', filename)
    print('[u:', nu, '][i:', ni, '][density:', 100*rows/(nu*ni), ']')
