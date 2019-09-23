import numpy as np
import pandas as pd
import argparse
import random


def parse_args():
    parser = argparse.ArgumentParser(description="Amazon")
    parser.add_argument('--dataset', nargs='?', default='', help='Input data')
    parser.add_argument('--num_neg', type=int, default=99, help='Negative')
    return parser.parse_args()


if __name__ == '__main__':
    args = parse_args()
    filename = args.dataset
    num_neg = args.num_neg
    inpath = '../../data/amazon/review/beta/' + filename + '.csv'
    trainpath = '../../data/amazon/review/ncf/' + filename + '.train.rating'
    testpath = '../../data/amazon/review/ncf/' + filename + '.test.rating'
    negapath = '../../data/amazon/review/ncf/' + filename + '.test.negative'

    df = pd.read_csv(inpath, ',', names=[
                     'u', 'i', 'r', 't'], engine='python', dtype=int)
    df.sort_values(by=['u', 't'], ascending=[True, False], inplace=True)
    maxu = df['u'].max() + 1
    maxi = df['i'].max() + 1
    dat = df.values
    [rows, cols] = dat.shape

    train = np.zeros((rows-maxu, cols), dtype=int)
    test = np.zeros((maxu, cols), dtype=int)
    neg = np.zeros((maxu, num_neg), dtype=int)
    uid = 0
    itest = 0
    itrain = 0
    inter = []
    for i in range(rows):
        if uid == dat[i, 0]:
            test[itest] = dat[i]
            if uid > 0:
                ne = random.sample(set(range(maxi)) - set(inter), num_neg)
                neg[uid-1] = ne
            inter = [dat[i, 1]]
            itest += 1
            uid += 1
        else:
            train[itrain] = dat[i]
            inter.append(dat[i, 1])
            itrain += 1
        print('t:', i, '/', rows-1, '[', filename, ']')
    ne = random.sample(set(range(maxi)) - set(inter), num_neg)
    neg[uid-1] = ne

    with open(negapath, 'w') as f:
        for i in range(maxu):
            f.write('(' + str(i) + ',' + str(test[i, 1]) + ')')
            for j in range(num_neg):
                f.write('\t' + str(neg[i, j]))
            f.write('\n')

    train = pd.DataFrame(train, columns=['u', 'i', 'r', 't'], dtype=int)
    train.sort_values(by=['u', 't'], ascending=[True, False], inplace=True)
    train.to_csv(trainpath, sep='\t', header=0, index=0)

    test = pd.DataFrame(test, columns=['u', 'i', 'r', 't'], dtype=int)
    test.sort_values(by=['u'], inplace=True)
    test.to_csv(testpath, sep='\t', header=0, index=0)
