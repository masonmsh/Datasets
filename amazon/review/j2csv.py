import json
import pandas as pd
import argparse


def parse_args():
    parser = argparse.ArgumentParser(description="Amazon")
    parser.add_argument('--dataset', nargs='?', default='', help='Input data')
    return parser.parse_args()


if __name__ == '__main__':
    args = parse_args()
    filename = args.dataset
    inpath = '../../data/amazon/review/json/' + filename + '.json'
    outpath = '../../data/amazon/review/csv/' + filename[:-2] + '.csv'

    js = open(inpath)
    rows = 0
    for line in js.readlines():
        if line != '':
            rows += 1
    print(rows)

    dat = [['0', '0', 0.0, 0] for i in range(rows)]

    js = open(inpath)
    row = 0
    for line in js.readlines():
        js = json.loads(line)
        dat[row] = [js['reviewerID'], js['asin'],
                    js['overall'], js['unixReviewTime']]
        row += 1

    dat = pd.DataFrame(dat, columns=['u', 'i', 'r', 't'])
    dat.to_csv(outpath, sep=',', header=0, index=0)
