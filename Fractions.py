#-*-coding:utf8;-*-

class Operators():
    
    @staticmethod
    def GCD(a,b):
        r=-1
        while(r!=0):
            r=a%b
            (a,b)=(b,r)
        return a
    
    @staticmethod    
    def LCM(a,b):
        return (a*b)/GCD(a,b)    
        

class Fraction:
    
    def __init__(self,_num,_den):
        self.num = _num
        self.den = _den
        
    def __neg__(self):
        return Fraction(-self.num , self.den)   
        
    def ToString(self):
        return "{0}/{1}".format(self.num,self.den)
        
    def Getd(self):
        return self.num/self.den
        
    def GetAsTupleOfInteger(self):
        return (self.num,self.den)
        
    def GetModularDivisionAsTupleOfIntegers(self):
        return (self.num / self.den , self.num % self.den)
        
    def IrreductibleForm(self):
        return Fraction(self.num/Operators.GCD(self.num,self.den),self.den/Operators.GCD(self.num,self.den))
    
    @staticmethod    
    def AddFrac(frac1,frac2):
        Frac1 = Fraction(frac1.num*frac2.den, frac1.den*frac2.den)
        Frac2 = Fraction(frac2.num*frac1.den, frac2.den*frac1.den)
        return Fraction(Frac1.num + Frac2.num, Frac1.den)
    
    @staticmethod
    def DiffFrac(frac1,frac2):
        return Fraction.AddFrac(frac1, -frac2)
    
    @staticmethod    
    def MultFrac(frac1,frac2):
        return Fraction(frac1.num * frac2.num, frac1.den * frac2.den)
        
    @staticmethod
    def DivFrac(frac1,frac2):
        return Fraction.MultFrac(frac1,frac2.Reverse)
    
    def Reverse(self):
        return Fraction(self.den,self.num)
        
   


