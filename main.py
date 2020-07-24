def main():       
  print("Hello!")    
  print("I can add two number for you")       
  num1 = eval(input("Enter one whole numbers(Ex. 52):"))    
  num2 = eval(input("Enter another whole numbers(Ex. 41):"))        
  sum = num1 + num2     
  print("The sum of the two numbers is", sum)
  if num1 > num2:
    print("The difference between the two numbers is", num1-num2)
  else:
    print("The difference between the two numbers is", num2-num1)
main()