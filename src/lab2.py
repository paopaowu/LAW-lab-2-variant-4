class Variable :
    def __init__(self,v):
        self.v=v
    def FV(self):
        return self.v
    def BV(self):
        return list()
class Constant :
    def __init__(self,c):
        self.c=c
    def FV(self):
        return list()
    def BV(self):
        return list()
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
    def BV(self):
        temp=[]
        if isinstance(self.s.BV(), String):
            temp.append(self.s.BV())
        else:
            temp=temp+self.s.BV()
        if isinstance(self.t.BV(), String):
            temp.append(self.t.BV())
        else:
            temp=temp+self.s.BV()

        return temp

class Abstractions :
    def __init__(self,x,s):
        self.x=x
        self.s=s
    def FV(self):
        temp=[]
        if isinstance(self.s.FV(),String):
            temp.append(self.s.FV())
        else:
            temp=self.s.FV()
        temp.remove(self.x)
        return  temp

    def BV(self):
        temp=[]
        temp=temp+self.s.BV()
        temp.append(self.x)
        return temp
