from __future__ import print_function
import sys
from .interface import CDB


OK=0
BAD_ARGS = 1
BAD_VERB = 2
BAD_KEY = 3


def usage():
    print("Usage:", file=sys.stderr)
    print("\tpython -m cdb.tool DBNAME get KEY", file=sys.stderr)
    print("\tpython -m cdb.tool DBNAME set KEY VALUE", file=sys.stderr)
    print("\tpython -m cdb.tool DBNAME delete KEY", file=sys.stderr)

def main(argv):
    if not (4<=len(argv)<=5):
        usage()
        return BAD_ARGS
    # python -m dbdb.tool example.db get foo
    # args第一个参数是文件名dbdb.tool，此处过滤
    dbname,verb,key,value=(argv[1:]+[None])[:4]
    try:
        key=int(key)
    except KeyError:
        print("Key Must Be int Class")
    if verb not in {'get','set','del'}:
        usage()
        return BAD_VERB

    cdb=CDB(dbname)

    try:
        if verb=='get':
            sys.stdout.write(cdb[key])
        elif verb=='set':
            cdb[key]=value
        elif verb=='del':
            del cdb[key]
    except KeyError:
        print("Key not found",file=sys.stderr)
        return BAD_KEY
    return OK

if __name__ == '__main__':
    sys.exit(main(sys.argv))