class Variable :
    def __init__(self,v):
        self.v=v
    def FV(self):
        return self.v
class Constant :
    def __init__(self,c):
        self.c=c
    def FV(self):
        return None

class Combination :
    def __init__(self,s,t):
        self.s=s
        self.t=t
    def FV(self):
        temp=[]
        if isinstance(self.s.FV(), String):
            temp.append(self.s.FV())
        else:
            temp=temp+self.s.FV()
        if isinstance(self.t.FV(), String):
            temp.append(self.t.FV())
        else:
            temp=temp+self.s.FV()

        return temp

class Abstractions :
    def __init__(self,x,s):
        self.x=x
        self.s=s
    def FV(self):
        list=[]
        if temp==None:
            return None
        if isinstance(self.s.FV(),String):
            list.append(self.s.FV())
        else:
            list=self.s.FV()
        list.remove(self.x)
        return  list

