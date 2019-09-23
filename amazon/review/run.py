import os
import time


if __name__ == '__main__':
    filepath = '../../data/amazon/review/json/'
    ls = os.listdir(filepath)
    for l in ls:
        print(l)
        jname = l[:-5]
        fname = l[:-7]
        cname = l[:-7]
        cmd = 'py .\\j2csv.py --dataset ' + jname
        os.system(cmd)
        time.sleep(2)
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