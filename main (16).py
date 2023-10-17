# natalie dent, CIS 113, 9-17-2023
# Casino Game

"""
1.import random 
1.5 playAgain = true
2. print welcome message
3. print rules
3.5  x = randint range(1,37)
3.7 while playAgain == true
  3.8 print win variable with message (you won x times)
  3.9 
4. ask player to select game using input statements

5. if gameType is '1' then print("you choose straight up")
6. ask player to guess a number from 1-36 using int input statement
7. print random number
8. if their guess == random number then they win 35 * their bet +5 ($5) and if not then print("you lose)

9. elif gametype = '2' Print("You choose split game")
10. ask for a number in the range (2, 35) using int input statement
11. print random number
12. if guess == x or guess +- 1 is equal to x then print("you win") they      the win 17 * their bet + their og bet ($5); else print("you lose")

13. elif gametype = '3' print("you choose street game")
14. ask for a number that is divisible by three using int input statement
15. print x (random number)
16. if guess == x or guess - 1 == x or guess - 2 == x then print("you win") they win their bet * 11 + their og bet($5); else print("you lose")

17. elif gametype = '4' print("you choose top")
18. print x
19. if x is in range (1,19) then print(you win) they then win $10 + their     og bet($5); else print("you lose")

20. elif gametype = '5' print("you choose bottom")
21. print x 
22. if x is in range(19,37) then print("you win") they then win $10 +         their og bet ($5); else print(you lose)

23. elif gametype == '6' print("you choose even/odd")
24. even/odd = int(input("are you betting on even('enter (2)') or odd('enter (1)'): ))
print('x')
25. if x%2 = 0 AND even/odd == '2':
      print("you win $10 plus your original $5")
    elif x%2 = 0 AND even/odd == '1':
      print("you lose")
    if x%2 = 1 AND even?odd == '1':
      print("you won $10 plus og amount")
    elif x%2=1 AND even/odd == '2':
      print("you lose")
    else:
    print("you did not follow instructions)

26. elif gameType == '7' Print("menu")
27. make 12 different variables for each gameType win and loss
    ex.
      a = 0 (splitGame win), b = 0 (splitGame loss); d= 0(top win), e = 0(top loss)
28. in each gametype after the player has won add 1 to the corresponding variable
29. in each gametype after the player has lost subtract one to the corresponding variable
30. in elif gameType == '7' print each variable with its gametype and correct label
    ex.
      Split Game: x wins, y losses
      (code: print("split Game: ", a, "wins", b, "losses))

ALSO
  1. IF PLAYER WON ADD 1 TO WIN VARIABLE (unique to each game)
  2 ask user if want to play again in every game
  3a. if 0: playAgain = true
  3b. if not: playAgain = false 
print("thanks for playing") 
"""
#menu
"""
StraightW = straight win, StraightL = straight loss; StreetW = street win, StreetL = street Loss; TopW = top win, TopL = top loss; BotW = bottom win, BotL = bottom loss EvenOddW = even odd win, EvenOddL = Even odd loss; splitW = split win, splitL = split loss
"""
import random
playAgain = True 
scoreboard = {"straight":0,"split":0,"street":0,"top":0,"bottom":0,"even/odd":0}




print("welcome to Roulette!!") #header
print()
print("Instructions: You bet $5 and choose the gametype that you want to play. \n \nGame types ************************** \nstraight up: is a single number section where your guess a number \n\t1-36 in hopes that the random number will be the same \n\tyou can win $175 \nsplit: beting on 2 adjacent numbers in hopes that one of the them \n\twill be the same as the random number \n\tyou can win $85 \nstreet: when you  bet on a number and the two above it (since board \n\thas 3 columms the number that starts the row is divisible by 3 \n\tyou can win $55")  #first half of game explanation
print("Top: bets that the random number is between 1-18 (inclusive) if won \n\tyou win even money($10) \nBottom: betting that the random number will land between 19 and 36 \n\t(inclusive) if won you win even($10) \nEven/Odd: covers all evens OR all odds if won you win even($10)")
playAgain = True #variable that controls the loop
print("")

  
while playAgain == True:
  print()
  print(scoreboard)
  x = random.randint(1,36) #random number
  print()
  print("**** spinning the wheel ****")
  
  print("enter the number corrosponding with the game")
  print("Straight up: 1 \nsplit: 2 \nstreet: 3 \nTop: 4 \nBottom: 5 \nEven/Odd: 6 ")
  print()
  gameType = int(input("enter your gametype: ")) #choosing game
  
  if gameType == 1:
    print("you choose straight up")
    guess = int(input("guess a number from 1 - 36: "))
    print("************** Spining Wheel ***********")
    print("The number is ",x)
    if guess > 36 or guess < 1: #if guess is not in range
      print("invalid guess")
    elif guess == x: #if random number = guess
      print("You win $175 plus your original $5!!")
      scoreboard.update({"straight":+1})
      print(scoreboard) #prints scoreboard
    else:
      print("you lose!")
      scoreboard.update({"straight":-1})
      print(scoreboard)
      #updating playAgain variable
    betting = int(input("enter 0 if you want to play again? Enter any other number to quit ")) 
    if betting == 0:
      playAgain == True
    else:
      break #leave loop
      
  elif gameType == 2:
    print("you choose the split game")
    guess = int(input("guess a number from 2 - 35: "))#not 1 or 36 as it would complicate code
    print("************** Spining Wheel ***********")
    print("The number is ",x)
    if guess == x or (guess - 1 == x) or (guess + 1 == x): #if x is the same as guess or +- guess
      print("You win $85 plus your original $5!!")
      scoreboard.update({"split":+1}) #add to split game tracker
      print(scoreboard)
    else:
      print("you lose!")
      scoreboard.update({"split":-1}) #subtract to split game tracker
      print(scoreboard)
    betting = int(input("enter 0 if you want to play again? Enter any other number to quit ")) 
    if betting == 0:
      playAgain == True
    else:
      break #leave loop
      
  elif gameType == 3:
    print("you choose the street game")
    guess = int(input("guess a number from 1-36 that is divisible by 3: "))
    if (guess%3 != 0) or (guess <=1) or (guess > 36): #if user did not guess a number divisible by three or within range
      print("invalid guess")
      continue
    print("************** Spining Wheel ***********")
    print("The number is ",x)
    if guess == x or (guess - 1 == x) or (guess - 2 == x): #guess = guess, guess - 1, and guess - 2
      print("You win $55 plus your original $5!!")
      scoreboard.update({"street":+1}) #add to street tracker
      print(scoreboard) #prints scoreboard
    else:
      print("you lose!")
      scoreboard.update({"street":-1}) #add to street lose tracker
      print(scoreboard) #prints scoreboard
      #playAgain function
    betting = int(input("enter 0 if you want to play again? Enter any other number to quit ")) 
    if betting == 0:
      playAgain == True
    else:
      break #leave loop
      
  elif gameType == 4: #Top
    print("you choose Top")
    print("************** Spining Wheel ***********")
    print("The number is ",x)
    if x in range(1,19): #if x is between 1 and 18
      print("You win $10 plus your original $5!!")
      scoreboard.update({"top":+1}) #add to top tracker
      print(scoreboard) #print scoreboard
    else:
      print("you lose!")
      scoreboard.update({"top":-1}) #add to top lose tracker
      print(scoreboard) #prints scoreboard
      #playAgain function
    betting = int(input("enter 0 if you want to play again? Enter any other number to quit ")) 
    if betting == 0:
      playAgain == True #if user enters 0 keep looping
    else:
      break #leave loop
      
  elif gameType == 5:
    print("you choose Bottom")
    print("************** Spining Wheel ***********")
    print("The number is ",x)
    if x in range(19,37): #if x is between 19 and 37
      print("You win $10 plus your original $5!!")
      scoreboard.update({"bottom": +1}) #add to bottom tracker
      print(scoreboard) #print scoreboard
    else:
      print("you lose!")
      scoreboard.update({"bottom":+1}) #add to bottom lose tracker
      print(scoreboard) #print scoreboard
      #playAgain Function
    betting = int(input("enter 0 if you want to play again? Enter any other number to quit ")) 
    if betting == 0: #if user enters zero
      playAgain == True #keep looping
    else:
      break #leave loop

  elif gameType == 6:
    print("you choose even/odd")
    evenOdd = int(input("are you betting on even(if so enter '2') or odd(if so enter '1')? "))
    print("************** Spining Wheel ***********")
    print(x)
    if (x%2 == 0) and (evenOdd == 2): #if even and guessed even
      print("you win $10 plus your original $5")
      scoreboard.update({"even/odd":+1}) #add to even odd win tracker
      print(scoreboard) #print scoreboard
    elif (x%2 == 0) and (evenOdd == 1): #if even but guessed odd
      print("you lose") 
      scoreboard.update({"even/odd":-1}) #add to even odd lose tracker
      print(scoreboard) #print scoreboard
    elif (x%2 == 1) and (evenOdd == 1): #if odd and guessed odd
      print("you win $10 plus your original $5")
      scoreboard.update({"even/odd":+1}) #add to even odd win tracker
      print(scoreboard) #print scoreboard
    elif (x%2 == 1) and (evenOdd == 2): #if odd but guessed even
      print("you lose")
      scoreboard.update({"even/odd":-1}) #add to even odd lose tracker
      print(scoreboard) #print scoreboard
    else:
      print("you did not follow instructions :(") #if you did not input '1' or '2'
      #playAgain Function
    betting = int(input("enter 0 if you want to play again? Enter any other number to quit ")) 
    if betting == 0:
      playAgain == True
    else:
      break #leave loop
      
  else:
    print("invalid input")
    print("try again")

print()
print("Thanks for playing!! Bye!")



  
      
