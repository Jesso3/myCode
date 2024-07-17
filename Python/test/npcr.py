def factorial(n):
  if n == 1:
      return n
  else:
      return n*factorial(n-1)
  
alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

def pc(str):
   for i in range(len(str)):
       for j in alphabet:
           if str[i]==j:
               return i
               break       
              
def calc2():
  calculation = input("write your calculation in nPr or nCr form\n")
  if calculation[pc(calculation)]=='P' or calculation[pc(calculation)]=='p':
    num = int(calculation[:pc(calculation)])
    length = int(calculation[(pc(calculation)+1):])
    if length>num:
       print("there are 0 permutations of that")
    elif length==0:
       print("there is 1 permutation of that")
    elif length==num:
       print("there are",factorial(length),"permutations of that")
    else:
      perms = factorial(num)/factorial(num-length)
      print("there are",int(perms),"permutations of that")
  elif calculation[pc(calculation)]=='C' or calculation[pc(calculation)]=='c':
    num = int(calculation[:pc(calculation)])
    length = int(calculation[(pc(calculation)+1):])
    if length>num:
       print("there are 0 combinations of that")
    elif length==0 or length==num:
       print("there is 1 combination of that")
    else:
      combs = factorial(num)/(factorial(length)*factorial(num-length))
      print("there are",int(combs),"combinations of that, bruv")
  else:
    calc2()
   
def calc():
  calculation = input("write your calculation in nPr or nCr form\n")
  if calculation[pc(calculation)]=='P' or calculation[pc(calculation)]=='p':
    num = int(calculation[:pc(calculation)])
    length = int(calculation[(pc(calculation)+1):])
    if length>num:
       print("there are 0 permutations of that")
    elif length==0:
       print("there is 1 permutation of that")
    elif length==num:
       print("there are",factorial(length),"permutations of that")
    else:
      perms = factorial(num)/factorial(num-length)
      print("there are",int(perms),"permutations of that")
  elif calculation[pc(calculation)]=='C' or calculation[pc(calculation)]=='c':
    num = int(calculation[:pc(calculation)])
    length = int(calculation[(pc(calculation)+1):])
    if length>num:
       print("there are 0 combinations of that")
    elif length==0 or length==num:
       print("there is 1 combination of that")
    else:
      combs = factorial(num)/(factorial(length)*factorial(num-length))
      print("there are",int(combs),"combinations of that")
  else:
    calc2()
    
calc()
