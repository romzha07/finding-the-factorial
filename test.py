f=int(input("Введите целое число\n")) 
def fact(f):
     if(f==1 or f==0):
          return 1
     else:
          return f*fact(n-1)

print(f"Факториал {f} это: {fact(n)}")
