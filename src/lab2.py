class Variable :

    def __init__(self,v):
        self.v=v

    def fv(self):
        return list().append(self.v)

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
        temp=temp+self.s.fv()
        temp=temp+self.s.fv()
        return temp

    def bv(self):
        temp=[]
        temp=temp+self.s.bv()
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

true=Abstraction('x',Abstraction('y',Variable('x')))
false=Abstraction('x',Abstraction('y',Variable('y')))
E1_E2=Abstraction(f,Combination("E1","E2"))

def number(n):
    if n==0:
        return Variable('x')
    return Combination(Variable('f'),number(n-1))

def getNumber(n):
    return Abstraction('f',Abstraction('x',number(n)))

def suc(n):
    return Abstraction('f', Abstraction('x', Combination(Variable('f'), Combination(Combination(n, Variable('f')), Variable('x')))))
def isZero(n):
    return Combination(Combination(n,Abstraction('x',false)),true)

def plus(m,n):
    return Abstraction('f', Abstraction('x', Combination(Combination(m, Variable('f')),Combination(Combination(n, Variable('f')), Variable('x')))))

def mult(m,n):
    return Abstraction('f', Combination(m, Combination(n, Variable('f'))))

def pred(n):
    return Abstraction('f', Abstraction('x', Combination(Combination(Combination(n, Abstraction('g', Abstraction('h', Combination(Variable('h'), Combination(Variable('g'), Variable('f')))))), Abstraction('u', Variable('x'))), Abstraction('u', Variable('u')))))














