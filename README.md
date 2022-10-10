# Computer-Vision-Rock-Paper-Scissors: MANUAL RPS
Coding ROCK, PAPER, SCISSORS game in Python
1. Import Random, which let's the computer select Rock, Paper or Scissors randomly.
n is the number of games you set to play.
2. Define the function play
3. Set the user's choice, here, it is R for Rock, P for Paper and S for Scissors.
4. Make the inputs upper case just in case someone inputs a lower case r, p or s, it does not register it as not Rock, Paper or Scissors.
5. Have the computer choose between the three choices (R, P, or S) randomly.
Having defined our functions of the user choice and the computer choice, we will proceed to play to determnine who wins. Again, we need to define the function to show who wins, who loses or when there is a tie.
6. Again, we define the function to get winner and play. You notice that you need to run the script each time you want to play. We can define another function that will allow us play the best out of a certain number of times/games (say n times) this, I will create another python file (manual_rps2.py) that will allow us play for n times an stop if the user wins up to seil, which is half the number of times set to play, the game ends. So if n=4, you will keep playing till you win n/2, which is 4/2 = 2. So you will play till you win 2 out of the set 4 number of games. So if n = 5, n/2 = 5/2 = 2.5 and it's aproximately 3. So you will win 3 times (3/5). If n = 7, 7/2 = 3.5 = 4 ==> 4/7.
We will initialize two variables in this function. User choice wins and computer choice wins and both are zero. We will also initialize wins neccessary, which is the number you get when you divide n by 2 and get the ceil value. Note, you will need to import the math module. We will play for n = 7 and 11.
For n=7, the ceil value will be 7/2 = 3.5 = 4. You will need to win 4 games.
For n=11, the ceil value will be 11/2 = 5.5 = 6. You will need to win 6 games.

We will now use a while loop. The resason for using a while loop is because we don't know how many times (iterations) we will play the game to achieve the number of wins necessary.
We can also set the while loop to say, if the user or the computer achieve this wins necessary, stop the loop, otherwise keep playing till the wins necessary is achieved.
We will also change what the play function returns.
we will return o for tie, 1 for user choice wins and -1 for computer wins.
We need to increament user win by 1


CAMERA RPS
This was approached using the Object Oriented Programming (OOP) technique. In this technique, 


 # Step 1: Create a list of choices (Rock,Paper, Scissors) and assign it to a variable called choices.
        # Step 2: Use random.choice method to randomly select a choice from the above created list of choices and assign this to a variable called comp_choice.
        # Step 3: Return comp_choice