import random,uuid
from .physical import CNode,Logic

MaxLevel=64 #最大层数，大约可存储2^64 elements
P=0.25 #增加层数的概率

class Node(CNode):
    def __init__(self,key=0,value=None):
        self.id=str(uuid.uuid1())
        self.key=key
        self.value=value
        self.right=None
        self.down=None
        self.pre=None
        self.back=None

class CSkipList(Logic):

    def __init__(self,isNew):
        if isNew:
            self.start=Node(-float("inf"))
            self.start.right=Node(float("inf"))
            self.end=self.start.right
            self.level=1
            self._saveData()
        else:
            self._loadData()

    @staticmethod
    def _checkkey(key):
        if not isinstance(key,int):
            raise KeyError("Key must be int class")
    
    def _search(self,key):

        self._checkkey(key)
        assert key!=float("inf") and key!=-float("inf")
        print("开始搜索")
        p=self.start
        print(p.key,p.right.key)
        while key>=p.right.key:
                p=p.right
        while p.down:
            p.down.pre=p
            p=p.down
            while key>=p.right.key:
                p.right.back=p
                p=p.right
        # print(p.right.key,p.value)
        return (p,True) if p.key==key else (p,False)

    def _get(self,key):
        p,b=self._search(key)
        if b:
            return p.value 
        else:
            raise KeyError("No {0} key".format(key))  

    def _insert(self,key,value):
        p,b=self._search(key)
        if b:
            p.value=value
            return

        tlevel=self.randomLevel()

        #从底部开始一层一层向上增加
        bottom_vNode=Node(key,value)
        ptr=p.right
        p.right=bottom_vNode
        bottom_vNode.right=ptr
        bottom_vNode.back=p
        down_vNode=bottom_vNode

        for i in range(2,tlevel):
            vNode=Node(key,value)
                
            if self.level<i:
                leftNode=Node(-float("inf"))
                rightNode=Node(float("inf"))
                leftNode.right=vNode
                vNode.right=rightNode
                vNode.back=leftNode
                leftNode.down=self.start
                rightNode.down=self.end

                self.start=leftNode
                self.level+=1
            else:
                while not p.pre:
                    p=p.back
                assert p.pre
                p=p.pre
                ptr=p.right
                p.right=vNode
                vNode.right=ptr
                vNode.back=p
        
            vNode.down=down_vNode
            down_vNode=vNode

        self._saveData()

    def _delete(self,key):
        p,b=self._search(key)
        if b:
            while p:
                assert p.back
                p.back.right=p.right
                p=p.pre
        else:
            raise KeyError("No {0} key".format(key))  

        self._saveData()
                                
    @staticmethod
    def randomLevel():
        level=1
        while random.random()<P and level<MaxLevel:
            level+=1
        return level
    

# if __name__=="__main__":
#     skip=CSkipList()
#     for i in range(1,1000):
#         skip._insert(i,i)
    
#     print(skip._get(3),skip._get(783),skip._get(996))
#     skip._delete(783)
#     skip._get(783)