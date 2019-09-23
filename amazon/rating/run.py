import os
import time


if __name__ == '__main__':
    filepath = '../../data/amazon/rating/csv/'
    ls = os.listdir(filepath)
    for l in ls:
        print(l)
        fname = l[:-4]
        cname = l[8:-4]
        cmd = 'py .\\format.py --dataset ' + fname
        os.system(cmd)
        time.sleep(2)
        cmd = 'py .\\clean.py --dataset ' + cname
        os.system(cmd)
        time.sleep(2)
    time.sleep(2)
    cmd = 'py .\\fmtinfo.py'
    os.system(cmd)
    print('done')