def fact(n):
    if(n==1):
        return n
    else:
        return n*(fact(n,1))
      
       
    def combination(n,r):
     return fact(n)/(fact(n-r))
            
                  
    print ("program for combination")
    print("**********************/n")
    n=int(input("enter the value for n:"))
    r=int(input("enter the value for r:"))
    print(int(combination(n,r)))