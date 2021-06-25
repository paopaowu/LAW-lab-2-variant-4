
class Variable :

    def __init__(self,v):
        self.v=v

    def __str__(self):
        return self.v

    #return the set of free variables
    def fv(self):
        return list().append(self.v)

    # return the set of  bound  variables
    def bv(self):
        return list()

    #replace free variables with expressions
    def substitution(self,x,s):
        if self.v==x:
            return s
        return self

    # Alpha conversion
    def alpha(self,y):
        return self

    #Beta conversion
    def beta(self):
        return self

    #Eta conversion
    def eta(self):
        return self

class Constant :

    def __init__(self,c):
        self.c=c

    #return the set of free variables
    def fv(self):
        return list()

    # return the set of  bound  variables
    def bv(self):
        return list()

    #  c[t/x] = c
    def substitution(self,x,s):
        return self

    # Alpha conversion
    def alpha(self, y):
        return self

    #Beta conversion
    def beta(self):
        return self

    # Eta conversion
    def eta(self):
        return self

class Combination :

    def __init__(self,s,t):
        self.s=s
        self.t=t

    #(s t)
    def __str__(self):
        return "({} {})".format(self.s,self.t)

    #return the set of free variables
    def fv(self):
        temp=[]
        temp=temp+self.s.fv()
        temp=temp+self.s.fv()
        return temp

    # return the set of  bound  variables
    def bv(self):
        temp=[]
        temp=temp+self.s.bv()
        temp=temp+self.s.bv()
        return temp

    #(s1s2)[t/x] = s1[t/x]s2[t/x]
    def substitution(self, x, s):
        return Combination(self.s.substitution(x,s),self.t.substitution(x,s))

    # Alpha conversion
    def alpha(self,y):
        return Combination(self.s.alpha(y), self.t.alpha(y))

    #Beta conversion
    def beta(self):
        if isinstance(self.s, Abstraction):
            return self.s.s.substitution(self.s.x,self.t)
        if isinstance(self.s, Combination):
            return Combination(self.s.beta(),self.t)
        if isinstance(self.t, Abstraction) or isinstance(self.t, Combination):
            return Combination(self.s,self.t.beta())
        return self

    #Eta conversion
    def eta(self):
        if isinstance(self.s,Abstraction) and isinstance(self.s.s, Combination):
            if self.s.x==self.s.t:
                return Combination(self.s.s.s,self.t)

class Abstraction :

    def __init__(self,x,s):
        self.x=x
        self.s=s

    def __str__(self):
        return "λ{}.{}".format(self.x,self.s)

    # return the set of free variables
    def fv(self):
        temp=self.s.fv()
        temp.remove(self.x)
        return  temp

    # return the set of bound variables
    def bv(self):
        temp=[]
        temp=temp+self.s.bv()
        temp.append(self.x)
        return temp

    # replace free variables with expressions
    def substitution(self, x, s):
        if x==self.x:
            return self
        return Abstraction(self.x,self.s.substitution(x,s))

    #Alpha conversion
    def alpha(self,y):
        if self.x==y:
            return self
        return Abstraction(y,self.s.substitution(self.x,y))

    #Beta conversion
    def beta(self):
        return Abstraction(self.x, self.s.beta())

    #Eta conversion
    def eta(self):
        return Abstraction(self.x, self.s.eta())

true=Abstraction('x',Abstraction('y',Variable('x')))
false=Abstraction('x',Abstraction('y',Variable('y')))
E1_E2=Abstraction('f',Combination("E1","E2"))

def number(n):
    if n==0:
        return Variable('x')
    return Combination(Variable('f'),number(n-1))

def getNumber(n):
    return Abstraction('f',Abstraction('x',number(n)))

def suc(n):
    return Abstraction('f', Abstraction('x', Combination(Variable('f'),
                                                         Combination(Combination(n, Variable('f')),Variable('x')))))
def isZero(n):
    return Combination(Combination(n,Abstraction('x',false)),true)

def plus(m,n):
    return Abstraction('f', Abstraction('x', Combination(Combination(m, Variable('f')),
                                                         Combination(Combination(n, Variable('f')), Variable('x')))))

def mult(m,n):
    return Abstraction('f', Combination(m, Combination(n, Variable('f'))))

def pred(n):
    return Abstraction('f', Abstraction('x',Combination(Combination(Combination(
        n, Abstraction('g', Abstraction('h', Combination(Variable('h'), Combination(
            Variable('g'), Variable('f')))))),Abstraction('u', Variable('x'))), Abstraction('u', Variable('u')))))

def factorial(n):
    if str(betaConversation(isZero(n)))==str(true):
        return getNumber(1)
    return mult(n,factorial(pred(n)))

def betaConversation(n):
    pre=n
    print("-------------------------")
    while(1):
        print(n)
        n=pre.beta()
        if str(n)==str(pre):
            return n
        pre=n







