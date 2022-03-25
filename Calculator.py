print("============= < Calculator > =============\n\n")

print("**** < Enter your choice >   ****")
print("**                             **")
print("**      Addition    ==> 1      **")
print("**      Subtraction ==> 2      **")
print("**      Multiply    ==> 3      **")
print("**      Divide      ==> 4      **")
print("**      Modulus     ==> 5      **")
print("**      Exit        ==> 6      **")
print("**                             **")
print("**** < Enter your choice >   ****\n")

#use exception handling for wrong input ==> add try-except block

while True:
  choice=int(input("Enter your choice ==>"))
  if(choice==1):
    print(" ==================== <Your choice is ADDITION > ===================\n")
    n1=int(input("Enter first number as A ==>"))
    n2=int(input("Enter Second number as B ==>"))
    print("\n==================== <Your choice is ADDITION > ===================")
    add=n1+n2
    print("\n\n******************************************")
    print("**                                     **")
    print("     Addition of ",n1,"+",n2," ==>",add)
    print("**                                     **")
    print("******************************************\n\n")
  elif(choice==2):
    print(" ==================== <Your choice is SUBTRACTION > ===================\n")
    n1=int(input("Enter first number as A ==>"))
    n2=int(input("Enter Second number as B ==>"))
    print("\n==================== <Your choice is SUBTRACTION > ===================")
    sub=n1-n2
    print("\n\n********************************************")
    print("**                                        **")
    print("    Subtraction of ",n1,"-",n2," ==>",sub)
    print("**                                        **")
    print("********************************************\n\n")
  elif(choice==3):
    print(" ==================== <Your choice is MULTIPLICATION > ===================\n")
    n1=int(input("Enter first number as A ==>"))
    n2=int(input("Enter Second number as B ==>"))
    print("\n==================== <Your choice is MULTIPLICATION > ===================")
    mul=n1*n2
    print("\n\n*******************************************")
    print("**                                           **")
    print("    Multiplication of ",n1,"*",n2," ==>",mul)
    print("**                                           **")
    print("***********************************************\n\n")
  elif(choice==4):
    print(" ==================== <Your choice is DIVISION > ===================\n")
    n1=int(input("Enter first number as A ==>"))
    n2=int(input("Enter Second number as B ==>"))
    print("\n==================== <Your choice is DIVISION > ===================")
    div=n1/n2
    print("\n\n*******************************************")
    print("**                                           **")
    print("    Division of ",n1,"/",n2,"==>",div)
    print("**                                           **")
    print("***********************************************\n\n")
  elif(choice==5):
    print(" ==================== <Your choice is MODULUS > ===================\n")
    n1=int(input("Enter first number as A ==>"))
    n2=int(input("Enter Second number as B ==>"))
    print("\n==================== <Your choice is MODULUS > ===================")
    mod=n1%n2
    print("\n\n*******************************************")
    print("**                                           **")
    print("   Modulud of ",n1,"%",n2,"==>",mod)
    print("**                                           **")
    print("***********************************************\n\n")
  elif(choice==6):
    print("\n\n=============== < EXITED FROM PROGRAM > ===============\n\n")
    break
  elif(choice>=7 or choice<0):
    while True:
      print("\nNo such choice available\n")
      print(" *    * ")
      print("  *  * ")
      print("   ** ")
      print("   ** ")
      print("  *  * ")
      print(" *    * ")
      print("\nTry again \n")
      break
    
print("\n\n============= < Calculator > =============")