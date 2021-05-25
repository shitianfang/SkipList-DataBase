class CNode(object):
    _cdb=None

    def __getattribute__(self, attr):
        
        if attr in ["right","down","pre","back"]:
            vid=super().__getattribute__(attr)
            print("获取键",self.key,vid)
            if not vid:
                return None
            return self._cdb._d[vid]

        return super().__getattribute__(attr)

    def __setattr__(self, attr, value):
        
        if attr in ["right","down","pre","back"]:
            if not value:
                return super().__setattr__(attr, None)

            self._cdb._d[value.id]=value 
            self._cdb._d[self.id]=self
            return super().__setattr__(attr, value.id)
        
        return super().__setattr__(attr, value)


class Logic(object):
    _cdb=None

    def _loadData(self):
        self.start=self._cdb._d["start"]
        self.end=self._cdb._d["end"]
        self.level=self._cdb._d["level"]
        print("加载数据完成")
        

    def _saveData(self):
        self._cdb._d["start"]=self.start
        self._cdb._d["end"]=self.end
        self._cdb._d["level"]=self.level
        


def register_cdb(cdb):
    CNode._cdb=cdb
    Logic._cdb=cdb
    print("注册完成",CNode._cdb,Logic._cdb)