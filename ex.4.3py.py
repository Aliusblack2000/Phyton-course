def main():
  a=int(input("Number of children: "))
  b=int(input("Monthly salary: "))
  c=input("Military, or civil service(enter character Y, or y for yes, otherwise any other character)?")
 #сначала проверяем самую большую зп
  if b >= 17500:
      print("The mortgage is approved with monthly payment of %.2f."%(b*.35))
#потом среднюю
  elif b >= 15000 and (c=='y' or c=='Y'):
      print("The mortgage is approved with monthly payment of %.2f."%(b*.25))
#и самую маленькую
  elif a >= 5 and b >= 14000:     
      print("The mortgage is approved with monthly payment of %.2f."%(b*.25))
  else:
      print("Sorry, the mortgage is not approved.") 
main()
    
    
    
