import random

#Game Rules Can be here
wheel = list(range(1, 37))
spin_number = random.choice(wheel)
red = [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36]
black = [2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35]

#Player: Ask for BET, Ask for Starting Balance
class Player:
    def __init__(self, name, balance, bet, lost_money, won_money, is_picking_bet):
        self.name = name # = player's name input
        self.balance = balance # = player's current monetary value
        self.bet = '' # = player's bet on current game
        self.lost_money = 0 # holds value of money lost and maths it to balance
        self.won_money = 0 #holds value of won money and maths it to balance
        self.is_picking_bet = '' #picking type of bet holds value --> empty string to pick through letters or numbers 



#Casino: show table, roll wheel, bet ends set up another bet, types of bets? Needs 6
class Casino:
    pass
    def __init__(self, table, is_rolling_wheel, is_setting_up):
        self.table = table # = table view --> the roulette table art
        self.is_rolling_wheel = is_rolling_wheel #generating random number
        self.is_setting_up = is_setting_up #to start another bet after a round has ended successfully --> while loop
        

#Get inf for Player:
player_name = input("""
                ♠♤♠**♡♥♡**♦♢♦**♧♣♧**♠♤♠**♡♥♡**♦♢♦**♧♣♧**♠♤♠**♡♥♡**♦♢♦**♧♣♧**♠♤♠**♡♥♡**♦♢♦**♧♣♧**♠♤♠
                  Howdy partner and welcome to the casino! Just need to ask you a couple questions.
                    Startin' with, what do they call you?
              """)

player_balance = int(input("""
                ♠♤♠**♡♥♡**♦♢♦**♧♣♧**♠♤♠**♡♥♡**♦♢♦**♧♣♧**♠♤♠**♡♥♡**♦♢♦**♧♣♧**♠♤♠**♡♥♡**♦♢♦**♧♣♧**♠♤♠
                   Well that's amazin' {name} now to play you must fill you account. 
                   How much rootin tootin money would you like to play with? (Enter as int ex: 20)
                       """.format(name=player_name)))


#To Run Code Between Player and Casino
player = Player(player_name, player_balance, '', 0, 0, '')