import random

#Game Rules Can be here
#table view so it takes up set amount of room!
wheel = list(range(1, 37))
spin_number = random.choice(wheel)
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

#Player: Ask for BET, Ask for Starting Balance
class Player: 
    def __init__(self, name, balance, bet, lost_money, won_money):
        self.name = name # = player's name input
        self.balance = balance # = player's current monetary value
        self.bet = '' # = player's bet on current game
        self.lost_money = 0 # holds value of money lost and maths it to balance
        self.won_money = 0 #holds value of won money and maths it to balance

    def is_picking_bet(self):
        player_bet_num = int(input("""
♠♤♠**♡♥♡**♦♢♦**♧♣♧**♠♤♠**♡♥♡**♦♢♦**♧♣♧**♠♤♠**♡♥♡**♦♢♦**♧♣♧**♠♤♠**♡♥♡**♦♢♦**♧♣♧**♠♤♠
Please pick a number for the available bets:
 [1] {bet_a}
              """.format(bet_a=a)))
        if player_bet_num == 1:
             player_bet_num = int(input("""
Please pick which color you would like to place your bet on:
 [1] {bet_a1}
 [2] {bet_a2}
                                    """.format(bet_a1=a_1, bet_a2=a_2)))
             if player_bet_num == 1:
                  self.bet = a_1
             else:
                  self.bet = a_2     
        else:
             print("Invalid Input please try again.")
        return self.bet
        
    def is_placing_bet(self):
         player_bet_value = int(input("For your bet placed on {bet} how much money would you like to pin on that partner? Your current balance is: {balance}\n".format(bet=self.bet, balance=self.balance)))
         if player_bet_value > self.balance:
              print("Woah there Partner! You don't have that much in your balance, how about you try that again.")
         elif player_bet_value <= 0:
             print("Inadequte amount for bet.")
         else:
            print("The ball is now rolling as all bets have been placed. . .")
         return player_bet_value
        
    #player_lost_money
    
    #player_won_money


#Casino: show table, roll wheel, bet ends set up another bet, types of bets? Needs 6
#


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
player = Player(player_name, player_balance, 0, 0, '')
#casino = Casino(player_balance)

#casino.display_game_rules()
player.is_picking_bet()
player.is_placing_bet()