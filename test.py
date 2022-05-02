f=int(input("Введите целое число\n")) 
def fact(n):
     if(n==1 or n==0):
          return 1
     else:
          return n*fact(n-1)

print(f"Факториал {n} это: {fact(n)}")
