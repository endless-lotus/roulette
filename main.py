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

    #can bet be done in here?
    # def player_is_picking_bet(self):
    # def player_bet(self):
    #     self.bet = int(input("{name} please place your desired bet amount. . . ").format(name=self.name))
    #     while self.bet > self.balance:
    #         self.bet = int(input("INVALID AMOUNT -- please enter bet amount again."))

    def is_picking_bet(self):
        player_bet = int(input("""
             ♠♤♠**♡♥♡**♦♢♦**♧♣♧**♠♤♠**♡♥♡**♦♢♦**♧♣♧**♠♤♠**♡♥♡**♦♢♦**♧♣♧**♠♤♠**♡♥♡**♦♢♦**♧♣♧**♠♤♠
              Please pick a number for the available bets:
              [1] {bet_a}
              """.format(bet_a=a)))
        return player_bet
        
    #player_lost_money
    #player_won_money


#Casino: show table, roll wheel, bet ends set up another bet, types of bets? Needs 6
class Casino:
    pass
    def __init__(self, balance):
        self.balance = player_balance * 10 # For the casino to play against player with --> either player wins or casino wins

    def display_game_rules(self):
        return print("""Game Rules Roulette:
                     {name} welcome to this terminal game of roulette! Here you are able to place bets to see if you can win against the casino.
                     This is possible via making the casino lose all of its money! 
                     The bets are ordered by varients for instance there is {bet_a}.
                     This is a bet in which you place in hopes the number will be {bet_a} if the number did not spin on whichever color you bet on you lose.
                     Roulette is a very simple game that depends soley on how the outcome of the role.
                     May the game be in your favor, good luck {name}!
                     """.format(name=player_name, bet_a=a))

    def show_bets(self):
        print(""" 
        These are your available bets:
              [1] {bet_a}
""")


#Get inf for Player:
player_name = input("""
                ♠♤♠**♡♥♡**♦♢♦**♧♣♧**♠♤♠**♡♥♡**♦♢♦**♧♣♧**♠♤♠**♡♥♡**♦♢♦**♧♣♧**♠♤♠**♡♥♡**♦♢♦**♧♣♧**♠♤♠
                  Howdy partner and welcome to the casino! Just need to ask you a couple questions.
                    Startin' with, what do they call you?
              """)

player_balance = int(input("""
                ♠♤♠**♡♥♡**♦♢♦**♧♣♧**♠♤♠**♡♥♡**♦♢♦**♧♣♧**♠♤♠**♡♥♡**♦♢♦**♧♣♧**♠♤♠**♡♥♡**♦♢♦**♧♣♧**♠♤♠
                   Well that's amazin' {name} now to play your must fill you account. 
                   How much rootin' tootin' money would you like to play with? (Enter as int ex: 20)
                       """.format(name=player_name)))

#To Run Code Between Player and Casino
player = Player(player_name, player_balance, 0, 0, '')
casino = Casino(player_balance)

casino.display_game_rules()
player.is_picking_bet()