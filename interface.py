from . import cshelve
from .cskiplist import CSkipList #避免循环依赖
from .physical import register_cdb

#使用接口的好处就是，可以强制执行前置或后置条件
class CDBS(object):

    def __init__(self,dbname,flag):
            self._d=cshelve.open(dbname,flag)
            #self._skip=CSkipList()
    
    def __getitem__(self, key):
        return self._skip._get(key)

    def __setitem__(self, key, value):
        return self._skip._insert(key,value)

    def __delitem__(self, key):
        return self._skip._delete(key)

    def __contains__(self, key):
        try:
            self[key]
        except KeyError:
            return False
        else:
            return True
    
    def __len__(self):
        return len(self._d)

    def commit(self):
        pass

    def close(self):
        self._d.close()

def CDB(dbname):
    isNew=False
    try:
        cdbs=CDBS(dbname,"w")
    except:
        cdbs=CDBS(dbname,"c")
        isNew=True

    register_cdb(cdbs)
    cdbs._skip=CSkipList(isNew)
    return cdbs
    




