class Variable :
    def __init__(self,v):
        self.v=v
    def fv(self):
        return self.v
    def bv(self):
        return list()
    def substitution(self,x,s):
        if self.v==x.v:
            return s
        return self
class Constant :
    def __init__(self,c):
        self.c=c
    def fv(self):
        return list()
    def bv(self):
        return list()
    def substitution(self,x,s):

        return self
class Combination :
    def __init__(self,s,t):
        self.s=s
        self.t=t
    def fv(self):
        temp=[]
        if isinstance(self.s.fv(), String):
            temp.append(self.s.fv())
        else:
            temp=temp+self.s.fv()
        if isinstance(self.t.fv(), String):
            temp.append(self.t.fv())
        else:
            temp=temp+self.s.fv()

        return temp
    def bv(self):
        temp=[]
        if isinstance(self.s.bv(), String):
            temp.append(self.s.bv())
        else:
            temp=temp+self.s.bv()
        if isinstance(self.t.bv(), String):
            temp.append(self.t.bv())
        else:
            temp=temp+self.s.bv()

        return temp

    def substitution(self, x, s):

        return Combination(self.s.substitution(x,s),self.t.substitution(x,s))

    def beta(self):
        return self.s.s.subtitution(self.s.x,t)
    def eta(self):
        if isinstance(self.s,Abstraction) and isinstance(self.s.s, Combination):
            if self.s.x==self.s.t:
                return Combination(self.s.s.s,self.t)

class Abstraction :
    def __init__(self,x,s):
        self.x=x
        self.s=s
    def fv(self):
        temp=[]
        if isinstance(self.s.fv(),String):
            temp.append(self.s.fv())
        else:
            temp=self.s.fv()
        temp.remove(self.x)
        return  temp

    def bv(self):
        temp=[]
        temp=temp+self.s.bv()
        temp.append(self.x)
        return temp
    def substitution(self, x, s):
        if x.v==self.x:
            return self
        return Abstraction(self.x,self.s.substitution(x,s))

    def alpha(self,y):
        if self.x==y:
            return self
        return Abstraction(y,self.s.substitution(x,y))
