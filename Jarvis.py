import pyttsx3
import random
speaker = pyttsx3.init()
speaker.say(
    'Hello sir,i am jarvis,select a command for me')
speaker.runAndWait()
while True:
    userinput = input('''please select what you want to do--
    1 - convert text to audio
    2 - play a song for me
    3 - lets play game
    4 - exit
    Type here----- ''')
    if userinput == '1':
        speaker.say('Enter the text that you want to convert into audio')
        speaker.runAndWait()
        text = input('please Enter the Text\n')
        speaker.say(text)
        speaker.runAndWait()
    elif userinput == '2':
        speaker.say('''playing justin beiber song - peaches
            I got my peaches out in Georgia

(Oh yeah, shit)

I get my weed from California

(That's that shit)

I took my chick up to the North, yeah

(Bad ass bitch)

I get my light right from the source, yeah

(Yeah, that's it)
''')
        speaker.runAndWait()
    elif userinput == '3':
        speaker.say('lets play Rock,Paper,scissors')
        speaker.runAndWait()
        print("Winning Rules of the Rock paper scissor game as follows: \n"
                                +"Rock vs paper->paper wins \n"
                                + "Rock vs scissor->Rock wins \n"
                                +"paper vs scissor->scissor wins \n")
  
        while True:
            print("Enter choice \n 1. Rock \n 2. paper \n 3. scissor \n")
            
            # take the input from user
            speaker.say('Enter your choice Sir')
            speaker.runAndWait()
            choice = int(input("User turn: "))
        
            # OR is the short-circuit operator
            # if any one of the condition is true
            # then it return True value
            
            # looping until user enter invalid input
            while choice > 3 or choice < 1:
                choice = int(input("enter valid input: "))
                speaker.say('Enter Valid Input sir')
                speaker.runAndWait()

                
        
            # initialize value of choice_name variable
            # corresponding to the choice value
            if choice == 1:
                choice_name = 'Rock'
            elif choice == 2:
                choice_name = 'paper'
            else:
                choice_name = 'scissor'
                
            # print user choice 
            print("user choice is: " + choice_name)
            print("\nNow its computer turn.......")
        
            # Computer chooses randomly any number 
            # among 1 , 2 and 3. Using randint method
            # of random module
            comp_choice = random.randint(1, 3)
            
            # looping until comp_choice value 
            # is equal to the choice value
            while comp_choice == choice:
                comp_choice = random.randint(1, 3)
        
            # initialize value of comp_choice_name 
            # variable corresponding to the choice value
            if comp_choice == 1:
                comp_choice_name = 'Rock'
            elif comp_choice == 2:
                comp_choice_name = 'paper'
            else:
                comp_choice_name = 'scissor'
                
            print("Computer choice is: " + comp_choice_name)
        
            print(choice_name + " V/s " + comp_choice_name)
        
            # condition for winning
            if((choice == 1 and comp_choice == 2) or
            (choice == 2 and comp_choice ==1 )):
                print("paper wins => ", end = "")
                result = "paper"
                
            elif((choice == 1 and comp_choice == 3) or
                (choice == 3 and comp_choice == 1)):
                print("Rock wins =>", end = "")
                result = "Rock"
            else:
                print("scissor wins =>", end = "")
                result = "scissor"
        
            # Printing either user or computer wins
            if result == choice_name:
                print("<== User wins ==>")
                speaker.say('ohh great ! You win sir')
                speaker.runAndWait()
            else:
                print("<== Jarvis wins ==>")
                speaker.say('Ha ha ha!! You lost Sir')
                speaker.runAndWait()
                
            print("Do you want to play again? (Y/N)")
            speaker.say('Do you want to play again?')
                
            speaker.runAndWait()
            ans = input()
        
        
            # if user input n or N then condition is True
            if ans == 'n' or ans == 'N':
                break
            
        # after coming out of the while loop
        # we print thanks for playing
        print("\nThanks for playing")
        speaker.say('Thanks for Playing')
        speaker.runAndWait()
        
            
    elif userinput == '4':
        break
    else:
        print('please Enter a valid key')
        speaker.say('Please Enter a valid key')
        speaker.runAndWait()


speaker.say('come again ,have a nice day')
speaker.runAndWait()
