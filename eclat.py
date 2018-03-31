import time
import decimal
from sys import argv
from multiprocessing import Pool
def eclat(prefix, items):
        while items:
            i,itids = items.pop()
            isupp = len(itids)
            if isupp/trans >= minsup:
                printstuff = prefix+[i]
                print("~~~~~~~")
                print(sorted(printstuff,key=int))
                print_str = str(','.join(sorted(printstuff,key=int)))+':'+str((D(isupp)/D(trans)).quantize(D('0.0001'),rounding=decimal.ROUND_UP))+'\n'
                writefile.write(print_str)
                suffix = []
                for j, objecttids in items:
                    jtids = itids & objecttids
                    if (len(jtids)/trans) >= minsup:
                        suffix.append((j,jtids))
            eclat(prefix + [i], sorted(suffix, key=lambda item: len(item[1])))


def split(line):
    left, right = line.split(":")
    left = left.split(",")
    left = list(map(int, left))
    return len(left), left, right

if __name__ == '__main__':
    D = decimal.Decimal
    data = {}
    minsup = float(argv[1])
    print(minsup)
    trans = 0
    f = open(argv[2], 'r')
    filename = str(argv[3])
    lst = list()
    newlist = []
    for row in f:
        trans += 1
        for item in row.split(','):
            item = item.strip('\n')

            if item not in data:
                data[item] = set()
            data[item].add(trans)
    f.close()
    start = time.clock()
    writefile = open(filename,"w",encoding="utf-8")
    eclat([],  sorted(data.items(), key=lambda item: len(item[1])))
    writefile.close()

    with open(filename, 'r', encoding='utf-8') as readfile:
        lines = readfile.read().splitlines()
        pool = Pool(5)
        compares = pool.map(split,lines)
        lines = sorted(range(len(lines)), key=lambda i:compares[i])
        print("~")

    writefile2 = open(filename,"w",encoding="utf-8")
    for line in lines:
        strline = str(line)+'\n'
        writefile2.write(strline)
        print(line)

    """
    readfile = open(filename,'r',encoding='utf-8')
    for line in readfile:
        lst+=line.split()
    readfile.close()
    lst = sorted(lst,key = lambda s:(len(s.split(':')[0]),s))
    #print(lst)
    for item in lst:
        newlist.append(item)
    #newlist = sorted(newlist,key=lambda item: (len(item.split(':')[0].split(',')),item))
    writefile2 = open(filename,"w",encoding="utf-8")
    for line in newlist:
        linestr = str(line)+'\n'
        #print(linestr)
        writefile2.write(linestr)
    """
    writefile2.close()
    end = time.clock()

    print ("run time: %f s" % (end-start))