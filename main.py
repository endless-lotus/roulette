import random

#Game Rules Can be here
#table view so it takes up set amount of room!
red = [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36]
black = [2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35]
#bets
a = "Red🔴 or Black⚫"
a_1 =  "Red🔴"
a_2 = "Black⚫"
b = "Odd or Even"
b_1 = "Odd"
b_2 = "Even"
c = "1 to 18 || 19 to 36"
c_1 = "1 to 18"
c_2 = "19 to 36"
d = "Dozens"
d_1 = "First Dozen"
d_2 = "Second Dozen"
d_3 = "Third Dozen"
#table view so it takes up set amount of room!
def table_view():
    return print("""   
    *  *   *                *                     *  *
                       /------\           *                         *
          *         ./--🔴⚫🔴--\.
                  ./--⚫  ---  ⚫--\.                      *
                 |--🔴  /  -  \  🔴--| *
*                |--⚫  |  ||  | ⚫--|                *
                 |--🔴  \  -  /  🔴--|                            *
                  .\--⚫  ---  ⚫--/.
            *       .\--⚫🔴⚫--/.           *
                       \------/                                                                
                 """)


#Player: have a print statement return info: money lost, money won, current balance
class Player: 
    def __init__(self, name, balance, bet_type, bet, bet_value, is_watching_ball_roll, lost_money, won_money, bet_text):
        self.name = name # = player's name input
        self.balance = balance # = player's current monetary value
        self.bet_type = ''
        self.bet = '' # = player's current variable value of bet
        self.bet_value = ''
        self.is_watching_ball_roll = ''
        self.lost_money = 0 #True or False to money being lost
        self.won_money = False #True or False to money being won
        self.bet_text = ''


    def is_picking_bet(self):
        self.bet_type = int(input("""
Please pick a number for the available bets:
 [1] {bet_a}
 [2] {bet_b}
 [3] {bet_c}
 [4] {bet_d}\n""".format(bet_a=a,bet_b=b,bet_c=c,bet_d=d)))
        if self.bet_type == 1: #Red or Black
             player_bet = int(input("Please pick which color you would like to place for your bet:\n[1] {bet_a1}\n[2] {bet_a2}\n".format(bet_a1=a_1,bet_a2=a_2)))
             if player_bet == 1: #for input 1
                  self.bet = a_1
             else: #for other inputs counted as 2
                  self.bet = a_2    
        elif self.bet_type == 2: #odd or even
             player_bet = int(input("Please pick which you would like for your bet:\n[1] {bet_b1}\n[2] {bet_b2}\n".format(bet_b1=b_1,bet_b2=b_2)))
             if player_bet == 1:
                  self.bet = b_1
             else:
                  self.bet = b_2 
        elif self.bet_type == 3: #1-18 or 19-36
             player_bet = int(input("Please pick which group you would like for your bet:\n[1] {bet_c1}\n[2] {bet_c2}\n".format(bet_c1=c_1,bet_c2=c_2)))
             if player_bet == 1:
                  self.bet = c_1
             else:
                  self.bet = c_2 
        elif self.bet_type == 4: #Dozens
             player_bet = int(input("Please pick one of the three you would like for your bet:\n[1] {bet_d1}\n[2] {bet_d2}\n[3] {bet_d3}\n".format(bet_d1=d_1,bet_d2=d_2,bet_d3=d_3)))
             if player_bet == 1:
                  self.bet = d_1 #first dozen
             elif player_bet == 2:
                 self.bet = d_2 #second dozen
             else:
                  self.bet = d_3 #third dozen
        else:
             print("ERROR - int input")
        return self.bet, self.bet_type
        
    # To get the amount of money the player would like to place on the bet
    def is_placing_bet(self):
         self.bet_value = int(input("For your bet placed on {bet} how much money would you like to pin on that partner? Your current balance is: {balance}\n".format(bet=self.bet, balance=self.balance)))
         if self.bet_value > self.balance: #to make sure no inputs are allowed higher than existing balance
              print("Woah there Partner! You don't have that much in your balance, how about you try that again.")
         elif self.bet_value <= 0: #to make sure no inputs 0 or below are entered
             print("Inadequte amount for bet.")
         else:
            table_view()
            print("The ball is now rolling as all bets have been placed. . .") 
         return self.bet_value #This Works!!!! returns int input for bet!
    
    #picks random number in in the 1-36 for the wheel
    def is_watching_the_ball_roll(self):
        wheel = list(range(1, 37))
        self.is_watching_ball_roll = random.choice(wheel)
        return print("The ball has landed on {number}!".format(number=self.is_watching_ball_roll)) 
        
    #FUCK YES IT WORKS --> was using wrong iteration of loops 
    def is_calculating_bet(self):
        if self.bet == a_1: #Red
            if self.is_watching_ball_roll in red:
                self.won_money = True
            else:
                self.won_money = False
        elif self.bet == a_2: #Black
            if self.is_watching_ball_roll in black:
                self.won_money = True
            else:
                self.won_money = False
        elif self.bet == b_1: #Odd
            if self.is_watching_ball_roll % 2 != 0:
                self.won_money = True
            else:
                self.won_money = False
        elif self.bet == b_2: #Even
            if self.is_watching_ball_roll % 2 == 0:
                self.won_money = True
            else:
                self.won_money = False
        elif self.bet == c_1: #1 to 18
            if self.is_watching_ball_roll in range(1, 19):
                self.won_money = True
            else:
                self.won_money = False
        elif self.bet == c_2: #19-36
            if self.is_watching_ball_roll in range(19, 37):
                self.won_money = True
            else:
                self.won_money = False
        elif self.bet == d_1: #first dozen
            if self.is_watching_ball_roll in range(1, 13):
                self.won_money = True
            else:
                self.won_money = False
        elif self.bet == d_2: #second dozen
            if self.is_watching_ball_roll in range(13, 25):
                self.won_money = True
            else:
                self.won_money = False
        elif self.bet == d_3: #third dozen
            if self.is_watching_ball_roll in range(25, 37):
                self.won_money = True
            else:
                self.won_money = False
        else:
            print("ERROR")
        return self.won_money   

#calculates balance after win or loss
    def is_calculating_balance(self):
        if self.won_money == True:
            #For different types of bets on roulette
            if self.bet_type == 1 or self.bet_type == 2 or self.bet_type == 3: #checking to see if black/red, odd/even, or 1-18/19-36 was chosen as bet type
                #For a 1 to 1 ratio
                self.balance += self.bet_value
                self.bet_text = 'won'
            elif self.bet_type == 4: #checking to see if bet is equal to dozens
                #Payout 2 to 1
                self.balance += (self.bet_value * 2)
                self.bet_text = 'won'
            else:
                print("ERROR")
        elif self.won_money == False:
            #For self.won_money == False
            self.balance -= self.bet_value
            self.bet_text = 'lost'
        else:
            print("ERROR")
        return print("{player} you have {won_or_loss} ${bet} your current balance is: ${balance}".format(player=self.name,won_or_loss=self.bet_text,bet=self.bet_value,balance=self.balance)), self.bet_value

#Add Welcome Print To Roulette


#Get inf for Player:
player_name = input("""
           *          *   *    *   *   *  *  *      *              *    *
       *  *       Welcome to Roulette!      *                   *                *
    *  *   *                *                     *  *
   |             1 to 18              |               19 to 36              |
   |--------------------|-------------|-------------|-----------------------|
   |  3🔴 6⚫ 9🔴 12🔴  |  15⚫ 18🔴  |  21🔴 24⚫  |  27🔴 30🔴 33⚫ 36🔴  | Red or Black
   |  2⚫ 5🔴 8⚫ 11⚫  |  14🔴 17⚫  |  20⚫ 23🔴  |  26⚫ 29⚫ 32🔴 35⚫  |
   |  1🔴 4⚫ 7🔴 10⚫  |  13⚫ 16🔴  |  19🔴 22⚫  |  25🔴 28⚫ 31⚫ 34🔴  | Odd or Even
   |--------------------|---------------------------|-----------------------|
   |     First Dozen    |        Second Dozen       |      Third Dozen      |   
                     
Howdy partner and welcome to the casino! This is your roulette board that shows all the available bets.
                    Just need to ask you a couple questions.
Startin' with, what is your name?
                 """)

player_balance = int(input("""
    Well that's amazin' {name} now to play your must fill you account. 
How much money would you like to play with?
                 """.format(name=player_name)))

#To Run Code Between Player and Casino
player = Player(player_name, player_balance,'', '', '', '', 0, False, '')

#casino.display_game_rules()
player.is_picking_bet() 
player.is_placing_bet() 
player.is_watching_the_ball_roll() 
player.is_calculating_bet() 
player.is_calculating_balance()