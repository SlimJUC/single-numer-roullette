from random import randint
    
print("============================================")

print("""        
        
        Welcome to single number Roulette

        You will be asked to pick a number from 0 to 36
        
        
        The program will tell you if you guessed the correct number
        
=============================================

        """ )

cont = input("Press enter to continue....") 
print(" ================================ ")
user_credit = int(input("Buy In Credit: "))
print(" ================================== ")

def Roulette():


    global user_credit
    if user_credit <= 0:
        print(" You do not have enough credits to play ")
        exit()
    else:
        
       user_num = int(input("Enter a number from 0 to 36: "))

       lucky_num = randint(0, 36)

       if user_num == lucky_num:
        user_credit += 36   
        print("""Congratulations, You guessed the correct numer!
        
        You have been credited  36 winnings
        
        Total Credit Available Now is: """ +str(user_credit))

       else:
           print ("Sorry, its not your lucky day. The lucky number was " + str(lucky_num))
           

    print ("====================================")
    again = input("Wanna try again? yes or no: ")
    for i in again:
        if again == "yes":
            user_credit-=1
            print ("Player Remaining Credit = " + str(user_credit))

            Roulette()
        elif again == "no":
            print("Thank you for playing...")
            exit()
        else:
            print("write 'yes' or 'no' no CAPS")   

Roulette()
print("============================================")
