import os
from time import sleep
import math
print("\n\n============= < SCIENTIFIC CALCULATOR > =============\n")

# import math for all math built-in functions
# from time import sleep:- to pause some time to dispaly the outpout
# import os :- to clear screen ==> os.system('cls')

# Calling options() function for user choice of operation :- also we can call it from athor file
# Extra:-  from optionsfile import* ==> def options(): ==> function should be present in the optionsfile (file)
# function
def options():
    print("**** < Enter your choice >   ******************************************************")
    print("**                              		 ")
    print("**      Add (A+B) \t\t\t\t==> 1      ")
    print("**      Subtract (A-B) \t\t\t\t==> 2      ")
    print("**      Multiply (A*B) \t\t\t\t==> 3      ")
    print("**      Divide (A/B) \t\t\t\t==> 4      ")
    print("**      Floor Division (A//B) \t\t\t==> 5      ")
    print("**      Modulus (A%B) \t\t\t\t==> 6      ")
    print("**      Exponentiation (A**B) \t\t\t==> 7      ")
    print("**      Get table (2*1=2) \t\t\t==> 8      ")
    print("**      Get Square root (A^B) \t\t\t==> 9      ")
    print("**      Get Absolute value (-9 ==> 9) \t\t==> 10      ")
    print("**      Find Greater number (A>B or A<B) \t==> 11      ")
    print("**      Get Factorial of number  \t\t==> 12      ")
    print("**      Swap Two numbers  \t\t\t==> 13      ")
    print("**      Exit \t\t\t\t\t==> 14      ")
    print("**                             		 ")
    print("**** < Enter your choice >   ******************************************************\n\n")

# While loop ==> for using the operation again and agin until user enters 6 to exit(STOP) the program,
# or show msg for  any invalid input (choice) #

while True:

# < Exception handling:- for choice if choice is greater than 6 then, msg will be shown that invalid
# input or user enters any string as choice then msg will be shown that enter a number instead of
# string value or any special character ?? // ! @ anything like sihbhsfb@63673 :- msg will be shown taht choice  is invalid and enter choice again or try again for any operation > #

    try:
        options()
        choice = input("Enter your choice ==>")
        choice = int(choice)
        os.system('cls')
        sleep(0.2)
# ==================== < ADDITION > =================== #
        if(choice == 1):
            print("\n==================== <Your choice is ADDITION > ===================\n")
            n1 = input("Enter first number as A ==>")
            an1 = n1
            if(an1 == ""):
                print("\nA is empty !!")
                print("Try Again\n")
            n2 = input("Enter Second number as B ==>")
            bn2 = n2
            if(bn2 == ""):
                print("\nB is empty !!")
                print("Try Again\n")
            try:
                # Take input in floating :-
                na1 = float(n1)
                nb2 = float(n2)
                add = na1+nb2
                print("\n\n*********************************************")
                print("**                                         ")
                print("**     ADDITION of ", na1, "+", nb2, " ==>",  add)
                print("**                                         ")
                print("*********************************************\n\n")
                print("\n==================== <Your choice was ADDITION > ===================\n")
            except ValueError:
                nn1 = n1.isalpha()
                nn2 = n2.isalpha()
                if(nn1 == True and nn2 == True):
                    print("Both", n1, " and ", n2, " are string")
                    print("Invlid input")
                    print("Try again")
                    print("\n==================== <Your choice was ADDITION > ===================\n")
                elif(nn1 == False and nn2 == False):
                    print("Enter the numbers again ==> Invlid input")
                    print("Try again")
                    print("\n==================== <Your choice was ADDITION > ===================\n")
                else:
                    if(nn1 == True):
                        print(n1, " is a String")
                        print("Invalid input")
                        print("Try again")
                        print("\n==================== <Your choice was ADDITION > ===================\n")
                    elif(nn2 == True):
                        print(n2, " is a String")
                        print("Invalid input")
                        print("Try again")
                        print("\n==================== <Your choice was ADDITION > ===================\n")
# ==================== < ADDITION > =================== #

# ==================== < SUBTRACTION > =================== #
        elif(choice == 2):
            print("\n==================== < Your choice is SUBTRACTION > ===================\n")
            n1 = input("Enter first number as A ==>")
            an1 = n1
            if(an1 == ""):
                print("\nA is empty !!")
                print("Try Again\n")
            n2 = input("Enter Second number as B ==>")
            bn2 = n2
            if(bn2 == ""):
                print("\nB is empty !!")
                print("Try Again\n")
            try:
                na1 = float(n1)
                nb2 = float(n2)
                sub = na1-nb2
                print("\n\n*********************************************")
                print("**                                        ")
                print("**   SUBTRACTION of ", na1, "-", nb2, " ==>", sub)
                print("**                                         ")
                print("*********************************************\n\n")
                print("\n==================== < Your choice was SUBTRACTION > ===================\n")
            except ValueError:                          
                nn1 = n1.isalpha()
                nn2 = n2.isalpha()
                if(nn1 == True and nn2 == True):
                    print("Both", n1, " and ", n2, " are string")
                    print("Invlid input")
                    print("Try again")
                    print("\n==================== < Your choice was SUBTRACTION > ===================\n")
                elif(nn1 == False and nn2 == False):
                    print("Enter the numbers again ==> Invlid input")
                    print("Try again")
                    print("\n==================== <Your choice was ADDITION > ===================\n")
                else:
                    if(nn1 == True):
                        print(n1, " is a String")
                        print("Invalid input")
                        print("Try again")
                        print("\n==================== < Your choice was SUBTRACTION > ===================\n")
                    elif(nn2 == True):
                        print(n2, " is a String")
                        print("Invalid input")
                        print("Try again")
                        print("\n==================== <Your choice was SUBTRACTION > ===================\n")
# ==================== < SUBTRACTION > =================== #

# ==================== < MULTIPLICATION > =================== #
        elif(choice == 3):
            print("\n==================== < Your choice is MULTIPLICATION > ===================\n")
            n1 = input("Enter first number as A ==>")
            an1 = n1
            if(an1 == ""):
                print("\nA is empty !!")
                print("Try Again\n")
            n2 = input("Enter Second number as B ==>")
            bn2 = n2
            if(bn2 == ""):
                print("\nB is empty !!")
                print("Try Again\n")
            try:
                na1 = float(n1)
                nb2 = float(n2)
                mul = na1*nb2
                print("\n\n***********************************************")
                print("**                                           ")
                print("**   MULTIPLICATION of ", na1, "*", nb2, " ==>", mul)
                print("**                                           ")
                print("***********************************************\n\n")
                print("\n==================== < Your choice was MULTIPLICATION > ===================\n")
            except ValueError:
                nn1 = n1.isalpha()
                nn2 = n2.isalpha()
                if(nn1 == True and nn2 == True):
                    print("Both", n1, " and ", n2, " are string")
                    print("Invlid input")
                    print("Try again")
                    print("\n==================== < Your choice was MULTIPLICATION  > ===================\n")
                elif(nn1 == False and nn2 == False):
                    print("Enter the numbers again ==> Invlid input")
                    print("Try again")
                    print("\n==================== <Your choice was ADDITION > ===================\n")
                else:
                    if(nn1 == True):
                        print(n1, " is a String")
                        print("Invalid input")
                        print("Try again")
                        print("\n==================== < Your choice was MULTIPLICATION  > ===================\n")
                    elif(nn2 == True):
                        print(n2, " is a String")
                        print("Invalid input")
                        print("Try again")
                        print("\n==================== <Your choice was MULTIPLICATION  > ===================\n")
# ==================== < MULTIPLICATION > =================== #

# ==================== < DIVISION > =================== #
        elif(choice == 4):
            print("\n==================== < Your choice is DIVISION > ===================\n")
            n1 = input("Enter first number as A ==>")
            an1 = n1
            if(an1 == ""):
                print("\nA is empty !!")
                print("Try Again\n")
            n2 = input("Enter Second number as B ==>")
            bn2 = n2
            if(bn2 == ""):
                print("\nB is empty !!")
                print("Try Again\n")
            try:
                na1 = float(n1)
                nb2 = float(n2)
                div = na1/nb2
                print("\n\n***********************************************")
                print("**                                           ")
                print("**   DIVISION (With decimal value) of ",na1, "/", nb2, " ==>", div)
                print("**                                           ")
                print("***********************************************\n\n")
                print("\n==================== < Your choice was DIVISION > ===================\n")
            except ValueError:
                nn1 = n1.isalpha()
                nn2 = n2.isalpha()
                if(nn1 == True and nn2 == True):
                    print("Both", n1, " and ", n2, " are string")
                    print("Invlid input")
                    print("Try again")
                    print("\n==================== < Your choice was DIVISION > ===================\n")
                elif(nn1 == False and nn2 == False):
                    print("Enter the numbers again ==> Invlid input")
                    print("Try again")
                    print("\n==================== <Your choice was DIVISION > ===================\n")
                else:
                    if(nn1 == True):
                        print(n1, " is a String")
                        print("Invalid input")
                        print("Try again")
                        print("\n=================== < Your choice was DIVISION > ===================\n")
                    elif(nn2 == True):
                        print(n2, " is a String")
                        print("Invalid input")
                        print("Try again")
                        print("\n==================== <Your choice was DIVISION > ===================\n")
# ==================== < DIVISION > =================== #

# ==================== < Floor Division > =================== #
        elif(choice == 5):
            print("\n==================== < Your choice is Floor Division > ===================\n")
            n1 = input("Enter first number as A ==>")
            an1 = n1
            if(an1 == ""):
                print("\nA is empty !!")
                print("Try Again\n")
            n2 = input("Enter Second number as B ==>")
            bn2 = n2
            if(bn2 == ""):
                print("\nB is empty !!")
                print("Try Again\n")
            try:
                na1 = float(n1)
                nb2 = float(n2)
                div = na1//nb2
                print("\n\n***********************************************")
                print("**                                           ")
                print("**   Floor Division (Without decimal value) of ",na1, "//", nb2, " ==>", div)
                print("**                                           ")
                print("***********************************************\n\n")
                print("\n==================== < Your choice was Floor Division > ===================\n")
            except ValueError:
                nn1 = n1.isalpha()
                nn2 = n2.isalpha()
                if(nn1 == True and nn2 == True):
                    print("Both", n1, " and ", n2, " are string")
                    print("Invlid input")
                    print("Try again")
                    print("\n==================== < Your choice was Floor Division > ===================\n")
                elif(nn1 == False and nn2 == False):
                    print("Enter the numbers again ==> Invlid input")
                    print("Try again")
                    print("\n==================== <Your choice was Floor Division > ===================\n")
                else:
                    if(nn1 == True):
                        print(n1, " is a String")
                        print("Invalid input")
                        print("Try again")
                        print("\n==================== < Your choice was Floor Division > ===================\n")
                    elif(nn2 == True):
                        print(n2, " is a String")
                        print("Invalid input")
                        print("Try again")
                        print("\n==================== <Your choice was Floor Division > ===================\n")
# ==================== < DIVISION > =================== #

# ==================== < MODULUS > =================== #
        elif(choice == 6):
            print("\n==================== < Your choice is MODULUS > ===================\n")
            n1 = input("Enter first number as A ==>")
            an1 = n1
            if(an1 == ""):
                print("\nA is empty !!")
                print("Try Again\n")
            n2 = input("Enter Second number as B ==>")
            bn2 = n2
            if(bn2 == ""):
                print("\nB is empty !!")
                print("Try Again\n")
            try:
                na1 = float(n1)
                nb2 = float(n2)
                mod = na1 % nb2
                print("\n\n*****************************************")
                print("**                                     ")
                print("**   MODULUS of ", na1, "%", nb2, " ==>", mod)
                print("**                                     ")
                print("*****************************************\n\n")
                print("\n==================== < Your choice was MODULUS > ===================\n")
            except ValueError:
                nn1 = n1.isalpha()
                nn2 = n2.isalpha()
                if(nn1 == True and nn2 == True):
                    print("Both", n1, " and ", n2, " are string")
                    print("Invlid input")
                    print("Try again")
                    print("\n==================== < Your choice was MODULUS > ===================\n")
                elif(nn1 == False and nn2 == False):
                    print("Enter the numbers again ==> Invlid input")
                    print("Try again")
                    print("\n==================== <Your choice was MODULUS > ===================\n")
                else:
                    if(nn1 == True):
                        print(n1, " is a String")
                        print("Invalid input")
                        print("Try again")
                        print(
                            "\n==================== < Your choice was MODULUS > ===================\n")
                    elif(nn2 == True):
                        print(n2, " is a String")
                        print("Invalid input")
                        print("Try again")
                        print("\n==================== <Your choice was MODULUS > ===================\n")
# ==================== < MODULUS > =================== #

# ==================== < EXPONENTIATION > =================== #
        elif(choice == 7):
            print("\n==================== < Your choice is EXPONENTIATION > ===================\n")
            n1 = input("Enter first number as A ==>")
            an1 = n1
            if(an1 == ""):
                print("\nA is empty !!")
                print("Try Again\n")
            n2 = input("Enter Second number as B ==>")
            bn2 = n2
            if(bn2 == ""):
                print("\nB is empty !!")
                print("Try Again\n")
            try:
                na1 = float(n1)
                nb2 = float(n2)
                mod = na1 ** nb2
                print("\n\n*****************************************")
                print("**                                     ")
                print("**   EXPONENTIATION (A^B) of ",na1, "**", nb2, " ==>", mod)
                print("**                                     ")
                print("*****************************************\n\n")
                print("\n==================== < Your choice was EXPONENTIATION > ===================\n")
            except ValueError:
                nn1 = n1.isalpha()
                nn2 = n2.isalpha()
                if(nn1 == True and nn2 == True):
                    print("Both", n1, " and ", n2, " are string")
                    print("Invlid input")
                    print("Try again")
                    print("\n==================== < Your choice was EXPONENTIATION > ===================\n")
                elif(nn1 == False and nn2 == False):
                    print("Enter the numbers again ==> Invlid input")
                    print("Try again")
                    print("\n==================== <Your choice was EXPONENTIATION > ===================\n")
                else:
                    if(nn1 == True):
                        print(n1, " is a String")
                        print("Invalid input")
                        print("Try again")
                        print("\n==================== < Your choice was EXPONENTIATION > ===================\n")
                    elif(nn2 == True):
                        print(n2, " is a String")
                        print("Invalid input")
                        print("Try again")
                        print("\n==================== <Your choice was EXPONENTIATION > ===================\n")
# ==================== < EXPONENTIATION > =================== #

# math.ceil :- It rounds the number up to the nearest integer.
# ==================== < Get table > =================== #
        elif(choice == 8):
            print("\n==================== < Your choice is Get table > ===================\n")
            n1 = input("Enter a number to get its table as A ==>")
            an1 = n1
            if(an1 == ""):
                print("\nA is empty !!")
                print("Try Again\n")
            try:
                na1 = float(n1)
                for x in range(1, 11):
                    print("\n\t\t", math.ceil(na1),
                          "*", x, "=", math.ceil(na1*x))
                print("\n\n==================== < Your choice was Get table > ===================\n")
            except ValueError:
                nn1 = n1.isalpha()
                if(nn1 == True):
                    print(n1, " is a String")
                    print("Invalid input")
                    print("Try again")
                    print("\n==================== < Your choice was Get table > ===================\n")
                else:
                    print(n1, " is not a number")
                    print("\n==================== < Your choice was Get table > ===================\n")
# ==================== < Get table > =================== #

# ==================== < Get Square root > =================== #
        elif(choice == 9):
            print("\n==================== < Your choice is Get Square root > ===================\n")
            n1 = input("Enter a number to get its square root ==>")
            an1 = n1
            if(an1 == ""):
                print("\nA is empty !!")
                print("Try Again\n")
            try:
                na1 = float(n1)
                if(na1 >= 0 or na1 < 0):
                    print("Square root of ==>", na1, "==>", math.sqrt(na1))
                    print("\n==================== < Your choice was Get Square root > ===================\n")
            except ValueError:
                nn1 = n1.isalpha()
                if(nn1 == True):
                    print(n1, " is a String")
                    print("Invalid input")
                    print("Try again")
                    print("\n==================== < Your choice was Get Square root >===================\n")
                else:
                    print(n1, " is not a number")
                    print("\n==================== < Your choice was Get Square root > ===================\n")
# ==================== < Get Square root > =================== #

# ==================== < Get Absolute value > =================== #
        elif(choice == 10):
            print("\n==================== < Your choice is Get Absolute value > ===================\n")
            n1 = input("Enter a number to get its Get Absolute value ==>")
            an1 = n1
            if(an1 == ""):
                print("\nA is empty !!")
                print("Try Again\n")
            try:
                na1 = float(n1)
                if(na1 >= 0 or na1 < 0):
                    print("Absolute value of ==>", na1, "==>", abs(na1))
                    print("\n==================== < Your choice was Get Absolute value > ===================\n")
            except ValueError:
                nn1 = n1.isalpha()
                if(nn1 == True):
                    print(n1, " is a String")
                    print("Invalid input")
                    print("Try again")
                    print("\n==================== < Your choice was Get Absolute value >===================\n")
                else:
                    print(n1, " is not a number")
                    print("\n==================== < Your choice was Get Absolute value > ===================\n")
# ==================== < Get Absolute value > =================== #

# ==================== < Find Greater number > =================== #
        elif(choice == 11):
            print("\n==================== < Your choice is Find Greater number > ===================\n")
            n1 = input("Enter first number as A ==>")
            an1 = n1
            if(an1 == ""):
                print("\nA is empty !!")
                print("Try Again\n")
            n2 = input("Enter Second number as B ==>")
            bn2 = n2
            if(bn2 == ""):
                print("\nB is empty !!")
                print("Try Again\n")
            try:
                na1 = float(n1)
                nb2 = float(n2)
                if(na1 > nb2):
                    print("A=", na1, " is greater than B=", nb2)
                    print("\n==================== < Your choice was Find Greater number > ===================\n")
                elif(na1 < nb2):
                    print("B=", nb2, " is greater than A=", na1)
                    print("\n==================== < Your choice was Find Greater number > ===================\n")
                elif(na1 == nb2):
                    print("A=", na1, " & B=", nb2, " both are equal numbers")
                    print("\n==================== < Your choice was Find Greater number > ===================\n")
            except ValueError:
                nn1 = n1.isalpha()
                nn2 = n2.isalpha()
                if(nn1 == True and nn2 == True):
                    print("Both", n1, " and ", n2, " are string")
                    print("Invlid input")
                    print("Try again")
                    print("\n==================== < Your choice was Find Greater number > ===================\n")
                elif(nn1 == False and nn2 == False):
                    print("Enter the numbers again ==> Invlid input")
                    print("Try again")
                    print("\n==================== <Your choice was Find Greater number > ===================\n")
                else:
                    if(nn1 == True):
                        print(n1, " is a String")
                        print("Invalid input")
                        print("Try again")
                        print(
                            "\n==================== < Your choice was Find Greater number > ===================\n")
                    elif(nn2 == True):
                        print(n2, " is a String")
                        print("Invalid input")
                        print("Try again")
                        print(
                            "\n==================== <Your choice was Find Greater number > ===================\n")
# ==================== < Find Greater number > =================== #

# ==================== < Get Factorial of number > =================== #
        elif(choice == 12):
            print("\n==================== < Your choice is Get Factorial of number > ===================\n")
            n1 = input("Enter a number to get its Get Factorial of number ==>")
            an1 = n1
            if(an1 == ""):
                print("\nA is empty !!")
                print("Try Again\n")
            try:
                na1 = int(n1)
                print("Factorial of number value of ==>",
                      na1, "==>", math.factorial(na1))
                print("\n==================== < Your choice was Get Factorial of number > ===================\n")
            except ValueError:
                nn1 = n1.isalpha()
                if(nn1 == True):
                    print(n1, " is a String")
                    print("Invalid input")
                    print("Try again")
                    print("\n==================== < Your choice was Get Factorial of number >===================\n")
                else:
                    print(n1, " is not a number")
                    print("\n==================== < Your choice was Get Factorial of number > ===================\n")
# ==================== < Get Factorial of number > =================== #

# ==================== < Swap Two numbers > =================== #
        elif(choice == 13):
            print("\n==================== < Your choice is Swap Two numbers > ===================\n")
            n1 = input("Enter first number as A ==>")
            an1 = n1
            if(an1 == ""):
                print("\nA is empty !!")
                print("Try Again\n")
            n2 = input("Enter Second number as B ==>")
            bn2 = n2
            if(bn2 == ""):
                print("\nB is empty !!")
                print("Try Again\n")
            try:
                na1 = float(n1)
                nb2 = float(n2)
                print("Befor Swapping A=", na1, " & B=", nb2)
                c = na1
                na1 = nb2
                nb2 = c
                print("After Swapping A=", na1, " & B=", nb2)
                print("\n==================== < Your choice was Swap Two numbers > ===================\n")
            except ValueError:
                nn1 = n1.isalpha()
                nn2 = n2.isalpha()
                if(nn1 == True and nn2 == True):
                    print("Both", n1, " and ", n2, " are string")
                    print("Invlid input")
                    print("Try again")
                    print("\n==================== < Your choice was Swap Two numbers > ===================\n")
                elif(nn1 == False and nn2 == False):
                    print("Enter the numbers again ==> Invlid input")
                    print("Try again")
                    print("\n==================== <Your choice was Swap Two numbers > ===================\n")
                else:
                    if(nn1 == True):
                        print(n1, " is a String")
                        print("Invalid input")
                        print("Try again")
                        print("\n==================== < Your choice was Swap Two numbers > ===================\n")
                    elif(nn2 == True):
                        print(n2, " is a String")
                        print("Invalid input")
                        print("Try again")
                        print("\n==================== <Your choice was Swap Two numbers > ===================\n")
# ==================== < Swap Two numbers > =================== #

# ==================== < EXITING FROM THE PROGRAM :- Means exiting from the loop > =================== #
        elif(choice == 14):
            print("\n============= < SCIENTIFIC CALCULATOR > =============")
            print("\n\n=============== < SUCCESSFULLY EXITED  > ===============")
            print("=\t\t\t*      *                       =")
            print("=\t\t\t *    *                        =")
            print("=\t\t\t  *  *                         =")
            print("=\t\t\t   **                          =")
            print("=\t\t\t   **                          =")
            print("=\t\t\t  *  *                         =")
            print("=\t\t\t *    *                        =")
            print("=\t\t\t*      *                       =")
            print("=============== < SUCCESSFULLY EXITED > ===============\n\n")
            break
# ==================== < EXITING FROM THE PROGRAM :- Means exiting from the loop > =================== #

# < EXITING FROM THE NESTED LOOP :- Means exiting from the inner loop and then, come inside the outer loop > #
        elif(choice >= 15 or choice <= 0):
            while True:
                print("\n==================== < Your choice is INVALID > ===================\n")
                print("No such choice available\n")
                print("Enter number as ==> 1,2,3,4,5,6,7,8,9,10,11,12,13,14")
                print("*      *")
                print(" *    * ")
                print("  *  * ")
                print("   ** ")
                print("   ** ")
                print("  *  * ")
                print(" *    * ")
                print("*      *")
                print("\nTry again")
                print("\n==================== < Your choice was INVALID > ===================\n")
                break
# < EXITING FROM THE NESTED LOOP :- Means exiting from the inner loop and then, come inside the outer loop > #

# < Exception error if input is a string or any special char then exiting from then inner loop and then,
# coming outside in the outer loop>#
    except ValueError:
        while True:
            txt = (choice.isalpha())
            if(txt == True):
                print("\n==================== < Your choice is INVALID > ===================\n")
                print(choice, " is a String")
                print("No such choice available\n")
                print("Enter number as ==> 1,2,3,4,5,6,7,8,9,10,11,12,13,14")
                print("*      *")
                print(" *    * ")
                print("  *  * ")
                print("   ** ")
                print("   ** ")
                print("  *  * ")
                print(" *    * ")
                print("*      *")
                print("\nTry again")
                print("\n==================== < Your choice was INVALID > ===================\n")
            else:
                print("\n==================== < Your choice is INVALID > ===================\n")
                print(choice, " is not a number")
                print("No such choice available\n")
                print("Enter number as ==> 1,2,3,4,5,6,7,8,9,10,11,12,13,14")
                print("*      *")
                print(" *    * ")
                print("  *  * ")
                print("   ** ")
                print("   ** ")
                print("  *  * ")
                print(" *    * ")
                print("*      *")
                print("\nTry again")
                print("\n==================== < Your choice was INVALID > ===================\n")
            break
#< Exception error if input is a string or any special char then exiting from then inner loop and then, coming outside in the outer loop>#

print("\n============= < SCIENTIFIC CALCULATOR > =============")