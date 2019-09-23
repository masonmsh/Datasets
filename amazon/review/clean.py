import numpy as np
import pandas as pd
import argparse
from collections import Counter


def parse_args():
    parser = argparse.ArgumentParser(description="Amazon")
    parser.add_argument('--dataset', nargs='?', default='', help='Input data')
    parser.add_argument('--drop', type=int, default=5, help='Drop threshold')
    return parser.parse_args()


if __name__ == '__main__':
    args = parse_args()
    filename = args.dataset
    drop = args.drop
    inpath = '../../data/amazon/review/alpha/' + filename + '.csv'
    outpath = '../../data/amazon/review/beta/' + filename + '.csv'
    infopath = '../../data/amazon/review/info/info.txt'

    df = pd.read_csv(inpath, ',', names=[
                     'u', 'i', 'r', 't'], engine='python', dtype=int)

    df.sort_values(by=['u', 'i'], inplace=True)
    dat = df.values
    dic = Counter(dat[:, 0])
    m = []
    u = df['u'].max() + 1
    for key in dic:
        if dic[key] < drop:
            m.append(key)
        print('d:', key, '/', u-1, '[', filename, ']')
    dat = df.drop(df[df['u'].isin(m)].index)

    dat.sort_values(by=['u'], inplace=True)
    dat = dat.values
    [rows, cols] = dat.shape

    datu = [[-1, -1, -1, -1] for i in range(rows)]
    dati = [[-1, -1, -1, -1] for i in range(rows)]

    uindex = -1
    ustr = -1
    for i in range(rows):
        if ustr != dat[i, 0]:
            uindex += 1
            ustr = dat[i, 0]
        datu[i] = [uindex, dat[i, 1], 1, dat[i, 3]]
        print('u:', i, '/', rows-1, '[', filename, ']')

    datu = pd.DataFrame(datu, columns=['u', 'i', 'r', 't'])
    datu.sort_values(by=['i'], inplace=True)
    datu = datu.values
    [rows, cols] = datu.shape

    iindex = -1
    istr = -1
    for i in range(rows):
        if istr != datu[i, 1]:
            iindex += 1
            istr = datu[i, 1]
        dati[i] = [datu[i, 0], iindex, 1, datu[i, 3]]
        print('i:', i, '/', rows-1, '[', filename, ']')

    dati = pd.DataFrame(dati, columns=['u', 'i', 'r', 't'])
    dati.sort_values(by=['u', 'i'], inplace=True)
    dati.to_csv(outpath, sep=',', header=0, index=0)
    nu = max(np.array(dati['u'])) + 1
    ni = max(np.array(dati['i'])) + 1

    fin = '[u:' + str(nu) + '][i:' + str(ni) + \
        '][density:' + str(100*rows/(nu*ni)) + ']\n\n'
    with open(infopath, 'a') as f:
        f.write(fin)
    print('dataset:', filename)
    print('[u:', nu, '][i:', ni, '][density:', 100*rows/(nu*ni), ']')
