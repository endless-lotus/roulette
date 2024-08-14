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
#table view so it takes up set amount of room!
def table_view():
    return print("""
                 ♠♤♠**♡♥♡**♦♢♦**♧♣♧**♠♤♠**♡♥♡**♦♢♦**♧♣♧**♠♤♠**ROULETTE**♧♣♧**♠♤♠**♡♥♡**♦♢♦**♧♣♧**♠♤♠**♡♥♡**♦♢♦**♧♣♧**♠♤♠**♡♥♡**♦♢♦     
                            
                        
                                |             1 to 18              |               19 to 36              |
                                |--------------------|-------------|-------------|-----------------------|
                                |  3🔴 6⚫ 9🔴 12🔴  |  15⚫ 18🔴  |  21🔴 24⚫  |  27🔴 30🔴 33⚫ 36🔴  | Red or Black
                                |  2⚫ 5🔴 8⚫ 11⚫  |  14🔴 17⚫  |  20⚫ 23🔴  |  26⚫ 29⚫ 32🔴 35⚫  |
                                |  1🔴 4⚫ 7🔴 10⚫  |  13⚫ 16🔴  |  19🔴 22⚫  |  25🔴 28⚫ 31⚫ 34🔴  | Odd or Even
                                |--------------------|---------------------------|-----------------------|
                                |     First Dozen    |        Second Dozen       |      Third Dozen      |                                                                   
                 """)


#Player: have a print statement return info: money lost, money won, current balance
class Player: 
    def __init__(self, name, balance, bet_type, bet, bet_value, is_watching_ball_roll, lost_money, won_money):
        self.name = name # = player's name input
        self.balance = balance # = player's current monetary value
        self.bet_type = ''
        self.bet = '' # = player's current variable value of bet
        self.bet_value = ''
        self.is_watching_ball_roll = ''
        self.lost_money = 0 #True or False to money being lost
        self.won_money = False #True or False to money being won


    def is_picking_bet(self):
        self.bet_type = int(input("""
♠♤♠**♡♥♡**♦♢♦**♧♣♧**♠♤♠**♡♥♡**♦♢♦**♧♣♧**♠♤♠**♡♥♡**♦♢♦**♧♣♧**♠♤♠**♡♥♡**♦♢♦**♧♣♧**♠♤♠
Please pick a number for the available bets:
 [1] {bet_a}
              """.format(bet_a=a)))
        if self.bet_type == 1:
             player_bet = int(input("""
Please pick which color you would like to place your bet on:
 [1] {bet_a1}
 [2] {bet_a2}
                                    """.format(bet_a1=a_1, bet_a2=a_2)))
             if player_bet == 1:
                  self.bet = a_1
             else:
                  self.bet = a_2     
        else:
             print("Invalid Input please try again.")
        return self.bet, print(self.bet_type)
        
    def is_placing_bet(self):
         self.bet_value = int(input("For your bet placed on {bet} how much money would you like to pin on that partner? Your current balance is: {balance}\n".format(bet=self.bet, balance=self.balance)))
         if self.bet_value > self.balance:
              print("Woah there Partner! You don't have that much in your balance, how about you try that again.")
         elif self.bet_value <= 0:
             print("Inadequte amount for bet.")
         else:
            table_view()
            print("The ball is now rolling as all bets have been placed. . .") 
         return self.bet_value #This Works!!!! returns int input for bet!
    
    def is_watching_the_ball_roll(self):
        wheel = list(range(1, 37))
        self.is_watching_ball_roll = random.choice(wheel)
        return print("The ball has landed on {number}!".format(number=self.is_watching_ball_roll)) #this works!!! I'm on a roll ^o^
        
    #FUCK YES IT WORKS --> was using wrong iteration of loops 
    def is_calculating_bet(self):
        if self.bet == a_1:
            if self.is_watching_ball_roll in red:
                self.won_money = True
            else:
                self.won_money = False
        elif self.bet == a_2:
            if self.is_watching_ball_roll in black:
                self.won_money = True
            else:
                self.won_money = False
        else:
            print("ERROR")
        return self.won_money   

    def is_calculating_balance(self):
        if self.won_money == True:
            #For different types of bets on roulette
            if self.bet_type == 1: #checking to see if its equal to a bet on Red or Black
                #For a 1 to 1 ratio
                self.balance += self.bet_value
            else:
                print("ERROR")
        elif self.won_money == False:
            #For self.won_money == False
            self.balance -= self.bet_value
        else:
            print("ERROR")
        return print(self.balance) #this works and is able to be used for later implementations
    
#print("🔴\nCongrats {player} you have won ${bet} on your bet for {bet_type}!".format(player=self.name, bet=self.bet_value, bet_type=self.bet))
#print("🔴⚫\n{player} its seems you have lost ${bet} on your bet for {bet_type}".format(player=self.name, bet=self.bet_value, bet_type=self.bet))
#print("Your current balance is: ${balance}".format(balance=self.balance))

#Get inf for Player:
player_name = input("""
♠♤♠**♡♥♡**♦♢♦**♧♣♧**♠♤♠**♡♥♡**♦♢♦**♧♣♧**♠♤♠**♡♥♡**♦♢♦**♧♣♧**♠♤♠**♡♥♡**♦♢♦**♧♣♧**♠♤♠
Howdy partner and welcome to the casino! Just need to ask you a couple questions.
Startin' with, what do they call you?
                 """)

player_balance = int(input("""
Well that's amazin' {name} now to play your must fill you account. 
How much rootin' tootin' money would you like to play with?
                 """.format(name=player_name)))

#To Run Code Between Player and Casino
player = Player(player_name, player_balance,'', '', '', '', 0, False)

#casino.display_game_rules()
player.is_picking_bet()
player.is_placing_bet()
player.is_watching_the_ball_roll()
player.is_calculating_bet()
player.is_calculating_balance()